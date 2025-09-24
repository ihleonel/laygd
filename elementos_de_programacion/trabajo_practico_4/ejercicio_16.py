# Incorporar más operaciones con string al código que se presenta en la Figura 4.10 (sección
# 6.1 del Documento Base de la Unidad 4). Para verificar su correcto funcionamiento, se
# deberán realizar al menos tres ejecuciones.

cadena = input("Ingresá una cadena de texto: ")

while True:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Verificar si un carácter está en la cadena")
    print("2. Obtener la longitud de la cadena")
    print("3. Obtener la cantidad de vocales en la cadena")
    print("4. Obtener la cantidad de consonantes en la cadena")
    print("5. Salir del programa")
    print("------------------------------")

    opcion = input("Elegí una opción (1-5): ")

    # Usamos un bloque if/elif/else para manejar las opciones
    if opcion == '1':
        caracter = input("Ingresá el carácter a buscar: ")
        # El operador 'in' es muy útil para saber si un elemento está en un string
        if caracter in cadena:
            print(f"El carácter '{caracter}' SÍ está en la cadena.")
        else:
            print(f"El carácter '{caracter}' NO está en la cadena.")
    elif opcion == '2':
        # La función len() devuelve la longitud de una cadena
        longitud = len(cadena)
        print(f"La longitud de la cadena es: {longitud} caracteres.")
    elif opcion == '3':
        vocales = 'aeiou'
        cantidad_vocales = 0
        for letra in cadena.lower():
            if letra in vocales:
                cantidad_vocales = cantidad_vocales + 1
            if letra in consonantes:
                cantidad_consonantes = cantidad_consonantes + 1

        print(f"Cantidad de vocales: {cantidad_vocales}")

    elif opcion == '4':
        consonantes = 'bcdfghjklmnñpqrstvwxyz'
        cantidad_consonantes = 0
        for letra in cadena.lower():
            if letra in consonantes:
                cantidad_consonantes = cantidad_consonantes + 1
        print(f"Cantidad de consonantes: {cantidad_consonantes}")

    elif opcion == '5':
        print("¡Gracias por usar el programa! Hasta pronto.")
        break  # El comando 'break' finaliza el bucle y el programa
    else:
        print("Opción no válida. Por favor, elegí un número del 1 al 3.")
