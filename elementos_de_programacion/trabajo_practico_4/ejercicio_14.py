# Escribir un script que permita ingresar números enteros positivos por teclado, hasta que el
# usuario ingrese -1. Luego, se debe calcular y mostrar por pantalla el promedio de los
# números ingresados.

suma = 0
cantidad = 0
while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero == -1:
        break

    suma = suma + numero
    cantidad = cantidad + 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron valores a promediar.")
