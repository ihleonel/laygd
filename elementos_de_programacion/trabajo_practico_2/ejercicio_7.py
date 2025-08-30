nombre = input("Ingrese su nombre: ")
cantidad_horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
monto_hora_trabajada = float(input("Ingrese el monto por hora trabajada: "))

salario = cantidad_horas_trabajadas * monto_hora_trabajada

print(f"Estimado {nombre}, su salario a liquidar es de ${salario} pesos.")
