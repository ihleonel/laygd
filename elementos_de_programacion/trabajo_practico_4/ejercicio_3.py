# Escribir un script que permita ingresar un número por teclado. Luego, determinar si el
# número ingresado es par o impar. Informar por pantalla con los carteles adecuados.

numero = float(input("Ingrese un número: "))

if numero % 2 == 0:
    print(f"{numero} es un número par")
else:
    print(f"{numero} es un número impar")
