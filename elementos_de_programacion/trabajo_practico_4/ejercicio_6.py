# Escribir un script que permita implementar una calculadora simple. Se debe solicitar por
# teclado, el ingreso de dos números enteros y un operador (+, -, *, /). Luego, realizar el
# cálculo correspondiente e informar por pantalla con los carteles adecuados. En el caso de la
# división, es importante controlar la división por cero.

numero_1 = int(input("Ingrese un número entero: "))
numero_2 = int(input("Ingrese otro número entero: "))
operador = input("Ingrese un operador (+, -, *, /): ")


if operador == '+':
    suma = numero_1 + numero_2
    print(f"Suma: {numero_1} + {numero_2} = {suma}")
elif operador == '-':
    resta = numero_1 - numero_2
    print(f"Resta: {numero_1} - {numero_2} = {resta}")
elif operador == '*':
    producto = numero_1 * numero_2
    print(f"Producto: {numero_1} * {numero_2} = {producto}")
elif operador == '/':
    if numero_2 == 0:
        print("No es posible la division por cero.")
    else:
        cociente = numero_1 / numero_2
        print(f"Cociente: {numero_1} / {numero_2} = {cociente}")
