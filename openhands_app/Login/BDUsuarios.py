import sqlite3

class ContactManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("openhands_app/data.db", check_same_thread = False)

    def add_usuario(self, email, nombre, password, nac):
        query = " INSERT INTO datos (EMAIL, USUARIO, PASSWORD, NAC)  VALUES (?,?,?,?)"

        self.connection.execute(query, (email, nombre, password, nac))
        self.connection.commit()

    def add_reporte(self, reporte):
        query = "INSERT INTO reportes (descrip) VALUES (?)"

        self.connection.execute(query, (reporte,))
        self.connection.commit()

    def get_usuario(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM datos"
        cursor.execute(query)
        contacts = cursor.fetchall()
        return contacts
    
    def get_usuario_credenciales(self, emailuser, password):
        cursor = self.connection.cursor()
        query = "SELECT * FROM datos WHERE (EMAIL =? OR USUARIO =?) AND PASSWORD =?"
        cursor.execute(query, (emailuser, emailuser, password))
        usuario = cursor.fetchone()  
        cursor.close()  
        return usuario
    
    def eliminar_usuario(self,name):
        query = "DELETE FROM datos WHERE nombre =?"
        self.connection.execute(query(name, ))
        self.connection.commit()

    def update_contact(self, contact_id, email, nombre, password, nac):
        query = "UPDATE datos SET EMAIL =?, NOMBRE =?, PASSWORD=?, NAC=? WHERE ID=?"
        self.connection.execute(query, (email, nombre, password, nac, contact_id))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

x = ContactManager()
#x.add_usuario("ejemplo123@correo.com", "Angelgr", "123", "02/09/05")
#print(x.get_usuario())
#print(x.get_usuario_credenciales("Angelgr", "123"))