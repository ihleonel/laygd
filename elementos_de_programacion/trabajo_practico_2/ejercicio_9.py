monto_pesos = float(input("Ingrese el monto en pesos: "))
cotizacion_dolar = float(input("Ingrese la cotizacion en dolares: "))

monto_dolares = monto_pesos / cotizacion_dolar

print(f"Monto en dolares: {monto_dolares}")
