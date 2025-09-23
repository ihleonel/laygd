# Escribir un script que permita ingresar un número por teclado. Luego, debe mostrar por
# pantalla, los números pares comenzando desde 0 hasta el número ingresado.

numero = int(input("Ingresar un número entero: "))
valor = 0

print(f"Números pares entre {valor} y {numero}")

while valor <= numero:
    if valor % 2 == 0:
        print(f"- {valor}")
    valor = valor + 1
