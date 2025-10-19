lista_ej_2 = [21, "Aula", 7.3, 230, "clase", 8.75, 65, "LECCION", 3.1]

# Luego, se pide recuperar y mostrar con carteles adecuados:
# 1. El número 65.
print("El elemento esta en la posicion 6:", lista_ej_2[6])
# 2. El string “LECCION”.
print("El elemento esta en la posicion 7:", lista_ej_2[7])
# 3. Los elementos “clase”,8.75.
print("Los elementos 'clase' y 8.75 estan en las posiciones 4 y 5:", lista_ej_2[4], lista_ej_2[5])
# 4. Todos los strings.
print("Todos los strings son:")
for elemento in lista_ej_2:
    if type(elemento) == str:
        print(elemento)
# 5. Todos los flotantes.
print("Todos los flotantes son:")
for elemento in lista_ej_2:
    if type(elemento) == float:
        print(elemento)
# 6. Todos los enteros.
print("Todos los enteros son:")
for elemento in lista_ej_2:
    if type(elemento) == int:
        print(elemento)
