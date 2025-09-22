# Escribir un script que permita ingresar una nota (0-10) por teclado. Luego, determinar si
# dicha nota es Insuficiente (0-4), Suficiente (5-6), Satisfactoria (7), Notable (8-9),
# Sobresaliente (10). Informar por pantalla con los carteles adecuados.

nota = int(input("Ingrese una nota (0 - 10): "))
if nota >= 10:
    print('Sobresaliente')
elif nota >= 8:
    print('Notable')
elif nota >= 7:
    print('Satisfactoria')
elif nota >= 5:
    print('Suficiente')
else:
    print('Insuficiente')
