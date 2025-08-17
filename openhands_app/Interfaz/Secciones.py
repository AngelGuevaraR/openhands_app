import flet as ft
from Login.BDUsuarios import ContactManager

class Navegacion:
    def __init__(self, page):
        self.page = page
        self.data = ContactManager()

        self.page.spacing = 5
        self.page.padding = 5
        self.page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.Colors.BLACK), font_family="Poppins")

        self.problema = ft.TextField(label="Problema:", border_color="black", width=280, height=40, hint_text="Error en la interfaz",  color = ft.Colors.BLACK, prefix_icon = ft.Icons.ERROR)

        self.card1 = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="assets/LSMAprendizaje.png", width=220, border_radius=5),
                                ft.Text("Aprendizaje", weight=ft.FontWeight.BOLD, size=18),
                                ft.Text(
                                    "Aprendizaje del abecedario LSM",
                                    size=12,
                                    color=ft.Colors.GREY,
                                ),
                                ft.ElevatedButton("¡Vamos!", bgcolor= ft.Colors.BLUE_200, color= ft.Colors.BLACK, on_click=lambda _: self.page.go("/Reconocimiento")),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=20,
                        width= 300,
                    ),
                    elevation=2,
        )

        self.card2 = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Sección en construcción...", weight=ft.FontWeight.BOLD, size=16),
                            ft.Text(
                                "Proximamente...",
                                size=12,
                                color=ft.Colors.GREY,
                            )
                        ],
                        spacing=5,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=20,
                    width=300
                ),
                elevation=2,
            )

        self.seleccion = ft.Container(
            shape=ft.BoxShape.CIRCLE,
            offset= ft.Offset(-0.38, 0),
            bgcolor= ft.Colors.BLUE_300, alignment=ft.alignment.center,
            margin=ft.margin.only(top=10),
            height=40,
            content=ft.Icon(ft.Icons.HOME_FILLED, color = ft.Colors.BLACK) 
        )

        self.nav = ft.Container(
            bgcolor= ft.Colors.WHITE60, alignment=ft.alignment.center,
            border_radius=10,
            padding=0,
            height=50,
            margin=ft.margin.only(top=5),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                ft.IconButton(icon=ft.Icons.HOME_FILLED, data= "1", icon_color= ft.Colors.BLACK, on_click=self.cambiopos, tooltip="Inicio"),
                ft.IconButton(icon=ft.Icons.NOTIFICATIONS, data= "2", icon_color= ft.Colors.BLACK, on_click=self.cambiopos, tooltip="Notificaciones"),
                ft.IconButton(icon=ft.Icons.BUG_REPORT, data= "3", icon_color= ft.Colors.BLACK, on_click=self.cambiopos, tooltip="Reportes"),
                ft.IconButton(icon=ft.Icons.EXIT_TO_APP, icon_color= ft.Colors.BLACK, on_click=lambda _: self.page.go("/Inicio"), tooltip="Salir")
            ],
            ),
        )

        self.contenedor1 = ft.Container(expand= True,
            padding=10,
            offset= ft.Offset(0,0),
            content=
                ft.Column(
                    expand=True,
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
                            ft.IconButton(icon=ft.Icons.PERSON, icon_color="black", tooltip="Perfil")
                        ]
                    ),
                        ft.Text(
                            "¡Hola, Bienvenido!",
                            size=20,
                            text_align="left",
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK
                        ),
                        ft.Text(
                            "¿Qué te gustaría hacer hoy?",
                            width=330,
                            size=22,
                            text_align=ft.TextAlign.LEFT,
                            weight="bold",
                            color=ft.Colors.BLACK
                        ),
                        ft.TextField(
                            prefix_icon=ft.Icons.SEARCH,
                            hint_text="Buscar sección",
                            border_radius=20,
                            bgcolor=ft.Colors.GREY_300,
                            border_color="transparent",
                            on_change=self.filter_nav,
                        ),
                        ft.Text(
                            "Nuestras secciones: ",
                            text_align=ft.TextAlign.LEFT,
                            size=18,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Container(
                            self.card1
                        ),
                        ft.Container(
                            self.card2
                        )
                        
                ],
            ),
        )
            
        self.contenedor2 = ft.Container(offset=ft.Offset(-2,0),
                                        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                                            ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Container(
                                                    ft.Image(
                                                        src="openhands_app/assets/logo.png",
                                                        height=50
                                                        )
                                                ),
                                                ft.IconButton(icon=ft.Icons.PERSON, icon_color="black", tooltip="Perfil")
                                            ]
                                        ),
                                            ft.Text("Notificaciones", size=40, weight=ft.FontWeight.BOLD), 
                                            ft.Container(alignment=ft.alignment.center,content=ft.Card(content=ft.Container(content= ft.Column([
                                                 ft.Text("Notificación: ", weight=ft.FontWeight.BOLD, size=18),
                                                 ft.Text(
                                                      "Sigue Aprendiendo...",
                                                      size=12,
                                                      color=ft.Colors.GREY,
                                                 ),
                                                 ft.ElevatedButton("Ir", bgcolor=ft.Colors.BLUE_200, color=ft.Colors.BLACK, on_click=lambda _: self.page.go("/Reconocimiento"))
                                            ],
                                            spacing=5,
                                            alignment= ft.MainAxisAlignment.START
                                            ),
                                            padding=20,
                                            width=300
                                            ),
                                            elevation=2
                                            )
                                            ),
                                            ft.Container(alignment=ft.alignment.center,content=ft.Card(content=ft.Container(content= ft.Column([
                                                 ft.Text("Notificación 2: ", weight=ft.FontWeight.BOLD, size=18),
                                                 ft.Text(
                                                      "Explora nuestras secciones...",
                                                      size=12,
                                                      color=ft.Colors.GREY,
                                                 ),
                                            ],
                                            spacing=5,
                                            alignment= ft.MainAxisAlignment.START
                                            ),
                                            padding=20,
                                            width=300
                                            ),
                                            elevation=2
                                            )
                                            )
                                        ]
                                    )
                                )
        

        self.contenedor3 = ft.Container(offset=ft.Offset(-2,0),
                                        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                                                ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    ft.Container(
                                                        ft.Image(
                                                            src="openhands_app/assets/logo.png",
                                                            height=50
                                                            )
                                                    ),
                                                    ft.IconButton(icon=ft.Icons.PERSON, icon_color="black", tooltip="Perfil")
                                                ]
                    ),
                    ft.Text("Soporte", size=40, weight= ft.FontWeight.BOLD), 
                    ft.Container(alignment=ft.alignment.center,
                                 content=ft.Image(src="assets/logo.png", fit=ft.ImageFit.CONTAIN, width=210)),
                    ft.Text("Explicanos tu problemática brevemente", text_align= ft.TextAlign.CENTER, size= 18),
                    ft.Container(self.problema),
                    ft.ElevatedButton("Enviar reporte", bgcolor=ft.Colors.BLUE_200, color=ft.Colors.BLACK, on_click=self.add_reporte),
                    ft.Text("Otros medios donde puedes contactarnos:", size=15, weight= ft.FontWeight.BOLD),
                    ft.Text("Correo eléctronico: soporte@openhands.com"),
                    ft.Text("Teléfono de soporte: 2225660284")
                                 ]))
                                 
        self.contenedor4 = ft.Container(offset=ft.Offset(-2,0),
                                        content= self.page.go("/Inicio"))
     
    
    def interfazsec(self):
        return ft.Container(
            ft.Column(expand= True, controls=[ft.Stack(
                controls= [
                    self.contenedor1,
                    self.contenedor2,
                    self.contenedor3,
                ]
            ),
                ft.Stack(
                    height=60,
                    controls=[
                        self.nav,
                        self.seleccion
                    ]
                ),

            ]),
            border_radius=20,
            width=350,
            height=800,
            bgcolor= ft.Colors.WHITE,
        )


    def filter_nav(self, e):
        pass

    def cambiopos(self, e):
        if e.control.data == "1":
            self.seleccion.offset = ft.Offset(-0.38, 0)
            self.seleccion.content = ft.Icon(name=ft.Icons.HOME_FILLED, color=ft.Colors.BLACK, tooltip="Inicio")
            self.contenedor1.offset = ft.Offset(0,0)
            self.contenedor2.offset = ft.Offset(-2,0)
            self.contenedor3.offset = ft.Offset(-2,0)
            self.contenedor4.offset = ft.Offset(-2,0)
        if e.control.data == "2":
            self.seleccion.offset = ft.Offset(-0.12, 0)
            self.seleccion.content = ft.Icon(name=ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK, tooltip="Notificaciones")
            self.contenedor1.offset = ft.Offset(-2,0)
            self.contenedor2.offset = ft.Offset(0,0)
            self.contenedor3.offset = ft.Offset(-2,0)
            self.contenedor4.offset = ft.Offset(-2,0)
        if e.control.data == "3":
            self.seleccion.offset = ft.Offset(0.12, 0)
            self.seleccion.content = ft.Icon(name=ft.Icons.BUG_REPORT, color=ft.Colors.BLACK, tooltip="Reportes")
            self.contenedor1.offset = ft.Offset(-2,0)
            self.contenedor2.offset = ft.Offset(-2,0)
            self.contenedor3.offset = ft.Offset(0,0)
            self.contenedor4.offset = ft.Offset(-2,0)
        if e.control.data == "4":
            self.seleccion.offset = ft.Offset(0.38, 0)
            self.seleccion.content = ft.Icon(name=ft.Icons.EXIT_TO_APP, color=ft.Colors.BLACK, tooltip="Salir")
            self.contenedor1.offset = ft.Offset(-2,0)
            self.contenedor2.offset = ft.Offset(-2,0)
            self.contenedor3.offset = ft.Offset(-2,0)
            self.contenedor4.offset = ft.Offset(0,0)
        
        self.page.update()

    def add_reporte(self, e):
        reporte = self.problema.value

        if reporte:
                self.data.add_reporte(reporte)
                snack_bar = ft.SnackBar(content=ft.Text("Reporte enviado"),
                bgcolor= ft.Colors.GREEN
                )
                self.page.overlay.append(snack_bar) 
                snack_bar.open = True
        else:
                snack_bar = ft.SnackBar(content=ft.Text("Hubo un error, contactate con nuestro equipo"),
                bgcolor= ft.Colors.RED
                )
                self.page.overlay.append(snack_bar) 
                snack_bar.open = True
        
        self.page.update()