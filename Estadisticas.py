from Jugador import Jugador

class Estadistica(Jugador):
    def __init__(self, username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo, tiempo_final, status):
        super().__init__(username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo)
        self.tiempo_final = tiempo_final
        self.status = status

    def mostrar_estadistica(self):
        print(f'Nombre de Usuario: {self.username}\nEdad: {self.edad}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nNivel de Difiultad: {self.dificultad}\nVidas: {self.vidas}\nPistas:{self.pistas}\nTiempo final: {self.tiempo_final}\nEstado: {self.status}')