import flet as ft
from Login.BDUsuarios import ContactManager 

class Inicio:
    def __init__(self, page):
        self.data = ContactManager()
        self.page = page
        self.EmailUsuario = ft.TextField(label="Correo o Usuario", border_color="black", width=280, height=40, hint_text="ejemplo@correo.com",  color = ft.Colors.BLACK, prefix_icon = ft.Icons.EMAIL)

        
        self.Contraseña = ft.TextField(label="Contraseña", border_color="black", width=280,
                height=40,
                hint_text="******",
                color=ft.Colors.BLACK,
                prefix_icon = ft.Icons.LOCK,
                password=True)
        
    def interfaz(self):
        return ft.Container(
    ft.Column(
        [
        ft.Container(
            ft.Image(
            src= "openhands_app/assets/logo.png",
            width = 250,
            height= 250
        ),
            padding= ft.padding.symmetric(vertical=-15, horizontal=40)
        ),
        ft.Container(
            ft.Text("Iniciar Sesión",
                    width=390,
                    size=30,
                    text_align="center",
                    weight = "w800",
                    color= ft.Colors.BLACK
                    ),
                    padding=ft.padding.symmetric(vertical=-25, horizontal=50)
        ),
        ft.Container(
            self.EmailUsuario,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            self.Contraseña,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="Iniciar sesión",
                width=280,
                bgcolor="blue",
                color= ft.Colors.BLACK,
                on_click=self.verif_user
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.Text("¿No tienes cuenta?"),
                ft.TextButton("Crear cuenta", on_click=lambda _: self.page.go('/Registro'))
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
        ),
    ],
    alignment= ft.MainAxisAlignment.SPACE_AROUND
    ),

    border_radius=20,
    width=320,
    height=600,
    gradient= ft.LinearGradient([
        ft.Colors.BLUE_100,
        ft.Colors.WHITE
    ]),
)

    
    def verif_user(self, _):
        emailUser = self.EmailUsuario.value.lower()
        password = self.Contraseña.value.lower()

        self.page.session.set("1", self.EmailUsuario.value)

        if len(emailUser) > 0 and len(password) > 0:
            usuario = self.data.get_usuario_credenciales(emailUser, password)

            if usuario:
                snack_bar = ft.SnackBar(content=ft.Text(f"Bienvenido {emailUser}"))
                self.page.overlay.append(snack_bar)
                snack_bar.open = True
                self.page.go("/Navegacion")
            else:
                self.clean_fields()
                snack_bar = ft.SnackBar(content=ft.Text("El usuario no existe"))
                self.page.overlay.append(snack_bar)  
                snack_bar.open = True

            self.page.update()
    

    def clean_fields(self):
        self.EmailUsuario.value = ""
        self.Contraseña.value = ""
