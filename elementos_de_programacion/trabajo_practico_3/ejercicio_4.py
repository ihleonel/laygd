# Solicitar dos números decimales al usuario y evaluar si:

num1 = float(input("Ingrese el primer número decimal: "))
num2 = float(input("Ingrese el segundo número decimal: "))

# ¿Son iguales?
son_iguales = num1 == num2
print(f"¿Los números {num1} y {num2} son iguales? {son_iguales}")

# ¿El primero es mayor que el segundo?
es_mayor = num1 > num2
print(f"¿El número {num1} es mayor que {num2}? {es_mayor}")

# ¿El primero es distinto al segundo?
es_distinto = num1 != num2
print(f"¿El número {num1} es distinto a {num2}? {es_distinto}")

# Finalmente, solicitar un tercer número decimal y evaluar si el primer número es mayor que el
# segundo número y mayor que el tercero número.
num3 = float(input("Ingrese el tercer número decimal: "))
mayor = num1 > num2 and num1 > num3
print(f"¿El número {num1} es mayor que {num2} y mayor que {num3}? {mayor}")

# ¿Qué tipo de operador necesita utilizar para resolverlo?
print("Para resolverlo se necesita utilizar el operador lógico 'and'")
