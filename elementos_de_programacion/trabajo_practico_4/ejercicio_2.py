# Escribir un script que permita ingresar un número por teclado. Luego, verificar si el número
# ingresado es positivo, negativo o cero. Informar por pantalla con los carteles adecuados

numero = float(input("Ingrese un número:"))

if numero > 0:
    print(f"{numero} es un numero positivo")
elif numero < 0:
    print(f"{numero} es un numero negativo")
else:
    print(f"{numero} es cero")
