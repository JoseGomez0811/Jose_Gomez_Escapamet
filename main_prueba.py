from Jugador import Jugador
from Estadisticas import Estadistica
import random
import  time
import pygame, sys
from pygame import mixer
from sympy import Symbol, diff, cos, tan, sin
import threading
from termcolor import colored
from colored import fg, bg, attr

#---MÚSICA DE FONDO---
def musica():
    # Se inicializa el mixer
    mixer.init()
    # Se carga la canción
    mixer.music.load("musica-de-misterio-terror-horror-sin-no-copyright-para-leer-libros-y-cuentos-y-relatos-de-terror.mp3")
    # Se ajusta el volumen
    mixer.music.set_volume(0.7)
    # Empieza a sonar la canción
    mixer.music.play()

#---CRONOMETRO DEL JUEGO---
def cronometro_1(user):
    # Se iniciliza pygame
    pygame.init()
    # Se crea la ventana principal
    ventana = pygame.display.set_mode((400,300))
    pygame.display.set_caption('Hola')
    # Se ajusta el estilo de la fuente
    fuente = pygame.font.SysFont('Arial', 30)
    # Código para medir el tiempo
    aux = 1
    while True:
        ventana.fill((255,255,255))
        tiempo = pygame.time.get_ticks()/1000
        if aux == tiempo:
            aux += 1 
            print(tiempo)
    
        if tiempo == user.tiempo:
            break

        for evento in pygame.event.get():
            if evento.type == quit:
                pygame.quit()
                sys.exit()
    
        contador = fuente.render('Tiempo: ' + str(tiempo),0,(120,70,0))
        ventana.blit(contador,(100,100))
        pygame.display.update()

    sys.exit()

#---ESTADÍSTICA DE LOS JUGARES---
def ver_estadisticas():
    usuarios = []
    # Se abre el archivo txt par apoder visualizar las estadísticas de cada jugador 
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    if len(datos) == 0:
        print('\nTodavía no hay ningún usuario registrado.\n')
    else:
        for dato in datos:
            user = dato[:-1].split('-')
            print(user)


#---JUEGO DE 21 BLACKJACK (FINAL BOSS)---
def TurnoCartas():
    # Se asignando las cartas que se usaran en el juego
    cartas = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

    total = 0
    eleccion = 1
    n = 1
    mesa = []

    while eleccion != 0 and total < 20:
        numero = 0
        numerosnaturales = [2,3,4,5,6,7,8,9,10]

        # Se escoge la carta que se repartira aleatoriamente
        print('\n')
        print(f'Carta # {n}: ')
        time.sleep(2)
        numero = random.choice(cartas)
        print (f'["{numero}"]')

        # Se valida el valor que tendrá la carta A
        if numero == "A":
            mesa.append(numero)
            print('Que valor quieres que tenga tu "A", 1 u 11?')
            numero = input('Escoja un valor: ')
            if numero != 1 and numero != 11:
                print ('PERDISTE POR TRAMPOSO!')
                vida = user.vidas
                vida -= 0.25
                user.vidas = vida
                print(user.vidas)
                return 0
                break
        
        # Se validan los valores que tendrán las cartas J, Q, K
        elif numero == 'J':
            mesa.append(numero)
            numero = 10
        elif numero == 'Q':
            mesa.append(numero)
            numero = 10
        elif numero == 'K':
            mesa.append(numero)
            numero = 10

        else:
            mesa.append(numero)

        total += numero
        time.sleep(2)
        if n > 1:
            print(f'Total: {total}')
            print('\n')

        # Menú de opciones que tendrá el jugador
        if total < 20:
            #mesa.append(numero)
            respuesta = 2
            while respuesta == 2:
                print(colored('''
                ------------------------------
                1: Pedir una carta
                ------------------------------
                2: Mirar tus cartas
                ------------------------------
                3: Plantarse
                ------------------------------
                ''', 'green'))
                # print('1: Pedir una carta\n2: Mirar tus cartas\n3: Plantarse')
                respuesta = int(input('--> '))
                while respuesta != 1 and respuesta != 2 and respuesta != 3:
                    print(colored('''
                    ------------------------------
                    1: Pedir una carta
                    ------------------------------
                    2: Mirar tus cartas
                    ------------------------------
                    3: Plantarse
                    ------------------------------
                    ''', 'green'))
                    # print('1: Pedir una carta\n2: Mirar tus cartas\n3: Plantarse')
                    respuesta = int(input('--> '))

                if respuesta == 1 :
                    n += 1
                elif respuesta == 2:
                    print (f'Cartas: {mesa}')
                    print('\n')
                    time.sleep(2)
                else:
                    eleccion = 0
                    return total

        # Se valida el resultado final de las cartas del juegador
        elif total == 21 :
            mesa.append(numero)
            print("FELICIDADES, has hecho un BLACKJACK!")
            time.sleep(4)
            print('¡Felicidades! Has logrado evitar una catástrofe en la Unimet')
            sys.exit()
            break
            return total
        elif total == 21:
            mesa.append(numero)
            print('FELICIDADES, has ganado la partida')
            time.sleep(4)
            print('¡Felicidades! Has logrado evitar una catástrofe en la Unimet')
            sys.exit()
            break
            return total
        else:
            print ("QUE MALA SUERTE! HAS PERDIDO! ")
            vida = user.vidas
            vida -= 0.25
            user.vidas = vida
            print(user.vidas)
            return 0

    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)

def jugar_blackjack():
    intentos = 0
    
    # Validar que el jugador aún tenga vidas disponibles
    if user.vidas > 0:
        while True:
            if intentos < 5:
                print ('JUEGO DE BLACK JACK')
                
                print ('Buenas, Jugadores, Vamos a empezar la Partida de BlackJack')
                time.sleep(2)
                print ('Inicia el Jugador numero 1')
                time.sleep(1)
                Jugador1 = TurnoCartas()
                print (f'Total del Jugador = {Jugador1}')
                print('\n')
                time.sleep(2)
                print('\n')
                continuar = input('Quieres Jugar Otra Vez? [S/N]: ').upper()
                print('\n')
                if continuar == 'N':
                    break
                else:
                    intentos += 1
            else:
                print('Ya no tienes más intentos')
                break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')


    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)

#---JUEGO DE ESCOGE UN NÚMERO ENTRE---
def numero():
    aleatorio = random.randint(1,15)
    return aleatorio

def jugar_numero(user):
    numero_aleatorio = numero()
    print(numero_aleatorio)
    intentos = 0

    contador_pistas = 0

    if user.vidas > 0:
        while True:
            print('Escoge un número entre 1 y 15')
            numeros = input('Escoge un número: ')
            while not numeros.isnumeric():
                numeros = input('Escoge un número: ')
                
            if intentos < 2:
                if int(numero_aleatorio) < int(numeros):
                    print('Estas por arriba')
                    intentos += 1

                elif int(numero_aleatorio) > int(numeros):
                    print('Estas por abajo')
                    intentos += 1

                elif int(numero_aleatorio) == int(numeros):
                    print('¡Ganaste! Ese era el número')
                    inventario = user.inventario
                    inventario.append('título Universitario')
                    user.inventario = inventario
                    print(user.inventario)
                    break
            else:
                print(f'¡Perdiste! El número era {numero_aleatorio}')
                vida = user.vidas
                vida -= 0.25
                user.vidas = vida
                print(user.vidas)
                break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE PALABRAS MEZCLADAS---
def aleatorio(palabras_cocina, palabras_baile, palabras_baño):
    categoria_aleatoria = random.choice((palabras_cocina, palabras_baile, palabras_baño))
    return categoria_aleatoria

def jugar_mezcladas(user, palabras_cocina, palabras_baile, palabras_baño):
    categorias_aleatorias = aleatorio(palabras_cocina, palabras_baile, palabras_baño) 
    
    for palabra in categorias_aleatorias:
        inversa = random.sample(palabra, len(palabra))
        print(inversa)
    
    intentos = 0
    respuesta_1 = ''
    respuesta_2 = ''
    respuesta_3 = ''
    respuesta_4 = ''
    respuesta_5 = ''

    if user.vidas > 0:
        while True:
            respuesta_1 = input('Reescriba la primera palabra: ').lower()
            respuesta_2 = input('Reescriba la segunda palabra: ').lower()
            respuesta_3 = input('Reescriba la tercera palabra: ').lower()
            respuesta_4 = input('Reescriba la cuarta palabra: ').lower()
            respuesta_5 = input('Reescriba la quinta palabra: ').lower()


            if intentos < 2:
                if categorias_aleatorias == palabras_cocina:
                    if respuesta_1 == 'sarten' and respuesta_2 == 'paleta' and respuesta_3 == 'olla' and respuesta_4 == 'vaso' and respuesta_5 == 'hornilla':
                        print('¡CORRECTO! Esas son las palabras')
                        inventario = user.inventario
                        inventario.append('contraseña')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                    else:
                        print('Una o varios palabras no son correctas')
                        intentos += 1
                        vida = user.vidas
                        vida -= 0.50
                        user.vidas = vida
                        print(user.vidas)

                elif categorias_aleatorias == palabras_baño:
                    if respuesta_1 == 'poceta' and respuesta_2 == 'cepillo' and respuesta_3 == 'afeitadora' and respuesta_4 == 'regadera' and respuesta_5 == 'grifo':
                        print('¡CORRECTO! Esas son las palabras')
                        inventario = user.inventario
                        inventario.append('contraseña')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                    else:
                        print('Una o varios palabras no son correctas')
                        intentos += 1
                        vida = user.vidas
                        vida -= 0.50
                        user.vidas = vida
                        print(user.vidas)

                elif categorias_aleatorias == palabras_baile:
                    if respuesta_1 == 'zumba' and respuesta_2 == 'salsa' and respuesta_3 == 'flamengo' and respuesta_4 == 'tango' and respuesta_5 == 'perreo':
                        print('¡CORRECTO! Esas son las palabras')
                        inventario = user.inventario
                        inventario.append('contraseña')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                    else:
                        print('Una o varios palabras no son correctas')
                        intentos += 1
                        vida = user.vidas
                        vida -= 0.50
                        user.vidas = vida
                        print(user.vidas)
            else:
                print('Ya no tienes más intentos')
                break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE ADIVINANZAS---
