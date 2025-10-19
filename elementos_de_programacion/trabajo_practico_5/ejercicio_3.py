# Escribir un script que permita ingresar seis números enteros por teclado y los almacene en
# una lista. Luego, mostrar usando un cartel adecuado, sólo los números pares.

lista_numeros = []
for i in range(6):
    numero = int(input(f"Ingrese el número entero {i+1}: "))
    lista_numeros.append(numero)

print("Los números pares son:")
for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)
