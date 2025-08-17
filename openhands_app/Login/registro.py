import flet as ft

from Login.BDUsuarios import ContactManager

class Registro:
    def __init__(self, page):
        self.data = ContactManager()

        self.page = page

        self.Email = ft.TextField(label="Correo electrónico", keyboard_type= ft.KeyboardType.EMAIL, border_color="black", width=280, height=40, hint_text="ejemplo@correo.com", color = ft.Colors.BLACK, prefix_icon = ft.Icons.EMAIL)

        self.Usuario = ft.TextField(label="Usuario", border_color="black", width=280, height=40, hint_text="ejemplo123", color= ft.Colors.BLACK, prefix_icon= ft.Icons.SUPERVISED_USER_CIRCLE)

        self.Contraseña = ft.TextField(label="Contraseña", border_color="black", width=280,
                height=40,
                keyboard_type= ft.KeyboardType.VISIBLE_PASSWORD,
                hint_text="******",
                color=ft.Colors.BLACK,
                prefix_icon = ft.Icons.LOCK,
                password=True)
        
        self.FechaNacimiento = ft.TextField(label="Fecha de nacimiento", border_color="black", width=280, height=40, hint_text= "02/09/2005", color=ft.Colors.BLACK, prefix_icon=ft.Icons.DATE_RANGE)
        
    
    def add_user(self, e):
        email = self.Email.value.lower()
        user = self.Usuario.value.lower()
        password = self.Contraseña.value.lower()
        nac = self.FechaNacimiento.value.lower()

        if not all([email, user, password, nac]):
            snack_bar = ft.SnackBar(content=ft.Text("Por favor, completa todos los campos"),
            bgcolor = ft.Colors.RED
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            return
        
        try:
            contact_exists = any(
                (row[1]== email or row[2] == user) for row in self.data.get_usuario()
            )
            if contact_exists:
                snack_bar = ft.SnackBar(content=ft.Text("El usuario o correo ya están registrados"),
                bgcolor= ft.Colors.RED
                )
                self.page.overlay.append(snack_bar) 
                snack_bar.open = True
            else:
                self.data.add_usuario(email, user, password, nac)
                self.clean_fields()

                snack_bar = ft.SnackBar(content=ft.Text("Usuario registrado con éxito"),
                bgcolor= ft.Colors.GREEN
                )
                self.page.overlay.append(snack_bar) 
                snack_bar.open = True
                
                self.page.go("/Inicio")

        except Exception as error:
            snack_bar = ft.SnackBar(content=ft.Text("ERROR al registrar al usuario: {str(error)}"),
                                    bgcolor=ft.Colors.RED)
            self.page.overlay.append(snack_bar)  
            snack_bar.open = True
        
        self.page.update()

    def clean_fields(self):
        self.Email.value = ""
        self.Usuario.value = ""
        self.Contraseña.value = ""
        self.FechaNacimiento.value = ""

    def interfaz(self):
        return ft.Container(
    ft.Column(
        [
        ft.Container(
            ft.Image(
            src= "assets/logo.png",
            width = 60,
            height= 60
        ),
            padding= ft.padding.only(bottom=20, top=-20)
        ),
        ft.Container(
            ft.Text("Registro",
                    width=320,
                    size=30,
                    text_align="center",
                    weight = "w900",
                    color= ft.Colors.BLACK
                    ),
                    padding=ft.padding.symmetric(vertical=-25, horizontal=50)
        ),
        ft.Container(
            self.Email,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            self.Usuario,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            self.Contraseña,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            self.FechaNacimiento,
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="Registrarte",
                width=280,
                bgcolor="blue",
                color= ft.Colors.BLACK,
                on_click=self.add_user
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.Text("¿Ya tienes cuenta?"),
                ft.TextButton("Inicio de sesión", on_click=lambda _: self.page.go('/Inicio'))
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
        ),
    ],
    alignment= ft.MainAxisAlignment.SPACE_EVENLY
    ),

    border_radius=20,
    width=320,
    height=600,
    gradient= ft.LinearGradient([
        ft.Colors.BLUE_100,
        ft.Colors.WHITE
    ]),
)
    
