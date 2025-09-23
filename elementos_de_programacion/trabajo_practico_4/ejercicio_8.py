# Escribir un script que permita ingresar la edad de una persona (1-100) por teclado. Luego,
# determinar si dicha persona es NIÑO (1-12), ADOLESCENTE (13-17), JOVEN (18-30), ADULTO
# (31-65) ADULTO MAYOR (>65) Informar por pantalla usando el formato adecuado.

edad = int(input("Ingrese una edad (1-100): "))
if edad > 65:
    categoria = "ADULTO MAYOR"
elif edad > 30:
    categoria = "ADULTO"
elif edad > 17:
    categoria = "JOVEN"
elif edad > 12:
    categoria = "ADOLESCENTE"
else:
    categoria = "NIÑO"

print(f"La persona es un {categoria}")
