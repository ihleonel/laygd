# Utilizar con cadenas de texto (str).
# Para cada operador o función, indicar
# qué hace, dar un ejemplo de
# uso claro y el resultado esperado.

# Operador: *

# ¿Que hace?
# El operador * nos permite repetir una cadenas.
# Si multiplicamos una cadena por un número entero,
# el resultado es la repetición de ese texto
print("Operador: *")
# Ejemplo
cadena = "Cadena"
cantidad_repeticiones = 4
print(f"Ejemplo: '{cadena}' * {cantidad_repeticiones}")
# Resultado
print(f"Resultado: {cadena * cantidad_repeticiones}")


# Operador: +

# ¿Que hace?
# El operador + permite unir o concatenar dos o más cadenas.
print("Operador: +")
# Ejemplo
cadena_1 = "Hola"
cadena_2 = "mundo"
print(f"Ejemplo: '{cadena_1}' + '{cadena_2}'")
# Resultado
print(f"Resultado: {cadena_1 + cadena_2}")

# Operador: ==

# ¿Que hace?
# El operador == sirve para comparar si dos cadenas son iguales.
# Devuelve un valor booleano (True o False)
print("Operador: ==")
# Ejemplo
cadena_1 = "Hola"
cadena_2 = "mundo"
print(f"Ejemplo: '{cadena_1}' == '{cadena_2}'")
# Resultado
print(f"Resultado: {cadena_1 == cadena_2}")


# Operador: in

# ¿Que hace?
# El operador in sirve para determinar
# si una cadena contiene a otra.
# Devuelve un valor booleano (True o False)
print("Operador: in")
# Ejemplo
cadena_1 = "Hola"
cadena_2 = "Hola, mundo"
print(f"Ejemplo: '{cadena_1}' in '{cadena_2}'")
# Resultado
print(f"Resultado: {cadena_1 in cadena_2}")


# Funcion: len()

# ¿Que hace?
# La función len() te da la longitud de una cadena.
# Retorna un int
print("Función: len()")
# Ejemplo
cadena_1 = "Hola"
print(f"Ejemplo: len('{cadena_1}')")
# Resultado
print(f"Resultado: {len(cadena_1)}")


# Operador: []

# ¿Que hace?
# El operador [] devulve el caracter de una cadena.
# Retorna el caracter (str) en el numero de posición dado.
# El O (cero) es la primera posición.
print("Operador: []")
# Ejemplo
cadena_1 = "Cadena"
print(f"Ejemplo: '{cadena_1}'[0]")
# Resultado
print(f"Resultado: '{cadena_1[0]}'")
