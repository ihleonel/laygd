cadena = input("Ingresar una palabra o frase: ")
caracter = input("Ingrese un caracter: ")

caracter_en_cadena = caracter in cadena

print(f"¿El caracter '{caracter}' se encuentra en la cadena '{cadena}'? {caracter_en_cadena}")
