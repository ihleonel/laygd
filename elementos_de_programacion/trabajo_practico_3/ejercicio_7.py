# Solicitar al usuario que ingrese una cadena de caracteres (string).
cadena = input("Ingrese una cadena de caracteres: ")

# Mostrar por pantalla con los carteles adecuados:
# ● la cadena ingresada en mayúsculas.
mayusculas = cadena.upper()
print(f"La cadena ingresada en mayúsculas es: {mayusculas}")

# ● la cadena ingresada en minúsculas.
minusculas = cadena.lower()
print(f"La cadena ingresada en minúsculas es: {minusculas}")

# ● la cadena ingresada como título (primera letra de cada palabra en mayúscula).
titulo = cadena.title()
print(f"La cadena ingresada como título es: {titulo}")

# ● la primera letra de la cadena ingresada.
primera_letra = cadena[0]
print(f"La primera letra de la cadena ingresada es: {primera_letra}")

# ● la cantidad de caracteres que tiene la cadena ingresada, es decir su longitud.
longitud = len(cadena)
print(f"La cantidad de caracteres de la cadena ingresada es: {longitud}")