def adivinanza(adivinanzas):
    aleatorio = random.choice(adivinanzas)
    return aleatorio

def jugar_adivinanzas(user, adivinanzas):
    adivinanza_aleatoria = adivinanza(adivinanzas)
    print(adivinanza_aleatoria)
    intentos = 0

    contador_pistas = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            print('Si deseas usar una pista presiona "*"')
            respuesta = input('Ingrese su respuesta: ').lower()
            # Opción de pedir un pista
            pista = user.pistas

            if respuesta == '*':
                if user.pistas > 0:
                    contador_pistas += 1
                    if adivinanza_aleatoria == adivinanzas[0]:
                        if contador_pistas == 1:
                            print('lo usas cuando se va la luz')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('lo puedes prender con un encendedor')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('es de cera')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                    elif adivinanza_aleatoria == adivinanzas[1]:
                        if contador_pistas == 1:
                            print('lo usas cuando hay luz')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('gracias a estar encendido puedes leer')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('se coloca en las lámparas')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')
                        
                    elif adivinanza_aleatoria == adivinanzas[2]:
                        if contador_pistas == 1:
                            print('fruta')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('POTASIO')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('parecido al cambur')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')
                else:
                    print('Se te acabaron las pistas')
            
                user.pistas = pista
            # Asociando las preguntas con sus respectivas respuestas
            # Buscar como sacar el print del bucle for
            elif adivinanza_aleatoria == adivinanzas[0]:
                respuesta_1 = ['vela', 'la vela', 'una vela']
                for i in respuesta_1:
                    
                    if i == respuesta:
                        print('La respuesta es correcta')
                        inventario = user.inventario
                        inventario.append('llave')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                    else:
                        intentos += 1
                        print('La respuesta es incorrecta')
                        vida = user.vidas
                        vida -= 0.5
                        user.vidas = vida
                        print(user.vidas)
                        if intentos == 3:
                            print('¡Perdiste!')
                            break
            elif adivinanza_aleatoria == adivinanzas[1]:
                respuesta_2 = ['un bombillo', 'bombillo', 'el bombillo']
                for i in respuesta_2:
                                
                    if i == respuesta:
                        print('La respuesta es correcta')
                        inventario = user.inventario
                        inventario.append('llave')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                                            
                    else:
                        intentos += 1
                        print('La respuesta es incorrecta')
                        vida = user.vidas
                        vida -= 0.5
                        user.vidas = vida
                        print(user.vidas)
                        if intentos == 3:
                            print('¡Perdiste!')
                            break
            else:
                respuesta_3 = ['un plátano', 'plátano','el plátano']
                for i in respuesta_3:
                    
                    if i == respuesta:
                        print('La respuesta es correcta')
                        inventario = user.inventario
                        inventario.append('llave')
                        user.inventario = inventario
                        print(user.inventario)
                        break
                    else:
                        intentos += 1
                        print('La respuesta es incorrecta')
                        vida = user.vidas
                        vida -= 0.5
                        user.vidas = vida
                        print(user.vidas)
                        if intentos == 3:
                            print('¡Perdiste!')
                            break
            break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE PREGUNTAS SOBRE PYTHON---
def pregunta_python(preguntas_python):
    aleatorio = random.choice(preguntas_python)
    return aleatorio

def jugar_python(user, preguntas_python):
    pregunta_aleatoria = pregunta_python(preguntas_python)
    print(pregunta_aleatoria)
    intentos = 0

    contador_pistas = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            print('Si deseas usar una pista presiona "*"')
            respuesta = input('Ingrese su respuesta: ')
            # Opción de pedir un pista
            pista = user.pistas

            if respuesta == '*':
                if user.pistas > 0:
                    contador_pistas += 1
                    if pregunta_aleatoria == preguntas_python[0]:
                        if contador_pistas == 1:
                            print('utiliza replace')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('utiliza split')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('utiliza int')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                    elif pregunta_aleatoria == preguntas_python[1]:
                        if contador_pistas == 1:
                            print('utiliza slices')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')
                        
                else:
                    print('Se te acabaron las pistas')
            
                user.pistas = pista
            # Asociando las preguntas con sus respectivas respuestas
            elif pregunta_aleatoria == preguntas_python[0]:
                frase = preguntas_python[0].split(' ')
                for n in frase:
                    if n == '50,00':
                        numero = n
                        decimal = numero.replace(',','.')
                        decimal = float(decimal)
                        print(type(decimal))
                respuesta_1 = decimal
                if respuesta_1 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('carnet')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                respuesta_2 = ' '.join(list(map(lambda x: x[::-1], preguntas_python[1].split())))
                if respuesta_2 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('carnet')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE SOPA DE LETRAS---
def matriz_aleatoria(matriz_1, matriz_2, matriz_3):
    aleatorio = random.choice((matriz_1, matriz_2, matriz_3))
    return aleatorio

def jugar_sopa(user, matriz_1, matriz_2, matriz_3):
    intentos = 0
    palabras = []
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    contador_pistas = 0

    matrices_aleatorias = matriz_aleatoria(matriz_1, matriz_2, matriz_3)
    
    if user.vidas > 0:
        while True:
            pista = user.pistas

            print(matrices_aleatorias)

            decision_pista = input('¿Deseas pedir una pista? [S/N]: ').upper()
            while decision_pista != 'S' and decision_pista != 'N':
                decision_pista = input('¿Deseas pedir una pista? [S/N]: ').upper()

            if decision_pista == 'S':
                if user.pistas > 0:
                    contador_pistas += 1
                    if matrices_aleatorias == matriz_1:
                        if contador_pistas == 1:
                            print('Una de las palabras es el apellido de la directora de escuela de sistemas')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('Una de las palabras es el apellido del director del CETIC')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Una de las palabras es el apellido del rector de la UNIMET')
                        else:
                            print('Ya no hay mas pistas')
                    elif matrices_aleatorias == matriz_2:
                        if contador_pistas == 1:
                            print('Una de las palabras es el apellido del profesor Luis')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('Una de las palabras es el apellido del profesor Alejandro')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Una de las palabras es el apellido del presidente de la UNIMET')
                        else:
                            print('Ya no hay mas pistas')
                    elif matrices_aleatorias == matriz_3:
                        if contador_pistas == 1:
                            print('Una de las palabras es el apellido del coronel de seguridad de la UNIMET')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('Una de las palabras es el apellido del presidente de la FCE-UNIMET')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Una de las palabras es el apellido de la vicerrectora académica de la UNIMET')
                        else:
                            print('Ya no hay mas pistas')
                user.pistas = pista
            else:
                print('\n')
                print('Hay 3 palabras en la sopa de letras')
                x1 = int(input('Ingrese la coordenada en x de la primera letra: '))
                y1 = int(input('Ingrese la coordenada en y de la primera letra: '))
                x2 = int(input('Ingrese la coordenada en x de la última letra: '))
                y2 = int(input('Ingrese la coordenada en y de la última letra: '))

                

                if len(palabras) < 2:
                    if intentos < 2:
                        if matrices_aleatorias == matriz_1:
                            if x1 == 1  and y1 == 1 and x2 == 1 and y2 == 5:
                                print('¡CORRECTO! La palabra es PILAR')
                                palabras.append('PILAR')
                            elif x1 == 5 and y1 == 0 and x2 == 5 and y2 == 9:
                                print('¡CORRECTO! La palabra es SCHARIFKER')
                                palabras.append('SCHARIFKER')
                            elif x1 == 6 and y1 == 13 and x2 == 1 and y2 == 8:
                                print('¡CORRECTO! La palabra es ARDILA')
                                palabras.append('ARDILA')
                            else:
                                print('La palabra que ingresó no es correcta')
                                intentos += 1
                                vida = user.vidas
                                vida -= 0.5
                                user.vidas = vida
                                print(user.vidas)
                    
                        elif matrices_aleatorias == matriz_2:
                            if x1 == 6  and y1 == 13 and x2 == 2 and y2 == 9:
                                print('¡CORRECTO! La palabra es BELLO')
                                palabras.append('BELLO')
                            elif x1 == 7 and y1 == 6 and x2 == 13 and y2 == 0:
                                print('¡CORRECTO! La palabra es MARCANO')
                                palabras.append('MARCANO')
                            elif x1 == 9 and y1 == 3 and x2 == 4 and y2 == 8:
                                print('¡CORRECTO! La palabra es DA GAMA')
                                palabras.append('DA GAMA')
                            else:
                                print('La palabra que ingresó no es correcta')
                                intentos += 1
                                vida = user.vidas
                                vida -= 0.5
                                user.vidas = vida
                                print(user.vidas)

                        elif matrices_aleatorias == matriz_3:
                            if x1 == 2  and y1 == 5 and x2 == 6 and y2 == 5:
                                print('¡CORRECTO! La palabra es BOADA')
                                palabras.append('BOADA')
                            elif x1 == 6 and y1 == 2 and x2 == 13 and y2 == 2:
                                print('¡CORRECTO! La palabra es LLORANTE')
                                palabras.append('LLORANTE')
                            elif x1 == 13 and y1 == 8 and x2 == 8 and y2 == 3:
                                print('¡CORRECTO! La palabra es DA GAMA')
                                palabras.append('DA GAMA')
                            else:
                                print('La palabra que ingresó no es correcta')
                                intentos += 1
                                vida = user.vidas
                                vida -= 0.5
                                user.vidas = vida
                                print(user.vidas)

                    else:
                        print('Ya no tienes más intentos')
                        break
                else: 
                    print('¡FELICIDADES! Haz conseguido todas las palabras')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE LÓGICA BOOLEANA---
