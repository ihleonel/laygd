# Escribir un script que permita ingresar por teclado un número natural. Luego, se debe
# mostrar por pantalla la suma de los primeros números naturales hasta el número natural
# ingresado.

numero = int(input("Ingresar un número natural: "))
valor = 1
suma = 0

while valor <= numero:
    suma = suma + valor
    valor = valor + 1

print(f"La suma de los primeros números naturales hasta el {numero} es: {suma}")

