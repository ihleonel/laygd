# Modifica la calculadora del Ejercicio 6 para que funcione de forma continua. En lugar de
# hacer un solo cálculo y terminar, el programa debe: pedirle al usuario los números y el
# operador. Luego de mostrar el resultado, debe volver a empezar, preguntando por un nuevo
# cálculo. El programa solo debe finalizar cuando el usuario decida salir, por ejemplo,
# escribiendo la palabra 'salir' en lugar de un operador


while True:

    operador = input("Ingrese un operador (+, -, *, /) o 'salir' para terminar: ")
    if operador == 'salir':
        break

    numero_1 = int(input("Ingrese un número entero: "))
    numero_2 = int(input("Ingrese otro número entero: "))

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

    print("_" * 30)