def pregunta_boobleana(preguntas_booleanas):
    aleatorio = random.choice(preguntas_booleanas)
    return aleatorio

def jugar_booleano(user, preguntas_booleanas):
    pregunta_aleatoria = pregunta_unimet(preguntas_booleanas)
    print(pregunta_aleatoria)
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            respuesta = input('Ingrese su respuesta: ').title()
            while not respuesta.isalpha():
                respuesta = input('Ingrese su respuesta: ').title()
            # Asociando las preguntas con sus respectivas respuestas
            if pregunta_aleatoria == preguntas_booleanas[0]:
                respuesta_1 = 'True'
                if respuesta_1 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('libro de Física')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                respuesta_2 = 'False'
                if respuesta_2 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('libro de Física')
                    user.inventario = inventario
                    print(user.inventario)
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#--- JUEGO DE MEMORIA CON EMOJIS--- 
def jugar_memoria(user):
    intentos = 0
    emojis = []
    contador_pistas = 0

    if user.vidas > 0:
        print('---BIENVENIDO---')
        while True:
            matriz = ('''
                        0     1      2     3
                    0 ['😀', '🙄', '🤮', '🥰'],
                    1 ['🤮', '😨', '🤓', '😷'],
                    2 ['😨', '🤓', '🥰', '😷'],
                    3 ['🤑', '🤑', '🙄', '😀']
                    ''')

            print(matriz)
            print('\n')
            print('Escoge los emojis que sean iguales')
            print('Si deseas usar una pista para conseguir el segundo emoji, debes introducir las coordenasdas del primer emoji y luego presionar "4" en las coordenadas del segundo emoji')
            x1 = int(input('Ingrese la coordenada en x del primer emoji: '))
            y1 = int(input('Ingrese la coordenada en y del primer emoji: '))
            x2 = int(input('Ingrese la coordenada en x del segundo emoji: '))
            y2 = int(input('Ingrese la coordenada en y del segundo emoji: '))

            pista = user.pistas

            if len(emojis) < 7:
                if intentos < 2:
                    if x2 == 4 and y2 == 4: 
                        if user.pistas > 0:                              
                            contador_pistas += 1
                            if x1 == 0  and y1 == 0:
                                print('El segundo emoji se encuentra en las coordenadas [3,3]')
                                pista -= 1
                            elif x1 == 3 and y1 == 3:
                                print('El segundo emoji se encuentra en las coordenadas [0,0]')
                                pista -= 1

                            elif x1 == 0 and y1 == 1:
                                print('El segundo emoji se encuentra en las coordenadas [3,2]')
                                pista -= 1
                            elif x1 == 3 and y1 == 2:
                                print('El segundo emoji se encuentra en las coordenadas [0,1]')
                                pista -= 1

                            elif x1 == 0 and y1 == 2:
                                print('El segundo emoji se encuentra en las coordenadas [1,0]')
                                pista -= 1
                            elif x1 == 1 and y1 == 0:
                                print('El segundo emoji se encuentra en las coordenadas [0,2]')
                                pista -= 1
                            
                            elif x1 == 0 and y1 == 3:
                                print('El segundo emoji se encuentra en las coordenadas [2,2]')
                                pista -= 1
                            elif x1 == 2 and y1 == 2:
                                print('El segundo emoji se encuentra en las coordenadas [0,3]')
                                pista -= 1
                            
                            elif x1 == 1 and y1 == 1:
                                print('El segundo emoji se encuentra en las coordenadas [2,0]')
                                pista -= 1
                            elif x1 == 2 and y1 == 0:
                                print('El segundo emoji se encuentra en las coordenadas [1,1]')
                                pista -= 1

                            elif x1 == 1 and y1 == 3:
                                print('El segundo emoji se encuentra en las coordenadas [2,3]')
                                pista -= 1
                            elif x1 == 2 and y1 == 3:
                                print('El segundo emoji se encuentra en las coordenadas [1,3]')
                                pista -= 1

                            elif x1 == 3 and y1 == 0:
                                print('El segundo emoji se encuentra en las coordenadas [3,1]')
                                pista -= 1
                            elif x1 == 3 and y1 == 1:
                                print('El segundo emoji se encuentra en las coordenadas [3,0]')
                                pista -= 1

                            elif x1 == 1 and y1 == 2:
                                print('El segundo emoji se encuentra en las coordenadas [2,1]')
                                pista -= 1
                            elif x1 == 2 and y1 == 1:
                                print('El segundo emoji se encuentra en las coordenadas [1,2]')
                                pista -= 1

                    if x1 == 0  and y1 == 0 and x2 == 3 and y2 == 3:
                        print('¡CORRECTO! Encontraste el par de 😀')
                        emojis.append('😀')
                    elif x1 == 3 and y1 == 3 and x2 == 0 and y2 == 0:
                        print('¡CORRECTO! Encontraste el par de 😀')
                        emojis.append('😀')

                    elif x1 == 0 and y1 == 1 and x2 == 3 and y2 == 2:
                        print('¡CORRECTO! Encontraste el par de 🙄')
                        emojis.append('🙄')
                    elif x1 == 3 and y1 == 2 and x2 == 0 and y2 == 1:
                        print('¡CORRECTO! Encontraste el par de 🙄')
                        emojis.append('🙄')

                    elif x1 == 0 and y1 == 2 and x2 == 1 and y2 == 0:
                        print('¡CORRECTO! Encontraste el par de 🤮')
                        emojis.append('🤮')
                    elif x1 == 1 and y1 == 0 and x2 == 0 and y2 == 2:
                        print('¡CORRECTO! Encontraste el par de 🤮')
                        emojis.append('🤮')

                    elif x1 == 0 and y1 == 3 and x2 == 2 and y2 == 2:
                        print('¡CORRECTO! Encontraste el par de 🥰')
                        emojis.append('🥰')
                    elif x1 == 2 and y1 == 2 and x2 == 0 and y2 == 3:
                        print('¡CORRECTO! Encontraste el par de 🥰')
                        emojis.append('🥰')

                    elif x1 == 1 and y1 == 1 and x2 == 2 and y2 == 0:
                        print('¡CORRECTO! Encontraste el par de 😨')
                        emojis.append('😨')
                    elif x1 == 2 and y1 == 0 and x2 == 1 and y2 == 1:
                        print('¡CORRECTO! Encontraste el par de 😨')
                        emojis.append('😨')

                    elif x1 == 1 and y1 == 3 and x2 == 2 and y2 == 3:
                        print('¡CORRECTO! Encontraste el par de 😷')
                        emojis.append('😷')
                    elif x1 == 2 and y1 == 3 and x2 == 1 and y2 == 3:
                        print('¡CORRECTO! Encontraste el par de 😷')
                        emojis.append('😷')

                    elif x1 == 3 and y1 == 0 and x2 == 3 and y2 == 1:
                        print('¡CORRECTO! Encontraste el par de 🤑')
                        emojis.append('🤑')
                    elif x1 == 3 and y1 == 1 and x2 == 3 and y2 == 0:
                        print('¡CORRECTO! Encontraste el par de 🤑')
                        emojis.append('🤑')

                    elif x1 == 1 and y1 == 2 and x2 == 2 and y2 == 1:
                        print('¡CORRECTO! Encontraste el par de 🤓')
                        emojis.append('🤓')
                    elif x1 == 2 and y1 == 1 and x2 == 1 and y2 == 2:
                        print('¡CORRECTO! Encontraste el par de 🤓')
                        emojis.append('🤓')

                    else:
                        print('El par de emojis que ingresó no son correctos')
                        intentos += 1
                        vida = user.vidas
                        vida -= 0.25
                        user.vidas = vida
                        print(user.vidas)
                else:
                    print('Ya no tienes más intentos')
                    break
            else: 
                print('¡FELICIDADES! Haz conseguido todos los pares de emojis')
                inventario = user.inventario
                inventario.append('martillo')
                user.inventario = inventario
                print(user.inventario)
                break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE CULTURA UNIMETANA---  
def pregunta_unimet(preguntas_unimet):
    aleatorio = random.choice(preguntas_unimet)
    return aleatorio

