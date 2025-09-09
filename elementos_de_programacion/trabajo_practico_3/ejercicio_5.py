# Solicitar al usuario que ingrese dos valores booleanos val1 y val2 (True o False). Luego,
# mostrar por pantalla:

val1 = input("Ingrese el primer valor booleano (True o False): ")
val1 = True if val1 == "True" else False
val2 = input("Ingrese el segundo valor booleano (True o False): ")
val2 = True if val2 == "True" else False

# El resultado de val1 and val2.
val1_and_val2 = val1 and val2
print(f"El resultado de {val1} and {val2} es {val1_and_val2}")

# El resultado de val1 or val2.
val1_or_val2 = val1 or val2
print(f"El resultado de {val1} or {val2} es {val1_or_val2}")

# El resultado de not val1.
not_val1 = not val1
print(f"El resultado de not {val1} es {not_val1}")
