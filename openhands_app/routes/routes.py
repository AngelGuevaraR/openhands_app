import flet as ft

from Login.login import Inicio
from Login.registro import Registro
from Interfaz.Secciones import Navegacion
from Interfaz.Aprendizaje import Abecedario


class Router:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/Inicio": Inicio(page).interfaz(),
            "/Registro": Registro(page).interfaz(),
            "/Navegacion": Navegacion(page).interfazsec(),
            "/Reconocimiento": Abecedario(page).interfazAprendizaje(),

        }
        self.body = ft.Container(content=self.routes["/Inicio"])

    def cambio_ruta(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()