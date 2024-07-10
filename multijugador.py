import time

def verificar_ganador(tablero, ficha):
    # Verificar filas
    for fila in tablero:
        for col in range(4):
            if fila[col] == ficha and fila[col + 1] == ficha and fila[col + 2] == ficha and fila[col + 3] == ficha:
                return True

    # Verificar columnas
    for col in range(7):
        for fila in range(3):
            if tablero[fila][col] == ficha and tablero[fila + 1][col] == ficha and tablero[fila + 2][col] == ficha and \
                    tablero[fila + 3][col] == ficha:
                return True

    # Verificar diagonales (de izquierda a derecha)
    for fila in range(3):
        for col in range(4):
            if tablero[fila][col] == ficha and tablero[fila + 1][col + 1] == ficha and tablero[fila + 2][
                col + 2] == ficha and tablero[fila + 3][col + 3] == ficha:
                return True

    # Verificar diagonales (de derecha a izquierda)
    for fila in range(3):
        for col in range(3, 7):
            if tablero[fila][col] == ficha and tablero[fila + 1][col - 1] == ficha and tablero[fila + 2][
                col - 2] == ficha and tablero[fila + 3][col - 3] == ficha:
                return True

    return False

def menu():
    juego = "Cuatro en linea"
    print(f"{juego: ^35}\n")

    print("1) Un jugador\n")
    print("2) Multijugador\n")
    print("3) Juegos realizados\n")
    print("4) Salir del juego\n")

    opcion = input("Opcion: ")
    while True:
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
            break
        else:
            print("Opcion invalida")
            opcion = input("Opcion: ")
    return opcion
def validar_movimiento(movimiento):
    try:
        movimiento = int(movimiento)
        return 1 <= movimiento <= 7
    except ValueError:
        return False


def comenzar_partida():
    jugador_1 = input("Nombre de jugador 1: ")
    jugador_2 = input("Nombre de jugador 2: ")
    limite_columnas = [0, 0, 0, 0, 0, 0, 0]
    tablero = []
    for i in range(6):
        nuevaFila = [" _ "] * 7
        tablero.append(nuevaFila)

    for fila in tablero:
        print("".join(fila))
    estado_juego = "en proceso"
    contador = 0
    movimiento = 1
    while movimiento >= 0 and estado_juego == "en proceso":
        if contador % 2 == 0:
            simbolo = " x "
            turno = jugador_1
        else:
            simbolo = " o "
            turno = jugador_2
        movimiento = input(f"{turno}: ")

        while True:
            if validar_movimiento(movimiento):
                movimiento = int(movimiento) - 1
                if limite_columnas[movimiento] < 6:
                    limite_columnas[movimiento] += 1
                    break
                else:
                    print("Opcion invalida")
                    movimiento = input(f"{turno}: ")

            else:
                print("Opcion invalida")
                movimiento = input(f"{turno}: ")

        for i in range(len(tablero) - 1, -1, -1):
            if tablero[i][movimiento] == " _ ":
                tablero[i][movimiento] = simbolo
                break
        for fila in tablero:
            print("".join(fila))

        contador += 1


        if verificar_ganador(tablero, simbolo):
            print(f"Ganador: {turno}")
            estado_juego = "terminado"
            inputFile = open("partidas.txt", "a")
            inputFile.write(f"{jugador_1} VS {jugador_2} - Ganador: {turno} el ")
            hora = time.strftime("%d/%m/%Y a las %H:%M:%S", time.localtime())
            inputFile.write(f"{hora}\n")
            inputFile.close()
            volver_a_jugar = input("¿Volver a jugar? ")
            if volver_a_jugar.lower().strip() == "no":
                return volver_a_jugar.lower().strip()
    return menu()


def ver_partidas():
    inputFile = open(f"partidas.txt", "r")
    for cadena in inputFile:
        print(cadena, end="")

    regresar = input("¿Regresar al menu? (si o no): ")
    regresar = regresar.lower()
    while regresar != "si" and regresar != "no":
        regresar = input("¿Regresar al menu? (si o no): ")
    if regresar == "si":
        return menu()
    elif regresar == "no":
        exit()


def salir():
    print("Juego terminado")
    exit()
