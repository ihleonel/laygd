peso_auto_gr = 750
peso_muneca_gr = 250

cantidad_autos = int(input("Ingrese la cantidad de autos: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas: "))

peso_total_gr = peso_auto_gr * cantidad_autos + peso_muneca_gr * cantidad_munecas

print(f"Peso total en gramos de última venta: {peso_total_gr}")
