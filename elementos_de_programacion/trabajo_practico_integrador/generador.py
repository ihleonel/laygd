# Video explicativo: https://youtu.be/dQw4w9WgXcQ
# Trabajo practico integrador
# Integrantes: Ibarra Hector Leonel

from random import randint

# Obtener categorias del archivo data_ia.txt
def obtener_categorias():
    categorias = {}
    archivo = open("data_ia.txt", "r")
    for linea in archivo:
        categoria, elementos = linea.strip().split(":")
        categorias[categoria] = elementos.split(",")
    archivo.close()
    return categorias

# Obtener un elemento aleatorio de una lista pasada por parametro
def obtener_elemento_aleatorio(lista):
    indice_aleatorio = randint(0, len(lista) - 1)
    return lista[indice_aleatorio]

# Generar perfil del personaje
def generar_perfil_personaje(categorias):
    nombre = input("Ingresa el nombre del personaje: ").capitalize()
    apellido = input("Ingresa el apellido del personaje: ").capitalize()

    personaje = {
        "nombre": f"{nombre} {apellido}",
        "categorias": [],
    }
    for categoria, elementos in categorias.items():
        elemento_seleccionado = obtener_elemento_aleatorio(elementos)
        personaje["categorias"].append(f"{categoria}: {elemento_seleccionado}")

    return personaje

# Guardar datos generados del perfil en el archivo perfil_personaje.txt
def guardar_perfil_personaje(personaje):
    archivo = open("perfil_personaje.txt", "w")
    archivo.write(f"nombre={personaje['nombre']}\n")
    archivo.write("categorias=")
    for categoria in personaje['categorias']:
        archivo.write(f"{categoria.strip()},")
    archivo.close()

# Obtener datos del perfil del personaje guardado en el archivo perfil_personaje.txt
def obtener_perfil_personaje():
    personaje = {}
    archivo = open("perfil_personaje.txt", "r")
    for linea in archivo:
        clave, valor = linea.strip().split('=')
        personaje[clave] = valor.strip()
        if clave == 'categorias':
            personaje[clave] = valor.strip().split(',')

    archivo.close()
    return personaje

# Mostrar por pantalla perfil del personaje guardado
def mostrar_perfil_personaje(personaje):
    print(f"Nombre: {personaje['nombre']}")
    for categoria in personaje['categorias']:
        print(categoria)

# Función principal que ejecuta el programa
def principal():
    print("==========================================================")
    print("¡Hola! Prepárate para generar un perfil de personaje único.")
    print("==========================================================")

    categorias = obtener_categorias()

    personaje = generar_perfil_personaje(categorias)
    guardar_perfil_personaje(personaje)
    print("==========================================================")
    print("¡Perfil de personaje generado con éxito!")
    print("==========================================================")

    personaje_guardado = obtener_perfil_personaje()
    print("===============Perfil del personaje=======================")
    mostrar_perfil_personaje(personaje_guardado)
    print("==========================================================")

# Llamada a la función principal para ejecutar el programa
principal()
