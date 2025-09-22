# Escribir un script que permita ingresar tres números por teclado. Luego, determinar cuál es
# el mayor de los tres. Informar por pantalla con los carteles adecuados.

numero_1 = float(input("Ingrese un primer número: "))
numero_2 = float(input("Ingrese un segundo número: "))
numero_3 = float(input("Ingrese un trecer número: "))

if numero_1 != numero_2 and numero_2 != numero_3:
    if numero_1 > numero_2:
        if numero_1 > numero_3:
            print(f"{numero_1} es el mayor de los tres")
        else:
            print(f"{numero_3} es el mayor de los tres")
    else:
        if numero_2 > numero_3:
            print(f"{numero_2} es el mayor de los tres")
        else:
            print(f"{numero_3} es el mayor de los tres")
else:
    print("Los tres números son iguales")

