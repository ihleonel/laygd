# Video explicativo: https://youtu.be/dQw4w9WgXcQ
from random import randint

def obtener_categorias():
    categorias = {}
    archivo = open("data_ia.txt", "r")
    for linea in archivo:
        categoria, elementos = linea.strip().split(":")
        categorias[categoria] = elementos.split(",")
    archivo.close()
    return categorias

def obtener_elemento_aleatorio(lista):
    indice_aleatorio = randint(0, len(lista) - 1)
    return lista[indice_aleatorio]

def generar_perfil_personaje(categorias):
    nombre = input("Ingresa el nombre del personaje: ")
    apellido = input("Ingresa el apellido del personaje: ")

    personaje = {
        "Nombre": nombre,
        "Apellido": apellido,
    }
    for categoria, elementos in categorias.items():
        elemento_seleccionado = obtener_elemento_aleatorio(elementos)
        personaje[categoria] = elemento_seleccionado

    return personaje

def guardar_perfil_personaje(personaje):
    archivo = open("perfil_personaje.txt", "w")
    for clave, valor in personaje.items():
        archivo.write(f"{clave}: {valor}\n")

    archivo.close()

def obtener_perfil_personaje():
    personaje = {}
    archivo = open("perfil_personaje.txt", "r")
    for linea in archivo:
        clave, valor = linea.strip().split(": ")
        personaje[clave] = valor
    archivo.close()
    return personaje

def mostrar_perfil_personaje(personaje):
    print(f"Nombre: {personaje['Nombre']} {personaje['Apellido']}")
    for categoria in ["ocupaciones", "signo zodiacal", "cualidades especiales"]:
        print(f"{categoria}: {personaje[categoria]}")

def principal():
    print("¡Hola! Prepárate para generar un perfil de personaje único.")

    categorias = obtener_categorias()

    personaje = generar_perfil_personaje(categorias)
    guardar_perfil_personaje(personaje)

    print("¡Perfil de personaje generado con éxito!")

    personaje_guardado = obtener_perfil_personaje()
    mostrar_perfil_personaje(personaje_guardado)

if __name__ == "__main__":
    principal()
