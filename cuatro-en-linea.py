from multijugador import menu, comenzar_partida, ver_partidas, salir
from un_jugador import comenzar_partida_contra_computadora

opcion = menu()
while opcion != "no":
    if opcion == "1" or opcion == "si":
        opcion = comenzar_partida_contra_computadora()
    elif opcion == "2":
        opcion = comenzar_partida()
    elif opcion == "3":
        opcion = ver_partidas()
    elif opcion == "4":
        salir()
