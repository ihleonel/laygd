dinero_invertir = float(input("Ingrese el monto a invertir: "))
interes_anual = float(input("Ingrese el interés anual: "))
anios_invertir = int(input("Ingrese la cantidad de años: "))

capital_final = dinero_invertir * (1 + interes_anual) * anios_invertir

print(f"Capital inicial: {dinero_invertir}; Capital final: {capital_final}")
