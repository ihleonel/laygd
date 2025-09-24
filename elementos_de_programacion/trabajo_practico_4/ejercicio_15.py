# Escribir un script que permita ingresar por teclado un string. Luego, se debe calcular y
# mostrar por pantalla la cantidad de vocales y la cantidad de consonantes que tiene dicho
# string. Importante: contar indistintamente minúsculas y mayúsculas.

cadena = input("Ingrese una cadena de texto: ")
vocales = 'aeiou'
consonantes = 'bcdfghjklmnñpqrstvwxyz'
cantidad_vocales = 0
cantidad_consonantes = 0

for letra in cadena.lower():
    if letra in vocales:
        cantidad_vocales = cantidad_vocales + 1
    if letra in consonantes:
        cantidad_consonantes = cantidad_consonantes + 1

print(f"Cantidad de vocales: {cantidad_vocales}")
print(f"Cantidad de consonantes: {cantidad_consonantes}")
