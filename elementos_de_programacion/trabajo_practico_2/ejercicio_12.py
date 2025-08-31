peso_auto_gr = 750
peso_muñeca_gr = 250

cantidad_autos = int(input("Ingrese la cantidad de autos: "))
cantidad_muñecas = int(input("Ingrese la cantidad de muñecas: "))

peso_autos_total_gr = peso_auto_gr * cantidad_autos
peso_muñecas_total_gr = peso_muñeca_gr * cantidad_muñecas

peso_total_gr = peso_autos_total_gr + peso_muñecas_total_gr

print(f"{'Item':<9}", f"{'Cantidad':<9}", f"{'Total gr.':<10}", f"{'Total kg.':<10}")
print("-" * 40)
print(f"{'Auto':<9}", f"{cantidad_autos:>8}", f"{peso_autos_total_gr:>10}", f"{peso_autos_total_gr/1000:>10}")
print(f"{'Muñeca':<9}", f"{cantidad_muñecas:>8}", f"{peso_muñecas_total_gr:>10}", f"{peso_muñecas_total_gr/1000:>10}")
print("-" * 40)
print(f"{'Totales':<9}", f"{cantidad_autos + cantidad_muñecas:>8}", f"{peso_total_gr:>10}", f"{peso_total_gr/1000:>10}")
