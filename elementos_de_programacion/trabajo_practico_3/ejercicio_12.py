# Escribe un programa que calcule el promedio de tres notas
# de un estudiante y debe determinar si aprueba.

nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))

promedio = (nota_1 + nota_2 + nota_3) / 3
print(f"El promedio de las notas es: {promedio}")

condicion = promedio >= 7
print(f"¿El estudiante ha aprobado? {condicion}")
