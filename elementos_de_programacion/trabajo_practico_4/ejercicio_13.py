# Escribir un script que permita ingresar por teclado la cantidad de números que se van a
# procesar. Luego, pedir el ingreso de esos números uno por uno. Al finalizar, mostrar por
# pantalla el mayor y el menor de los números ingresados.

cantidad = int(input("Cantidad de números a solicitar: "))
inicio = 1
mayor = - 10**10
menor = 10**10

while inicio <= cantidad:
    numero = int(input("Ingrese un número: "))
    if numero >= mayor:
        mayor = numero
    if numero <= menor:
        menor = numero

    inicio = inicio + 1

print(f"El mayor de los número ingresado es: {mayor}")
print(f"El menor de los número ingresado es: {menor}")
