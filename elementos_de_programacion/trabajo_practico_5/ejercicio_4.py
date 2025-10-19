# Escribir un script que, usando un cartel adecuado, permita mostrar por pantalla la cantidad
# de elementos de una lista ingresada por el usuario. Luego, se debe agregar un elemento a
# la lista y mostrar nuevamente la cantidad de elementos por pantalla, usando un cartel
# adecuado.
lista = []
cantidad_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
for i in range(cantidad_elementos):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    lista.append(elemento)

print(f"La cantidad de elementos en la lista es: {len(lista)}")

nuevo_elemento = input("Ingrese un nuevo elemento para agregar a la lista: ")
lista.append(nuevo_elemento)

print(f"La cantidad de elementos en la lista es: {len(lista)}")
