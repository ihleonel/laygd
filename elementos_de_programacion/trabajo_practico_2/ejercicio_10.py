cantidad_dinero = float(input("Ingrese la cantidad de dinero: "))
porcentaje = float(input("Ingrese el porcentaje: "))

porcentaje_dinero = cantidad_dinero * porcentaje / 100

print(f"Monto ingresado: ${cantidad_dinero} * {porcentaje}% = ${porcentaje_dinero}")
