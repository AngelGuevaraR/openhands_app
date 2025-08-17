import flet as ft
import cv2
import base64
import mediapipe as mp
import threading
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class Abecedario:
    def __init__(self, page):
        self.page = page

        self.page.window_width = 900
        self.frame = None
        self.thread_running = True

        path = base64.b64encode(open("openhands_app/assets/Camara.png", "rb").read()).decode("utf-8")
        self.video1 = ft.Image(src_base64=path, expand=True)

        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            raise ValueError("No se logró conectar a la cámara")

        self.cameras = ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    border_radius=10,
                    content=self.video1
                )
            ]
        )

        self.threading = threading.Thread(target=self.update_frame_camera)
        self.threading.start()



    def interfazAprendizaje(self):
        return ft.Container(
            ft.Column(
                controls=[
                     ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                    ft.Image(
                                        src="openhands_app/assets/logo.png",
                                        height=50
                                        )
                                    ),
                                    ft.IconButton(icon=ft.Icons.EXIT_TO_APP, icon_color="black", on_click=self.exit_click, tooltip="Regresar")
                                ]
                        ),
                        ft.Container(
                            expand=True,
                            content= self.cameras
                        ),
                        ft.Text("Abecedario LSM:", size=16, weight=ft.FontWeight.BOLD),
                        ft.Container(content=ft.Image(src="openhands_app/assets/LSM.png", border_radius=5))
                ],
                
            ),
            border_radius=20,
            width=350,
            height=800,
            bgcolor= ft.Colors.WHITE,
        )
    
    def distancia_euclidiana(p1, p2):
        d = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        return d

    def draw_bounding_box(image, hand_landmarks):
        image_height, image_width, _ = image.shape
        x_min, y_min = image_width, image_height
        x_max, y_max = 0, 0
        
        # landmarks (marcas de mano)
        for landmark in hand_landmarks.landmark:
            x, y = int(landmark.x * image_width), int(landmark.y * image_height)
            if x < x_min: x_min = x
            if y < y_min: y_min = y
            if x > x_max: x_max = x
            if y > y_max: y_max = y
        
        # Draw the bounding box
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    def update_frame_camera(self):
        with mp_hands.Hands(
                    model_complexity=1,
                    min_detection_confidence=0.7,
                    min_tracking_confidence=0.7,
                    max_num_hands=1
                ) as hands:
            while self.thread_running:
                ret, frame = self.capture.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = hands.process(frame_rgb)

                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            mp_drawing.draw_landmarks(
                                frame, 
                                hand_landmarks, 
                                mp_hands.HAND_CONNECTIONS, 
                                mp_drawing_styles.get_default_hand_landmarks_style(), 
                                mp_drawing_styles.get_default_hand_connections_style()
                            )
                            
                            image_height, image_width, _ = frame.shape

                            index_finger_tip = (int(hand_landmarks.landmark[8].x * image_width),
                                            int(hand_landmarks.landmark[8].y * image_height))
                            index_finger_pip = (int(hand_landmarks.landmark[6].x * image_width),
                                            int(hand_landmarks.landmark[6].y * image_height))
                            
                            thumb_tip = (int(hand_landmarks.landmark[4].x * image_width),
                                            int(hand_landmarks.landmark[4].y * image_height))
                            thumb_pip = (int(hand_landmarks.landmark[2].x * image_width),
                                            int(hand_landmarks.landmark[2].y * image_height))
                            
                            middle_finger_tip = (int(hand_landmarks.landmark[12].x * image_width),
                                            int(hand_landmarks.landmark[12].y * image_height))
                            
                            middle_finger_pip = (int(hand_landmarks.landmark[10].x * image_width),
                                            int(hand_landmarks.landmark[10].y * image_height))
                            
                            ring_finger_tip = (int(hand_landmarks.landmark[16].x * image_width),
                                            int(hand_landmarks.landmark[16].y * image_height))
                            ring_finger_pip = (int(hand_landmarks.landmark[14].x * image_width),
                                            int(hand_landmarks.landmark[14].y * image_height))
                            
                            pinky_tip = (int(hand_landmarks.landmark[20].x * image_width),
                                            int(hand_landmarks.landmark[20].y * image_height))
                            pinky_pip = (int(hand_landmarks.landmark[18].x * image_width),
                                            int(hand_landmarks.landmark[18].y * image_height))
                            
                            wrist = (int(hand_landmarks.landmark[0].x * image_width),
                                            int(hand_landmarks.landmark[0].y * image_height))
                            
                            ring_finger_pip2 = (int(hand_landmarks.landmark[5].x * image_width),
                                            int(hand_landmarks.landmark[5].y * image_height))
                            
                            if abs(thumb_tip[1] - index_finger_pip[1]) < 45 \
                                and all(finger_tip[1] > finger_pip[1] for finger_tip, finger_pip in [
                                    (index_finger_tip, index_finger_pip),
                                    (middle_finger_tip, middle_finger_pip),
                                    (ring_finger_tip, ring_finger_pip),
                                    (pinky_tip, pinky_pip)
                                ]) and abs(thumb_tip[0] - index_finger_pip[0]) > 40:
                                cv2.putText(frame, 'A', (50, 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 
                                            2.0, (0, 0, 255), 4)
                                
                            elif index_finger_pip[1] - index_finger_tip[1]>0 and pinky_pip[1] - pinky_tip[1] > 0 and \
                                middle_finger_pip[1] - middle_finger_tip[1] >0 and ring_finger_pip[1] - ring_finger_tip[1] >0 and \
                                    middle_finger_tip[1] - ring_finger_tip[1] <0 and abs(thumb_tip[1] - ring_finger_pip2[1])<40:
                                cv2.putText(frame, 'B', (50, 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 
                                            2.0, (0, 0, 255), 4)
                                
                            elif abs(index_finger_tip[1] - thumb_tip[1]) < 260 and \
                                index_finger_tip[1] - middle_finger_pip[1]<0 and index_finger_tip[1] - middle_finger_tip[1] < 0 and \
                                    index_finger_tip[1] - index_finger_pip[1] > 0:
                                    cv2.putText(frame, 'G', (50, 50), 
                                                    cv2.FONT_HERSHEY_SIMPLEX, 
                                                    2.0, (0, 0, 255), 4)
                            
                            elif index_finger_pip[1] - index_finger_tip[1] < 0 and pinky_pip[1] - pinky_tip[1] < 0 and \
                                middle_finger_pip[1] - middle_finger_tip[1] < 0 and ring_finger_pip[1] - ring_finger_tip[1] < 0 \
                                    and abs(index_finger_tip[1] - thumb_tip[1]) < 100 and \
                                        thumb_tip[1] - index_finger_tip[1] > 0 \
                                        and thumb_tip[1] - middle_finger_tip[1] > 0 \
                                        and thumb_tip[1] - ring_finger_tip[1] > 0 \
                                        and thumb_tip[1] - pinky_tip[1] > 0:

                                cv2.putText(frame, 'E', (50, 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 
                                            2.0, (0, 0, 255), 4)
                            
                            elif abs(index_finger_tip[1] - index_finger_pip[1]) < 30 and \
                                abs(index_finger_tip[0] - thumb_tip[0]) < 70 and \
                                middle_finger_tip[1] > middle_finger_pip[1] and \
                                ring_finger_tip[1] > ring_finger_pip[1] and \
                                pinky_tip[1] > pinky_pip[1]:
                                cv2.putText(frame, 'C', (50, 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 
                                            2.0, (0, 0, 255), 4)
                            
                            elif abs(index_finger_tip[1] - middle_finger_tip[1]) < 30 and \
                                all(finger_tip[1] > finger_pip[1] for finger_tip, finger_pip in [
                                    (ring_finger_tip, ring_finger_pip),
                                    (pinky_tip, pinky_pip)
                                ]) and \
                                thumb_tip[0] < index_finger_pip[0] and \
                                abs(thumb_tip[1] - ring_finger_pip[1]) < 40:
                                cv2.putText(frame, 'H', (50, 50),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            2.0, (0, 0, 255), 4)
                                
                            elif pinky_tip[1] < pinky_pip[1] and \
                                all(finger_tip[1] > finger_pip[1] for finger_tip, finger_pip in [
                                    (index_finger_tip, index_finger_pip),
                                    (middle_finger_tip, middle_finger_pip),
                                    (ring_finger_tip, ring_finger_pip)
                                ]) and \
                                abs(thumb_tip[0] - index_finger_pip[0]) < 50:
                                cv2.putText(frame, 'I', (50, 50),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            2.0, (0, 0, 255), 4)
                            

                            elif abs(index_finger_tip[1] - middle_finger_tip[1]) < 50 and \
                                abs(index_finger_tip[0] - middle_finger_tip[0]) > 40 and \
                                all(finger_tip[1] > finger_pip[1] for finger_tip, finger_pip in [
                                    (ring_finger_tip, ring_finger_pip),
                                    (pinky_tip, pinky_pip)
                                ]) and \
                                thumb_tip[0] < index_finger_tip[0] and \
                                thumb_tip[0] > middle_finger_tip[0] and \
                                thumb_tip[1] > index_finger_tip[1]:
                                cv2.putText(frame, 'K', (50, 50),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            2.0, (0, 0, 255), 4)
                                
                            elif thumb_tip[1] < thumb_pip[1] and \
                                index_finger_tip[1] < index_finger_pip[1] and \
                                middle_finger_tip[1] > middle_finger_pip[1] and \
                                ring_finger_tip[1] > ring_finger_pip[1] and \
                                pinky_tip[1] > pinky_pip[1] and \
                                abs(index_finger_tip[0] - thumb_tip[0]) > 40:
                                cv2.putText(frame, 'L', (50, 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 
                                            2.0, (0, 0, 255), 4)

                    _, buffer = cv2.imencode(".png", frame)
                    self.frame = base64.b64encode(buffer).decode("utf-8")
                    self.video1.src_base64 = self.frame
                    self.page.update()
                else:
                    print("Error al capturar el video")
                time.sleep(0.03)

    def exit_click(self, e):
        self.page.go("/Navegacion")