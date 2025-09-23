# Escribir un script que permita ingresar por teclado: el nombre de dos equipos y la cantidad
# de goles que ha hecho cada uno en un partido entre ambos. Luego, informar por pantalla el
# nombre del equipo ganador o bien el nombre de ambos equipos, en caso de empate.

nombre_equipo_1 = input("Ingrese el nombre del primer equipo: ")
goles_equipo_1 = int(input("Ingrese la cantidad de goles del primer equipo: "))
nombre_equipo_2 = input("Ingrese el nombre del segundo equipo: ")
goles_equipo_2 = int(input("Ingrese la cantidad de goles del segundo equipo: "))

if goles_equipo_1 > goles_equipo_2:
    print(f"El equipo '{nombre_equipo_1}' fue el ganador")
elif goles_equipo_2 > goles_equipo_1:
    print(f"El equipo '{nombre_equipo_2}' fue el ganador")
else:
    print(f"Los equipos '{nombre_equipo_1}' y '{nombre_equipo_2}' empataron")
