import time
from multijugador import verificar_ganador, validar_movimiento, menu

def movimiento_computadora(tablero, limite_columnas, ficha_computadora, ficha_jugador):
    # Verificar si la computadora puede ganar en el siguiente movimiento
    for col in range(7):
        if limite_columnas[col] < 6:
            tablero_temporal = [fila[:] for fila in tablero]
            for fila in range(5, -1, -1):
                if tablero_temporal[fila][col] == " _ ":
                    tablero_temporal[fila][col] = ficha_computadora
                    break
            if verificar_ganador(tablero_temporal, ficha_computadora):
                return col

    # Verificar si el jugador puede ganar en el siguiente movimiento y bloquearlo
    for col in range(7):
        if limite_columnas[col] < 6:
            tablero_temporal = [fila[:] for fila in tablero]
            for fila in range(5, -1, -1):
                if tablero_temporal[fila][col] == " _ ":
                    tablero_temporal[fila][col] = ficha_jugador
                    break
            if verificar_ganador(tablero_temporal, ficha_jugador):
                return col

    # De lo contrario, escoger la primera columna disponible
    for col in range(7):
        if limite_columnas[col] < 6:
            return col

def comenzar_partida_contra_computadora():
    jugador_1 = input("Nombre de jugador 1: ")
    jugador_2 = "Computadora"
    limite_columnas = [0, 0, 0, 0, 0, 0, 0]
    tablero = []
    for i in range(6):
        nuevaFila = [" _ "] * 7
        tablero.append(nuevaFila)

    for fila in tablero:
        print("".join(fila))
    estado_juego = "en proceso"
    contador = 0
    while estado_juego == "en proceso":
        if contador % 2 == 0:
            simbolo = " x "
            turno = jugador_1
            movimiento = input(f"{turno}: ")
            while not validar_movimiento(movimiento) or limite_columnas[int(movimiento) - 1] >= 6:
                print("Opción inválida")
                movimiento = input(f"{turno}: ")
            movimiento = int(movimiento) - 1
        else:
            simbolo = " o "
            turno = jugador_2
            movimiento = movimiento_computadora(tablero, limite_columnas, " o ", " x ")
            print(f"{jugador_2}: {movimiento + 1}")

        limite_columnas[movimiento] += 1
        for i in range(len(tablero) - 1, -1, -1):
            if tablero[i][movimiento] == " _ ":
                tablero[i][movimiento] = simbolo
                break

        for fila in tablero:
            print("".join(fila))

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
        contador += 1

    return menu()
