# Escribir un script que permita ingresar por teclado dos números enteros Luego, debe
# mostrar por pantalla todos aquellos números que se encuentren entre el primer número
# ingresado y el segundo número ingresado, y qué además sean divisibles por 7


numero_1 = int(input("Ingresar un número entero: "))
numero_2 = int(input("Ingresar otro número entero: "))

paso = 1
if numero_1 > numero_2:
    paso = -1

valor = numero_1

while valor != numero_2:
    if valor % 7 == 0:
        print(f"- {valor}")
    valor = valor + paso

if valor % 7 == 0:
    print(f"- {valor}")