def jugar_cultuta_unimet(user, preguntas_unimet):
    pregunta_aleatoria = pregunta_unimet(preguntas_unimet)
    print(pregunta_aleatoria)
    intentos = 0
    
    contador_pistas = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            # respuesta = input('Ingrese su respuesta: ')
            pista = user.pistas
            # Opción de pedir un pista y Asociando las preguntas con sus respectivas respuestas
            if pregunta_aleatoria == preguntas_unimet[0]:
                print('22 de septiembre')
                print('22 de octubre')
                print('25 de octubre')
                print('25 de septiembre')
                print('Si deseas usar una pista presiona "*"')
                respuesta = input('Ingrese su respuesta: ')
                respuesta_1 = '22 de octubre'
                if respuesta == '*':
                    if user.pistas > 0:
                        contador_pistas += 1
                        if pregunta_aleatoria == preguntas_unimet[0]:
                            if contador_pistas == 1:
                                print('es en octubre')
                                pista -= 1
                            else:
                                print('Ya no hay mas pistas')
                    else:
                        print('Se te acabaron las pistas')

                elif respuesta_1 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('libro de matemáticas')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break

            elif pregunta_aleatoria == preguntas_unimet[1]:
                print('1979')
                print('1969')
                print('1970')
                print('1980')
                print('Si deseas usar una pista presiona "*"')
                respuesta = input('Ingrese su respuesta: ')
                respuesta_2 = '1970'
                if respuesta == '*':
                    if user.pistas > 0:
                        contador_pistas += 1
                        if pregunta_aleatoria == preguntas_unimet[1]:
                            if contador_pistas == 1:
                                print('termina en 0 el año')
                                pista -= 1
                            else:
                                print('Ya no hay mas pistas')
                    else:
                        print('Se te acabaron las pistas')

                elif respuesta_2 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('libro de matemáticas')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                print('Eugenio Mendoza')
                print('Rafael Matiezo')
                print('Lorenzo Mendoza')
                print('Luis Miguel Da Gama')
                print('Si deseas usar una pista presiona "*"')
                respuesta = input('Ingrese su respuesta: ').title()
                respuesta_3 = 'Eugenio Mendoza'
                if respuesta == '*':
                    if user.pistas > 0:
                        contador_pistas += 1
                        if pregunta_aleatoria == preguntas_unimet[2]:
                            if contador_pistas == 1:
                                print('tiene una estatua')
                                pista -= 1
                            else:
                                print('Ya no hay mas pistas')
                    else:
                        print('Se te acabaron las pistas')

                elif respuesta_3 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('libro de matemáticas')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.5
                    user.vidas = vida
                    print(user.vidas)
                    break
    
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')

    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE ENCUENTRA LA LÓGICA---
def pregunta_logica(preguntas_logica):
    aleatorio = random.choice(preguntas_logica)
    return aleatorio

def jugar_logica(user, preguntas_logica):
    pregunta_aleatoria = pregunta_logica(preguntas_logica)
    print(pregunta_aleatoria)
    intentos = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            respuesta = int(input('Ingrese su respuesta: '))
            while not respuesta.isnumeric():
                respuesta = int(input('Ingrese su respuesta: '))
            # Asociando las preguntas con sus respectivas respuestas
            if pregunta_aleatoria == preguntas_logica[0]:
                respuesta_1 = 67
                if respuesta_1 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('Disco Duro')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                respuesta_2 = 41
                if respuesta_2 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('Disco Duro')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DEL CRIPTOGRAMA---
def pregunta_criptograma(preguntas_criptograma):
    aleatorio = random.choice(preguntas_criptograma)
    return aleatorio

def jugar_criptograma(user, preguntas_criptograma):
    pregunta_aleatoria = pregunta_criptograma(preguntas_criptograma)
    print('Debes descifrar el siguente criptograma')
    print(pregunta_aleatoria)
    intentos = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            respuesta = input('Ingrese su respuesta: ')
            # Asociando las preguntas con sus respectivas respuestas
            if pregunta_aleatoria == preguntas_criptograma[0]:
                respuesta_1 = 'Si te graduas pisas el samán'
                if respuesta_1 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('Mensaje: Si estas gradudado puedes pisar el Samán')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break

            elif pregunta_aleatoria == preguntas_criptograma[1]:
                respuesta_2 = 'Si te graduas pisas el samán'
                if respuesta_2 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('Mensaje: Si estas gradudado puedes pisar el Samán')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break

            else:
                respuesta_3 = 'Si te graduas pisas el samán'
                if respuesta_3 == respuesta:
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('Mensaje: Si estas gradudado puedes pisar el Samán')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)
                    break
    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
    
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)


#---JUEGO DE PREGUNTAS MATEMÁTICAS---
def pregunta_matematica(preguntas_matematica):
    aleatorio = random.choice(preguntas_matematica)
    return aleatorio

def jugar_matematica(user, preguntas_matematica):
    pregunta_aleatoria = pregunta_matematica(preguntas_matematica)
    print(pregunta_aleatoria)
    intentos = 0

    contador_pistas = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            print('Si deseas usar una pista presiona "*"')
            respuesta = input('Ingrese su respuesta: ')
            # Opción de pedir un pista
            pista = user.pistas

             
            if respuesta == '*': 
                if user.pistas > 0:                              
                    contador_pistas += 1
                    if pregunta_aleatoria == preguntas_matematica[0]:
                        if contador_pistas == 1:
                            print('no hay pistas aquí jajajajaj')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                    elif pregunta_aleatoria == preguntas_matematica[1]:
                        if contador_pistas == 1:
                            print('no hay pistas aquí jajajajaj')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                    elif pregunta_aleatoria == preguntas_matematica[2]:
                        if contador_pistas == 1:
                            print('no hay pistas aquí jajajajaj')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                else:
                    print('Se te acabaron las pistas')
            
                user.pistas = pista
            # Asociando las preguntas con sus respectivas respuestas
            elif pregunta_aleatoria == preguntas_matematica[0]:
                respuesta_1 = diff(sin(3.1415)/2 - tan(3.1415)**2)
                if respuesta_1 == int(respuesta):
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('cable HDMI')
                    user.inventario = inventario
                    print(user.inventario)
                    break
                    
                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.25
                    user.vidas = vida
                    print(user.vidas)
                    break

            elif pregunta_aleatoria == preguntas_matematica[1]:
                respuesta_2 = diff((sen(3.1415)) / 2)
                if respuesta_2 == int(respuesta):
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('cable HDMI')
                    user.inventario = inventario
                    print(user.inventario)
                    break

                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.25
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                respuesta_3 = diff((sen(3.1415))/5 - (tan(3.1415)))
                if respuesta_3 == int(respuesta):
                    print('La respuesta es correcta')
                    inventario = user.inventario
                    inventario.append('cable HDMI')
                    user.inventario = inventario
                    print(user.inventario)
                    break

                else:
                    print('La respuesta es incorrecta')
                    vida = user.vidas
                    vida -= 0.25
                    user.vidas = vida
                    print(user.vidas)
                    break

    else:
        print('Se te acabaron las vidas ¡GAME OVER!')  

    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Incompleto'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)             


#---JUEGO DEL AHORCADO---  
def palabra(palabras_ahorcado):
    aleatorio = random.randint(0, len(palabras_ahorcado) - 1)
    return palabras_ahorcado[aleatorio]

def consola(ocultas, intentos, imagenes):
    print(imagenes[intentos])
    print('')
    print(ocultas)

def jugar(user, palabras_ahorcado, imagenes):
    palabra_aletoria = palabra(palabras_ahorcado)
    ocultas = ['-'] * len(palabra_aletoria)
    intentos = 0
    # Asociando las preguntas con sus respectivas respuestas
    if palabra_aletoria == 'metromix':
        print('Me encuentro en la entrada de la Universidad')
    elif palabra_aletoria == 'piscina':
        print('Me buscan y nunca me encuentran en la Universidad')
    else:
        print('Tienes que subir muchos pisos para llegar a mi')

    contador_pistas = 0
    # Validando la cantidad de vidas restantes
    if user.vidas > 0:
        while True:
            consola(ocultas, intentos, imagenes)
            print('Si deseas usar una pista presiona "*"')
            letra = str(input('Escoge una letra: '))
            while not letra.isalpha() and letra != '*':
                letra = str(input('Escoge una letra: '))
            # Opción de pedir un pista
            pista = user.pistas
            
            if letra == '*':
                if user.pistas > 0:
                    contador_pistas += 1
                    if palabra_aletoria == 'metromix':
                        if contador_pistas == 1:
                            print('sitio de comida')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('al lado de las copias')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Comienza por Metro')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')

                    elif palabra_aletoria == 'piscina':
                        if contador_pistas == 1:
                            print('Es rectangular')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('Tiene agua')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Se puede nadar')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')
                        
                    elif palabra_aletoria == 'rectorado':
                        if contador_pistas == 1:
                            print('Esta en el Eugenio Mendoza')
                            pista -= 1
                        elif contador_pistas == 2:
                            print('Ultimo piso del Eugenio')
                            pista -= 1
                        elif contador_pistas == 3:
                            print('Oficina del Rector')
                            pista -= 1
                        else:
                            print('Ya no hay mas pistas')
                else:
                    print('Se te acabaron las pistas')
            
            user.pistas = pista

            # Comparando la letra introducido por el usuario con la palabra seleccionada
            indice = []
            for l in range(len(palabra_aletoria)):
                if palabra_aletoria[l] == letra:
                    indice.append(l)
            # Intentos errados
            if len(indice) == 0:
                intentos += 1

                if intentos == 7:
                    consola(ocultas, intentos, imagenes)
                    print('')
                    print(f'"F" La palabra era {palabra_aletoria}')
                    vida = user.vidas
                    vida -= 5
                    user.vidas = vida
                    print(user.vidas)
                    break
            else:
                for l in indice:
                    ocultas[l] = letra

                indice = []
            # Intentos acertados
            try:
                ocultas.index('-')
            except ValueError:
                print('')
                print('"Así mismo es"')
                inventario = user.inventario
                inventario.append('cable HDMI')
                user.inventario = inventario
                print(user.inventario)
                break

    else:
        print('Se te acabaron las vidas ¡GAME OVER!')
        sys.exit()
        
    # Se actualizan los datos en el archivo txt de las estadiasticas
    nu = user.username
    with open('DatosEstadisticas.txt') as dataes:
        datos = dataes.readlines()
    for dato in datos:
        user_2 = dato[:-1].split('-')
        # print(datos[-1])
        if nu in user_2[0]:
            user_2[6] = f'Pistas Restantes: {user.pistas}'
            user_2[5] = f'Vidas Restantes: {user.vidas}'
            user_2[3] = f'Inventario: {user.inventario}'
            if user.vidas > 0:
                user_2[-1] = 'Status: Ganador'
            else:
                user_2[-1] = 'Status: Perdedor'
            datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
        
            print(user_2[0])
            print(user_2[5])


    with open('DatosEstadisticas.txt', 'w') as dataes:
        dataes.writelines(datos)

        
