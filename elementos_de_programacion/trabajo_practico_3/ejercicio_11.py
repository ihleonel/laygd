libro_gr = 500
cuaderno_gr = 200
dibujo_gr = 50

cant_libros_vendidos = int(input("Ingrese cantidad de libros vendidos: "))
cant_libros_cuadernos = int(input("Ingrese cantidad de cuadernos vendidos: "))
cant_libros_dibujos = int(input("Ingrese cantidad de dibujos vendidos: "))

peso_total_gr = (cant_libros_vendidos * libro_gr) + (cant_libros_cuadernos * cuaderno_gr) + (cant_libros_dibujos * dibujo_gr)

peso_total_kg = peso_total_gr / 1000

print(f"El peso total del paquete en kg: {peso_total_kg}")
