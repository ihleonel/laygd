peso_auto_gr = 750
peso_muñeca_gr = 250
costo_envio_kg = 200.00

cantidad_autos = int(input("Ingrese la cantidad de autos: "))
cantidad_muñecas = int(input("Ingrese la cantidad de muñecas: "))

peso_autos_total_gr = peso_auto_gr * cantidad_autos
peso_autos_total_kg = peso_autos_total_gr / 1000
costo_autos_kg = peso_autos_total_kg * costo_envio_kg
peso_muñecas_total_gr = peso_muñeca_gr * cantidad_muñecas
peso_muñecas_total_kg = peso_muñecas_total_gr / 1000
costo_muñecas_kg = peso_muñecas_total_kg * costo_envio_kg

cantidad_total = cantidad_autos + cantidad_muñecas
peso_total_gr = peso_autos_total_gr + peso_muñecas_total_gr
peso_total_kg = peso_total_gr/1000
costo_total_kg = costo_autos_kg + costo_muñecas_kg

print(f"{'Item':<10} {'Cantidad':>10} {'Peso gr.':>10} {'Peso kg.':>10} {'Costo $/kg':>16}")
print("-" * 60)
print(f"{'Auto':<10} {cantidad_autos:>10} {peso_autos_total_gr:>10} {peso_autos_total_kg:>10} {costo_autos_kg:>16}")
print(f"{'Muñeca':<10} {cantidad_muñecas:>10} {peso_muñecas_total_gr:>10} {peso_muñecas_total_kg:>10} {costo_muñecas_kg:>16}")
print("-" * 60)
print(f"{'Totales':<10} {cantidad_total:>10} {peso_total_gr:>10} {peso_total_kg:>10} {costo_total_kg:>16}")
