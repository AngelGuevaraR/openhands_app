import flet as ft
from routes.routes import Router

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Rutas
    myRouter = Router(page, ft)
    page.on_route_change = myRouter.cambio_ruta

    page.add(
        myRouter.body
    )
    page.go("/Inicio")


ft.app(target=main, assets_dir="assets")