# Escribir un script que permita:
# 1. Definir una lista vacía.
lista_vacia = []
# 2. Definir una lista con tres elementos de igual tipo de dato.
lista_tres_elementos = ['hola', 'mundo', 'python']
# 3. Definir una lista con una cantidad de ceros ingresada por teclado.
cantidad = int(input("Ingrese la cantidad de ceros: "))
lista_ceros = []
for i in range(cantidad):
    lista_ceros.append(0)
