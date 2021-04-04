class Jugador:

    def __init__(self, username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo):
        self.username = username
        self.contraseña = contraseña
        self.edad = edad
        self.avatar = avatar
        self.inventario = inventario
        self.dificultad = dificultad
        self.vidas = vidas
        self.pistas = pistas
        self.tiempo = tiempo
        

    def mostrar_jugador(self):
        print(f'Nombre de Usuario: {self.username}\nContraseña: {self.contraseña}\nEdad: {self.edad}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nNivel de Difiultad: {self.dificultad}\nVidas: {self.vidas}\nPistas:{self.pistas}\nTiempo: {self.tiempo}')
        
    def mostrar_nombre_de_usuario(self):
        print(f'Nombre de Usuario: {self.username}')

# class Estadistica(Jugador):
    
#     def __init__(self, username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo,  tiempo_final, status):
#         Jugador.__init__(self, username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo)
#         self.tiempo_final = tiempo_final
#         self.status = status

#     def mostrar_estadistica(self):
#         print(f'Nombre de Usuario: {self.username}\nEdad: {self.edad}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nNivel de Difiultad: {self.dificultad}\nVidas: {self.vidas}\nPistas:{self.pistas}\nTiempo final: {self.tiempo_final}\nEstado: {self.status}')


