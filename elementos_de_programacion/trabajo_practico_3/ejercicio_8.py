año_actual = 2025

nombre_apellido = input('Ingrese su nombre y apellido: ')
año_nacimiento = int(input('Ingrese su año de nacimiento: '))
altura_mt = float(input('Ingrese su altura en metros: '))

edad = año_actual - año_nacimiento
altura_cm = altura_mt * 100

print(f"Nombre y apellido: {nombre_apellido.upper()}")
print(f"Edad: {edad}")
print(f"Altura: {altura_cm}cm")
