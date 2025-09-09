# Solicitar al usuario un número entero y convertirlo a real (float).
numero_entero = int(input("Ingrese un número entero: "))
numero_real = float(numero_entero)
print(f"El número entero {numero_entero} convertido a real (float) es {numero_real}")

# Solicitar al usuario un número real (float) y convertirlo a entero.
numero_real = float(input("Ingrese un número real (float): "))
numero_entero = int(numero_real)
print(f"El número real {numero_real} convertido a entero es {numero_entero}")

# Ingresar por teclado un número entero usando la función input(). Convertir el
# valor ingresado a entero y realizar alguna operación aritmética.
numero = input("Ingrese un número entero: ")
numero_convertido = int(numero)
resultado = numero_convertido * 2
print(f"El número original es {numero_convertido} el número convertido es {numero_convertido}")
print(f"El doble del número {numero_convertido} es {resultado}")


# Ingresar por teclado un número real usando la función input(). Convertir el valor
# ingresado a float y realizar alguna operación aritmética.
numero = input("Ingrese un número real (float): ")
numero_convertido = float(numero)
resultado = numero_convertido / 2
print(f"El número original es {numero_convertido} el número convertido es {numero_convertido}")
print(f"La mitad del número {numero_convertido} es {resultado}")