# ---CUARTO 1 (LA BIBLIOTECA)---
def cuarto_1(user,  palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño):
    while True:
        # Validar que el jugador aún tenga vidas disponibles
        if user.vidas > 0:
            print('---CUARTO 1---')
            print('\n')
            time.sleep(1)
            color = fg('#8d2424') + bg('#ffffff')
            res = attr('reset')
            print(color + '''
            ----------------------------------BIBLIOTECA---------------------------------
            |   |                                                                    |  |
            | /||                           ______________                           |  |
            || ||                           |   |  |  |  |                           |  |
            || ||                           |___|__|__|__|                       ____|  |
            || ||                           |  |  |  |   |                      |\____\ |
            || ||                           |__|__|__|___|                      | |   | |
            ||/ |                           |  |  |   |  |                      |\|   | |
            |   |_/_________________________|__|__|___|__|______________________| |   | |
            |  / /|                                                             |\|   | |
            | / /|                                                               \|___| |
            |/_________________________________________________________________________\|
            Estas en la biblioteca de la UNIMET

            ''' + res)
            # print('Estas en la biblioteca de la UNIMET')
            print('\n')
            time.sleep(1)
            print('Hay 3 objetos')
            print('\n')
            time.sleep(1)
            print('1: Un mueble de libros ubicado en el centro')
            time.sleep(1)
            print('2: Un mueble para sentarse a la izquierda')
            time.sleep(1)
            print('3: Un mueble con gabetas a la derecha')
            print('\n')
            time.sleep(1)
            print('(Si desea cambiar de cuarto presione 4)')
            print('\n')
            time.sleep(1)
            decision = int(input('Escoge uno: '))
            while decision != 1 and decision != 2 and decision != 3 and decision != 4:
                decision = int(input('Escoge uno: '))

            if decision == 1:
                # El Ahorcado
                
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Solo tienes 7 intentos para dar con la palabra correcta. Escribe letra por letra hasta completar la palabra.')
                print('\n')
                time.sleep(0.5)
                jugar(user, palabras_ahorcado, imagenes)
                

            elif decision == 2:
                #Preguntas Matematicas
                # for objeto in user.inventario:
                if "libro de matemáticas" in user.inventario:
                    print('¡Que empiece el juego!')
                    print('\n')
                    time.sleep(0.5)
                    print('Veamos que tan bueno eres en matemáticas. En este juego tendrás con resolver un derivada, solo tendras que escribir el resultado.')
                    print('\n')
                    time.sleep(0.5)
                    jugar_matematica(user, preguntas_matematica)
                else:
                    print('Necesito que sepas derivar')

            elif decision == 3:
                #Criptograma
                if "llave" in user.inventario:
                    print('¡Que empiece el juego!')
                    print('\n')
                    time.sleep(0.5)
                    print('¿Eres bueno descifrando mensajes ocultos? Ya lo veremos. Tendrás que descifrar el siguiente mensaje.')
                    print('\n')
                    time.sleep(0.5)
                    jugar_criptograma(user, preguntas_criptograma)
                else:
                    print('No me puedes abrir, busca algo para abrirme')
            
            else:
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Samán\n2: Puertas de laboratorio')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_2(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_3(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

            print('\n')
            continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()
            while continuar != 'S' and continuar != 'N':
                continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()

            if continuar == 'N':
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Samán\n2: Puertas de laboratorio')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_2(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_3(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

        else:
            print('Se te acabaron las vidas ¡GAME OVER!')
            sys.exit()

