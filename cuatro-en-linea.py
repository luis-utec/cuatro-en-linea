from modulos import menu, comenzar_partida, ver_partidas, salir

opcion = menu()
while opcion != "no":
    if opcion == "1" or opcion == "si":
        opcion = comenzar_partida()
    elif opcion == "2":
        opcion = ver_partidas()
    elif opcion == "3":
        salir()
