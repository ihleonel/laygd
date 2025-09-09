# Solicitar dos números enteros al usuario. Realizar las siguientes operaciones aritméticas:
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Módulo (resto).
modulo = num1 % num2
print(f"El módulo (resto) de {num1} % {num2} es {modulo}")

# Potencia.
potencia = num1 ** num2
print(f"La potencia de {num1} elevado {num2} es {potencia}")

# División entera.
division_entera = num1 // num2
print(f"La división entera de {num1} // {num2} es {division_entera}")