#---CUARTO 2 (PLAZA DE RECTORADO)---
def cuarto_2(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño):
    while True:
        # Validar que el jugador aún tenga vidas disponibles
        if user.vidas > 0:
            print('---CUARTO 2---')
            time.sleep(1)
            color = fg('#8d2424') + bg('#ffffff')
            res = attr('reset')
            print(color + '''
            -------------------------------------PLAZA-----------------------------------

            
                   ____________________________︵.︵_______________________________
                  /                           (˛. *˛)                             \
                 /  /                        (˛˛. *。)                           \ \
                /  /|                        (˛* ˛*˛*)                           |\ \
               /  /                             |.|                                \ \
              /  /|                                                                |\ \
             /_________________________________________________________________________\
            Estas en la plaza de rectorado de la UNIMET

            ''' + res)
            # print('Estas en la plaza de rectorado de la UNIMET')
            print('\n')
            time.sleep(1)
            print('Hay 3 objetos')
            print('\n')
            time.sleep(1)
            print('1: El Samán ubicado en el centro')
            time.sleep(1)
            print('2: Un banco para sentarse a la izquierda')
            time.sleep(1)
            print('3: Otro banco para sentarse a la derecha')
            print('\n')
            time.sleep(1)
            print('(Si desea cambiar de cuarto presione 4)')
            print('\n')
            time.sleep(1)
            decision = int(input('Escoge uno: '))
            while decision != 1 and decision != 2 and decision != 3 and decision != 4:
                decision = int(input('Escoge uno: '))

            if decision == 1:
                # Encuentra la lógica y resuelve
                if 'Titulo Universitario' in user.inventario and 'Mensaje: Si estas gradudado puedes pisar el Samán' in user.inventario:
                    print('¡Que empiece el juego!')
                    print('\n')
                    time.sleep(0.5)
                    print('Si consideras tener buena lógica pues este juego es para ti. Debes hallar el valor oculto detrás de los emojis.')
                    print('\n')
                    time.sleep(0.5)
                    jugar_logica(user, preguntas_logica)
                else:
                    print('Pierdes una vida por pisar el samán 🥵')
                    vida = user.vidas
                    vida -= 1
                    user.vidas = vida
                    print(user.vidas)


            elif decision == 2:
                #Quizizz Cultura Unimetana
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('En este juego pondremos a prueba tus conocimientos sobre la UNIMET. Se te darán algunas opciones y debes escriber la correcta.')
                print('\n')
                time.sleep(0.5)
                jugar_cultuta_unimet(user, preguntas_unimet)

            elif decision == 3:
                #memoria con emojis
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Veamos que tan buena es tu memorización. Aquí tendrás que escribir las coordenadas X e Y de los pares de emojis.')
                print('\n')
                time.sleep('0.5')
                jugar_memoria(user)
            
            else: 
                print('\n')
                cuarto_1(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
            
            print('\n')
            continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()
            if continuar == 'N':
                cuarto_1(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                # break
        nu = user.username
        with open('DatosEstadisticas.txt') as dataes:
            datos = dataes.readlines()
        for dato in datos:
            user_2 = dato[:-1].split('-')
            # print(datos[-1])
            if nu in user_2[0]:
                user_2[5] = f'Vidas Restantes: {user.vidas}'
                datos[-1] = f'{user_2[0]} - {user_2[1]} - {user_2[2]} - {user_2[3]} - {user_2[4]} - {user_2[5]} - {user_2[6]} - {user_2[7]} - {user_2[8]}\n'
            
                print(user_2[0])
                print(user_2[5])


        with open('DatosEstadisticas.txt', 'w') as dataes:
            dataes.writelines(datos)

        else:
            print('Se te acabaron las vidas ¡GAME OVER!')
            sys.exit()

#---CUARTO 3 (PASILLO DE LOS LABORATORIOS)---
def cuarto_3(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño):
    while True:
        # Validar que el jugador aún tenga vidas disponibles
        if user.vidas > 0:
            print('---CUARTO 3---')
            print('\n')
            time.sleep(1)
            color = fg('#8d2424') + bg('#ffffff')
            res = attr('reset')
            print(color + '''
            ------------------------------------PUERTA-----------------------------------
            | |                           ___________________                         | |
            | |                          |                   |                        | |
            | |                          |                   |                        | |
            | |                          |                   |                        | |
            | |                          |                   |                        | |
            | |                          |                _  |                        | |
            | |                          |               |o| |                        | |
            | |                          |               |_| |                        | |
            | |                          |                   |                        | |
            | |__________________________|___________________|________________________| |
            |/_________________________________________________________________________\|
            Estas en el pasillo de los laboratorios de la UNIMET

            ''' + res)
            # print('Estas en el pasillo de los laboratorios de la UNIMET')
            print('\n')
            time.sleep(1)
            print('Hay solo un objeto')
            print('\n')
            time.sleep(1)
            print('1: Una puerta ubicada en el centro')
            print('\n')
            time.sleep(1)
            print('(Si desea cambiar de cuarto presione 2)')
            print('\n')
            time.sleep(1)
            print('\n')
            decision = int(input('Toma la puerta: '))
            while decision != 1 and decision != 2:
                decision = int(input('Escoge uno: '))

            if decision == 1:
                # Lógica Booleana
                if 'martillo' in user.inventario:
                    print('¡Que empiece el juego!')
                    print('\n')
                    time.sleep(0.5)
                    print('Se te hará una pregunta y tendrás que contestar con True o False')
                    print('\n')
                    time.sleep(0.5)
                    jugar_booleano(user, preguntas_booleanas)
                else:
                    print('Está cerrado con candado!!!!!')
            
            else:
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Biblioteca\n2: Laboratorios')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_1(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

            print('\n')
            continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()
            if continuar == 'N':
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Biblioteca\n2: Laboratorios')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_1(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

        else:
            print('Se te acabaron las vidas ¡GAME OVER!')
            sys.exit()

#---CUARTO 4 (LABORATORIOS)---
def cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño):
    while True:
        # Validar que el jugador aún tenga vidas disponibles
        if user.vidas > 0:
            print('---CUARTO 4---')
            print('\n')
            time.sleep(1)
            color = fg('#8d2424') + bg('#ffffff')
            res = attr('reset')
            print(color + '''
            ---------------------------------LABORATORIO---------------------------------
            |   |                                                                    |  |
            |   |                         ____________________                       |  |
            |   |                        |LKNF1LGNDMLKFMGKFDRR|                      |  |
            |   |                        |LRKTHJLDKJFKDJ9GLKJD|                      |  |
            |   |                        |OIRUTRTKJELKFKDLNEKJ|                      |  |
            |   |  _______               |KLFJGLDKJFGLKDFKGMLK|              _______ |  |
            |   | |       |              |KJDLKF3GDLLYKLDJGJDK|             |       ||  |
            |   | |_______|              |IOIJJNLKWKFCFGNDLKGD|             |_______||  |
            |   |__|____|__              |KDJFKGJDKRKLDJFKG6DK|            __|____|__|  |
            |   |          |             |____________________|           |          |  |
            |   |          |                                              |          |  |
            |   |__________|______________________________________________|_________ |  |
            |  /                                                                     \  |
            | /                                                                       \ |
            |/_________________________________________________________________________\|
            Estas en los laboratorios de la UNIMET

            ''' + res)
            # print('Estas en los laboratorios de la UNIMET')
            print('\n')
            time.sleep(1)
            print('Hay 3 objetos')
            print('\n')
            time.sleep(1)
            print('1: Una pizarra ubicada en el centro')
            time.sleep(1)
            print('2: Un computador ubicado a la izquierda')
            time.sleep(1)
            print('3: Un computador ubicado a la derecha')
            print('\n')
            time.sleep(1)
            print('(Si desea cambiar de cuarto presione 4)')
            print('\n')
            time.sleep(1)
            decision = int(input('Escoge uno: '))
            while decision != 1 and decision != 2 and decision != 3 and decision != 4:
                decision = int(input('Escoge uno: '))

            if decision == 1:
                # Sopa de letras
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Veamos que tan bueno eres encontrando palabras. Deberás escribir las coordenadas X e Y tanto de la primera como de la ultima letra de la palabra')
                print('\n')
                time.sleep(0.5)
                jugar_sopa(user, matriz_1, matriz_2, matriz_3)
            elif decision == 2:
                # Preguntas sobre python
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('En este juego pondremos a prueba tus conociminetos sobre python. Deberás escribir en una línea de código la solución del problema propuesto')
                print('\n')
                time.sleep(0.5)
                jugar_python(user, preguntas_python)
            elif decision == 3:
                # Adivinanzas
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Veamos si logras adivinar el acertijo que te tenemos.')
                print('\n')
                time.sleep(0.5)
                jugar_adivinanzas(user, adivinanzas)
            
            else:
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Pasillo de los laboratorios\n2: Sala de servidores')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_3(user, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_5(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
            print('\n')
            continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()
            if continuar == 'N':
                print('\n')
                print('¿A qué habitación desea ir?')
                print('\n')
                print('1: Pasillo de los laboratorios\n2: Sala de servidores')
                print('\n')
                cuartos = int(input('Escoja una habitación: '))
                while cuartos != 1 and cuartos != 2:
                    cuartos = int(input('Escoja una habitación: '))
                if cuartos == 1:
                    cuarto_3(user, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                else:
                    cuarto_5(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
        
        else:
            print('Se te acabaron las vidas ¡GAME OVER!')
            sys.exit()

#---CUARTO 5 (SALA DE SERVIDORES)---
def cuarto_5(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño):
    while True:
        # Validar que el jugador aún tenga vidas disponibles
        if user.vidas > 0:
            print('---CUARTO 5---')
            print('\n')
            time.sleep(1)
            color = fg('#8d2424') + bg('#ffffff')
            res = attr('reset')
            print(color + '''
            ------------------------------SALA DE SERVIDORES ----------------------------
            |   |                                                                    |  |
            | /||                           ______________                           |  |
            ||/||                           |            |                           |  |
            ||/||                           |            |                           |  |
            ||/||                           |            |                           |  |
            ||/||                           |            |                           |  |
            ||/||                           |            |                       ____|  |
            ||/||___________________________|____________|______________________|\ ___\ |
            ||//                                                                | |   | |
            ||/                                                                  \|___| |
            |/_________________________________________________________________________\|
            Estas en la sala de servidores de la UNIMET

            ''' + res)
            # print('Estas en la sala de servidores de la UNIMET')
            print('\n')
            time.sleep(1)
            print('Hay 3 objetos')
            print('\n')
            time.sleep(1)
            print('1: Una puerta ubicada en el centro')
            time.sleep(1)
            print('2: Un Rack ubicado a la izquierda')
            time.sleep(1)
            print('3: Una papelera ubicada a la derecha')
            print('\n')
            time.sleep(1)
            print('(Si desea cambiar de cuarto presione 4)')
            print('\n')
            time.sleep(1)
            decision = int(input('Escoge uno: '))
            while decision != 1 and decision != 2 and decision != 3 and decision != 4:
                decision = int(input('Escoge uno: '))

            if decision == 1:
                # 21 Blackjack
                if 'carnet' in user.inventario:
                    print('¡Que empiece el juego!')
                    print('\n')
                    time.sleep(0.5)
                    print('Veamos si la suerte está de tu lado. Debes conseguir 21 BlackJack o ganarle a tu oponente.')
                    print('\n')
                    time.sleep(0.5)
                    jugar_blackjack()
                else:
                    print('Necesitas tener un carnet de trabajador para poder pasar')
            elif decision == 2:
                # Palabra mezclada
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Las siguentes palabras se encuentran mezcladas. Deberas ordenarlas una por una.')
                print('\n')
                jugar_mezcladas(user, palabras_cocina, palabras_baile, palabras_baño)
            elif decision == 3:
                # escoge un número entre
                print('¡Que empiece el juego!')
                print('\n')
                time.sleep(0.5)
                print('Tal y como lo veo, este juego es de pura suerte. A lo largo del juego recibirás algo de ayuda')
                print('\n')
                jugar_numero(user)
            else:
                print('\n')
                cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                
            
            print('\n')
            continuar = input('¿Desea continuar en la habitación? [S/N]: ').upper()
            if continuar == 'N':
                print('\n')
                print('¿Desea volver a la habitación anterior (laboratorios)?')
                print('\n')
                cuartos = input('Tome una decisión [S/N]: ').upper()
                while cuartos != 'S' and cuartos != 'N':
                    cuartos = input('Tome una decisión: ')
                if cuartos == 'N':
                    break
                else:
                    cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

        else:
            print('Se te acabaron las vidas ¡GAME OVER!')
            sys.exit()
 

#---CRONOMETRO DEL JUEGO---
# def cronometro(user):
#     tiempo = user.tiempo

#     minutos = 0
#     segundos = 0

#     while minutos < tiempo:
#         for n in range(1,61):
#             time.sleep(1)
#             n = segundos
#             segundos += 1
#             if segundos == 60:
#                 segundos = 00
#                 minutos += 1
#                 time.sleep(1)
#             # print(f'{minutos}:{segundos}')
#     sys.exit()
            
#     return minutos, segundos


#---VISUALIZAR LISTA DE USUARIOS REGISTRADOS---
def ver_usuarios():
    usuarios = []
    try: 
        with open('DatosUsuarios.txt') as dataus:
            datos = dataus.readlines()
        if len(datos) == 0:
            print('\nTodavía no hay ningún usuario registrado.\n')
        else:
            for dato in datos:
                user = dato[:-1].split('-')
                usuarios.append(Jugador(user[0],user[1],user[2],user[3],user[4],user[5],user[6],user[7], user[-1]))

            print("\n\t\tUSUARIOS REGISTRADOS (por orden de registro)\n")
            for i,us in enumerate(usuarios):
                print("-"*2,str(i+1),"-"*18)
                print(us.mostrar_nombre_de_usuario())
            return True
    
    except FileNotFoundError:
        print("\nTodavía no hay ningún usuario registrado.\n")
        return False


#---VALIDAR EXISTEN DE USUARIOS REGISTRADOS---
def validar_existencia_username():
    # Pedir el nombre que desea usar el usuario en el juego
    username = input('Ingrese su nombre de usuario: ')
    un = username.split()
    # Validando el nombre introducido por el usuario
    while True:
        if not ("".join(un)).isalpha():
            username = input("Ingreso inválido, ingrese su nombre de usuario: ")
            un = username.split()
        elif ("".join(un)).isalpha():
            break
    username = username.title()
    # Pedir contraseña 
    contraseña = input('Ingrese su contraseña: ')
    con = contraseña.split()
    # Validando la contraseña introducida por el usuario
    while True:
        if not ("".join(con)).isalnum():
            contraseña = input("Ingreso inválido, ingrese su contraseña: ")
            con = contraseña.split()
        elif ("".join(con)).isalnum():
            break
    # Validando que el nombre y contraseña no existan
    try:
        with open('DatosUsuarios.txt') as dataus:
            datos = dataus.readlines()
        for dato in datos:
            username_l = dato[:-1].split(" - ")
            for i,j in enumerate(username_l):
                if i == 0:
                    if j == username:
                        print("\nUsername ya registrado.")
                        user = Jugador(username_l[0],username_l[1],username_l[2],username_l[3],username_l[4],username_l[5],username_l[6],username_l[7], username_l[-1])
                        return user

                elif i == 1:
                    if j == contraseña:
                        print('\nContraseña ya registrada')
                        user = Jugador(username_l[0],username_l[1],username_l[2],username_l[3],username_l[4],username_l[5],username_l[6],username_l[7], username_l[-1])
                        return user

            
        else:
            return registar_nuevo_jugador(username, contraseña)
    except FileNotFoundError:
        print("\nTodavía no hay ningún username registrado.\n")
        return registar_nuevo_jugador(username, contraseña)


#---REGISTRAR NUEVOS USUARIOS---
def registar_nuevo_jugador(username,contraseña):  
    # Lista de avatares
    avatares = {
        1 : 'Scharifker', 
        2 : 'Eugenio Mendoza', 
        3 : 'Pelusa', 
        4 : 'Gandhi'
        }            
    # Pedir la edad del usuario 
    edad = input('Ingrese su edad: ')
    while not edad.isnumeric():
        edad = input('¡ERROR! Ingrese su edad: ')
    # Pedir avatar que desea usar el usuario
    print(avatares)
    avatar = int(input('Escoja un avatar: '))
    while avatar != 1 and avatar != 2 and avatar != 3 and avatar != 4:
        avatar = int(input('Escoja un avatar que si exista: '))
    for key in avatares:
        if key == avatar:
            value = avatares.get(key)
            avatar = value
    # Pedir nivel de dificultad
    print('1: Fácil\n2: Medio\n3: Difícil')
    dificultad = int(input('Escoja un nivel de dificultad: '))
    while dificultad != 1 and dificultad != 2 and dificultad != 3:
        dificultad = int(input('Escoja un nivel de dificultad: '))

    if dificultad == 1:
        dificultad = 'Fácil'
        vidas = 5.0
        pistas = 5
        tiempo = 1200
        
    elif dificultad == 2:
        dificultad = 'Medio'
        vidas = 3.0
        pistas = 3
        tiempo = 900
        
    else:
        dificultad = 'Difícil'
        vidas = 1.0
        pistas = 2
        tiempo = 600
        
    # Lista de objetos conseguidos por el usuario durante el juego
    inventario = []

    user = Jugador(username, contraseña, edad, avatar, inventario, dificultad, vidas, pistas, tiempo)
    
    # Guardar los datos recolectados del usuario en un archivo .txt
    with open('DatosUsuarios.txt','a+') as dataus:
        dataus.write(f'{user.username} - {user.contraseña} - {edad} - {avatar} - {inventario} - {dificultad} - {vidas} - {pistas} - {tiempo} segundos\n')

    tiempo_final = user.tiempo
    status = ''

    user_1 = Estadistica(user.username, user.contraseña, user.edad, user.avatar, user.inventario, user.dificultad, user.vidas, user.pistas, user.tiempo, tiempo_final, status)
    
    with open('DatosEstadisticas.txt', 'a+') as dataes:
        dataes.write(f'Nombre de usuario: {user.username} - Edad: {user.edad} - Avatar: {user.avatar} - Inventario: {user.inventario} - Nivel de Dificultad: {user.dificultad} - Vidas Restantes: {user.vidas} - Pistas Restantes: {user.pistas} - Tiempo Final: {tiempo_final} - Status: {status}\n')


    print('\nUsusario registrado con éxito')
    return user


def main():
    
    #---iMAGENES USADAS EN EL JUEGO DEL AHORCADO
    imagenes = [colored('''
        +---+
        |   |
            |
            |
            |
            |
            =========''','red'), colored('''
        +---+
        |   |
        O   |
            |
            |
            |
            =========''', 'red'), colored('''
        +---+
        |   |
        O   |
        |   |
            |
            |
            =========''','red'), colored('''
        +---+
        |   |
        O   |
       /|   |
            |
            |
            =========''', 'red'), colored('''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =========''', 'red'), colored('''
        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            =========''', 'red'), colored('''
        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
            =========''', 'red'), colored('''
        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            =========''', 'red'), '''
    ''']

    #---PALABRAS USADAS EN EL JUEGO DEL AHORCADO---
    palabras_ahorcado = [
        'metromix', 
        'piscina', 
        'rectorado'
    ]

    #---PREGUNTAS USADAS EN EL JUEGO DE MATEMÁTICA---
    preguntas_matematica = [
        'Calcula la derivada de la función evaluada en pi  f(x)=((sen(x))/2))',
        'Calcula la derivada de la función en pi  f(x)=((cos(x))/2 - (tan(x))/5)',
        'Calcula la derivada de la función en pi  f(x)=((sen(x))/5 - (tan(x)))'
    ]

    #---PALABRAS USADAS EN EL JUEGO DE CRIPTOGRAMA---
    preguntas_criptograma = [
        'qg rc epybsyq ngqyq cj qykál (desplazamiento 2)',
        'wm xi kvehyew tmwew ip weqár (desplazamiento 4)',
        'xn yj lwfizfx unxfx jq xfrás (desplazamiento 5)'
    ]

    #---PREGUNTAS USADAS EN EL JUEGO DE CULTURA UNIMETANA---
    preguntas_unimet = [
        '¿En qué fecha es el Aniversario de la Universidad Metropolitana?',
        '¿En qué año fue Fundada la Universidad Metropolitana?',
        '¿Quién fundó la Unimet?'
    ]

    #---PREGUNTAS USADAS EN EL JUEGO ENCUENTRA LA LÓGICA---
    preguntas_logica = [
        '🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?',
        '🐧+🐧+🐧=27 \n 🐧+🐝+🐝=19 \n 🐝+🐦+🐦=13 \n 🐝x🐧-🐦=?'
    ]

    #---PREGUNTAS USADAS EN EL JUEGO DE LÓGICA BOOLEANA---
    preguntas_booleanas = [
        '¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b)',
        '¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and a) or (b) or (b or a) or (a and not a and not b)'
    ]

    #---MATRICES USADAS EN LA SOPA DE LETRAS---
    matriz_1 = (colored('''
                0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
            0 ['K','F','K','H','G','R','G','Y','C','K','O','Q','Z','L','K'] 
            1 ['T','P','I','L','A','R','C','F','A','K','A','G','G','D','L'] 
            2 ['A','B','V','Q','H','C','G','P','K','L','W','O','C','V','Z'] 
            3 ['N','P','U','L','R','X','I','H','U','F','I','I','B','H','B'] 
            4 ['R','B','W','U','F','A','A','W','K','O','D','D','X','F','U'] 
            5 ['S','C','H','A','R','I','F','K','E','R','W','N','R','V','X'] 
            6 ['K','X','R','M','G','L','I','W','B','X','F','I','V','A','A'] 
            7 ['A','P','Y','K','W','R','X','D','B','V','R','Q','D','I','P'] 
            8 ['H','N','U','F','L','H','Y','H','F','G','R','Z','V','W','U'] 
            9 ['G','K','R','V','V','A','A','D','C','W','B','M','M','N','F'] 
           10 ['L','Y','X','N','B','Q','D','D','W','Z','F','P','I','V','J'] 
           11 ['I','S','T','U','L','U','O','V','M','J','G','L','Q','G','N'] 
           12 ['Q','K','V','D','V','S','L','A','J','H','Y','K','D','E','Q'] 
           13 ['K','K','H','C','R','O','H','T','T','I','V','V','Y','D','E'] 
           14 ['B','K','P','G','V','N','L','F','T','F','W','V','N','U','U']
            
        '''), 'grey')

    matriz_2 = (colored('''
                0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
            0 ['H','K','E','Q','O','T','M','R','J','L','P','R','X','U','F'] 
            1 ['T','E','O','O','A','R','H','Q','X','O','M','D','Q','M','W'] 
            2 ['H','S','A','R','F','F','F','O','V','O','Q','B','Z','N','X'] 
            3 ['H','C','R','X','M','J','A','K','Y','N','L','V','B','Y','L'] 
            4 ['G','S','A','N','X','Z','L','S','A','X','T','L','M','M','E'] 
            5 ['T','G','H','H','H','E','A','M','U','Y','Q','G','E','I','S'] 
            6 ['X','G','B','S','V','W','A','J','F','K','O','Y','I','B','F'] 
            7 ['B','C','X','N','F','G','M','S','N','P','T','V','H','L','H'] 
            8 ['M','H','M','X','A','A','T','L','H','N','F','M','O','V','F'] 
            9 ['X','M','R','D','R','N','U','K','M','K','Z','O','H','Y','R'] 
           10 ['E','H','W','C','A','Y','O','Z','Q','K','K','H','V','U','L'] 
           11 ['L','E','A','C','X','M','H','B','M','Z','P','T','J','H','B'] 
           12 ['X','N','F','S','C','R','C','W','G','O','M','T','R','J','G'] 
           13 ['O','T','Q','E','Y','E','T','U','B','M','L','D','N','Z','C'] 
           14 ['J','I','Y','S','Y','K','B','T','H','X','C','M','F','M','P']
            
        '''), 'grey')
            
    matriz_3 = (colored('''
                0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
            0 ['C','Q','I','P','E','F','I','B','P','Z','D','G','C','Q','O'] 
            1 ['O','N','J','C','G','W','L','Y','Q','V','B','A','R','K','E'] 
            2 ['Z','Z','X','F','G','B','F','T','B','X','B','O','T','A','Z'] 
            3 ['V','V','E','Y','M','O','G','U','M','G','E','X','V','M','Y'] 
            4 ['X','Y','K','V','L','A','G','B','C','E','B','H','N','F','U'] 
            5 ['B','B','S','V','Y','D','E','L','O','M','A','V','S','R','Y'] 
            6 ['G','G','L','G','G','A','E','M','O','X','U','S','J','C','U'] 
            7 ['O','Z','L','G','G','H','Z','N','N','I','J','G','Q','S','S'] 
            8 ['I','J','O','A','T','Z','O','V','R','Y','Z','B','R','Y','Q'] 
            9 ['M','Y','R','L','M','U','T','Y','H','F','Q','D','Z','N','T'] 
           10 ['U','E','A','W','P','A','F','D','P','P','G','E','A','Z','J'] 
           11 ['A','Q','N','X','X','U','G','J','S','X','O','I','S','K','Y'] 
           12 ['J','L','T','H','L','Z','S','A','N','W','B','R','E','M','V'] 
           13 ['R','X','E','S','K','N','Z','W','D','S','A','J','R','R','B'] 
           14 ['Z','Y','P','L','A','Z','A','G','B','Q','P','T','R','D','W']
            
        '''),'grey')

    #---PREGUNTAS USADAS EN EL JUEGO PREGUNTAS SOBRE PTYHON---
    preguntas_python = [
        'tengo en mi cuenta 50,00 $',
        'oidutse ne al ortem aireinegni ed sametsis'
    ]

    #---PREGUNTAS USADAS EN EL JUEGO DE ADIVINANZAS---
    adivinanzas = [
        "Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo?",
        "Es pequeño como una pera, pero alumbra la casa entera. ¿Qué soy yo?",
        "Oro parece y plata no es, y no lo adivinas de aquí a un mes ¿Qué soy yo?"
    ]

    #---PALABRAS USADAS EN EL JUEGO DE PALABRAS MEZCLADAS---
    palabras_cocina = [
        "sarten",
        "paleta",
        "olla",
        "vaso",
        "hornilla"
    ]

    palabras_baño = [
        "poceta",
        "cepillo",
        "afeitadora",
        "regadera",
        "grifo"
    ]

    palabras_baile = [
        "zumba",
        "salsa",
        "flamengo",
        "tango",
        "perreo"
    ]

    #---MENU PRINCIPAL---
    musica()
    while True:
        print(colored('''
        ------------------------------
        1: Crear cuenta
        ------------------------------
        2: Ya tengo una cuenta
        ------------------------------
        3: Ver instrucciones
        ------------------------------
        4: Ver estadísticas
        ------------------------------
        5: Salir
        ------------------------------
        ''', 'green'))
        
        decision_cuenta = int(input('--> '))
        while decision_cuenta != 1 and decision_cuenta != 2 and decision_cuenta != 3 and decision_cuenta != 4 and decision_cuenta != 5:
            print('¡ERROR!')
            decision_cuenta = int(input('--> '))

        if decision_cuenta == 1:
            user = validar_existencia_username()
    
            print("\n")
            print(user.mostrar_jugador())

        #---INICIO DE LA TRAMA DEL JUEGO---
            correr_cronometro = threading.Thread(target=cronometro_1, args=(user, ))
            correr_cronometro.start()

            print('\n')
            print(f'''
            Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
            lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto 
            de redes que tiene toda la información de SAP de estudiantes, pagos y asignaturas. 
            Necesitamos que nos ayudes a recuperar el disco, para eso tienes {user.tiempo} minutos, 
            antes de que el servidor se caiga y no se pueda hacer más nada. 
            ''')

            decision_reto = input('¿Aceptas el reto? [S/N]: ').upper()
            while decision_reto != 'S' and decision_reto != 'N':
                decision_reto = input('¿Aceptas el reto? [S/N]: ').upper()

            if decision_reto == 'S':
                
                print('\n')
                print(f'''
                Bienvenido {user.username}, gracias por tu disposición a ayudarnos a 
                resolver este inconveniente, te encuentras actualmente ubicado en la 
                biblioteca, revisa el menú de opciones para ver qué acciones puedes 
                realizar. Recuerda que el tiempo corre más rápido que un trimestre en 
                este reto.
                ''')

                # sys.exit(cronometro_1(user))

                cuarto_1(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                cuarto_2(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                cuarto_3(user, palabras_ahorcado, imagenes, preguntas_matematica, preguntas_criptograma, preguntas_unimet, preguntas_logica, preguntas_booleanas, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                cuarto_4(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)
                cuarto_5(user, preguntas_python, adivinanzas, matriz_1, matriz_2, matriz_3, palabras_cocina, palabras_baile, palabras_baño)

                print('¡Felicidades! Has logrado evitar una catástrofe en la Unimet')
                sys.exit()
            else:
                print('¿Qué pasó papá, le tienes miedo al éxito?')
        
        elif decision_cuenta == 2:
            print()
            # ver_usuarios()
            # validar_nombre = input('Ingrese su nombre de usuario: ')
            # vun = validar_nombre.split()

            # while True:
            #     if not ("".join(vun)).isalpha():
            #         validar_nombre = input('Ingrese su nombre de usuario: ')
            #         vun = validar_nombre.split()
            #     elif ("".join(vun)).isalpha():
            #         break
            # validar_nombre = validar_nombre.title()

            # validar_contraseña = input('Ingrese su contraseña: ')
            # vcon = validar_contraseña.split()

            # while True:
            #     if not ("".join(vcon)).isalnum():
            #         validar_contraseña = input('Ingrese su contraseña: ')
            #         vvcon = validar_contraseña.split()
            #     elif ("".join(vcon)).isalnum():
            #         break
            
            
            # with open('DatosUsuarios.txt') as dataus:
            #     datos = dataus.readlines()
            #     # print(datos)
            # for dato in datos:
            #     # print(dato)
            #     username_v = dato[:-1].split(" - ")
            #     # print(username_v)
            #     if username_v[0] == validar_nombre and username_v[1] == validar_contraseña:
            #         print('Usuario confirmado con exito')
            #         break
            #     else:
            #         print('Username o contraseña incorrectos')
                    

            #     for i,j in enumerate(username_v):
            #         if i == 0:
            #             if j == validar_nombre:
            #                print('Nombre de usuario valido') 
            #             else:
            #                 print('Nombre de usuario no existe')
            #                 break
                    
            #         if i == 1:
            #             if j == validar_contraseña:
            #                 print('Usuario confirmado con exito')
            #             else:
            #                 print('Contraseña Incorrecta')
            #                 break
        

        elif decision_cuenta == 3:
            print('''
            1.	Crea una cuenta: Para poder llevar un control de tu progreso en el juego, será necesario que te crees una cuenta. 
            En ella deberás ingresar tu nombre de usuario, contraseña, escoger un personaje y el nivel de dificultad del juego. 
            En caso de que ya tengas una cuenta creada, solo tendrás que validar tu nombre de usuario y contraseña, de esta manera 
            podremos comprobar que realmente eres el dueño de la cuenta.
            
            2.	Una vez tengas listas tu cuenta empezará el juego, tendrás un límite de tiempo y un máximo de vidas y pistas para 
            poder resolver todo el juego, esto dependerá del nivel de dificultad que hayas escogido (Fácil: 20 minutos, 5 vidas, 
            5 pistas; Medio: 15 minutos, 3 vidas, 3 pistas; Difícil: 10 minutos, 1 vida, 2 pistas).
            
            3.	Habrá 5 habitaciones en total (Plaza de Rectorado, Biblioteca, Puertas de Laboratorios, Laboratorios y Cuarto de 
            Servidores). En cada habitación hay 3 retos (excepto en las puertas de laboratorios, ahí solo hay uno), por cada victoria 
            recibirás una recompensa las cuales serán necesarias para poder resolver algunos retos; por cada fallo perderás un cierto 
            porcentaje de vida, si llevas a cero (0) GAME OVER. 
            
            4.	Ganas el juego una vez que hayas completado todos los retos y cumplido con tu misión.

            ''')
        
        elif decision_cuenta == 4:
            ver_estadisticas()

        else:
            sys.exit()

        
            

main()


   ︵.︵
  (˛. *˛)
 (˛˛. *。)
 (˛* ˛*˛*)
    |.|



            -------------------------------------PLAZA-----------------------------------
                   ____________________________︵.︵_______________________________
                  /                           (˛. *˛)                             \
                 /  /                        (˛˛. *。)                           \ \
                /  /|                        (˛* ˛*˛*)                           |\ \
               /  /                             |.|                                \ \
              /  /|                                                                |\ \
             /_________________________________________________________________________\