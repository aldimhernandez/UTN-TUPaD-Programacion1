# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 7 - Estructuras de datos complejas
# Actividades

print("\nTP 7 - Estructuras de datos complejas")


# Función para indicar el inicio de cada ejercicio
def indicar_inicio_ejercicio(numero, nombre=""):
    print("\n-----------------------------------------------------------------")
    print(f"Ejercicio {numero}: {nombre}\n")


# * 1) Dado el diccionario precios_frutas
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
    # Añadir las siguientes frutas con sus respectivos precios:
    # ● Naranja = 1200
    # ● Manzana = 1500
    # ● Pera = 2300

indicar_inicio_ejercicio(1, "Agregar frutas al diccionario")
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# * 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
    # ● Banana = 1330
    # ● Manzana = 1700
    # ● Melón = 2800

indicar_inicio_ejercicio(2, "Actualizar precios de frutas")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

# * 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

indicar_inicio_ejercicio(3, "Crear lista de frutas")

precios_frutas_key_list = list(precios_frutas.keys())
print(precios_frutas_key_list)

# * 4) Escribí un programa que permita almacenar y consultar números telefónicos.
    # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
    # • Luego, pedí un nombre e imprimí el número asociado, si existe.
        # Ejemplo: contactos = {"Juan": "123456", "Ana": "987654"}
    # Consultar: "Juan" -> Imprime "123456"

indicar_inicio_ejercicio(4, "Agenda telefónica")

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico del contacto: ")
    contactos[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto {nombre_consulta} no existe.")

# * 5) Solicita al usuario una frase e imprime:
    # • Las palabras únicas (usando un set).
    # • Un diccionario con la cantidad de veces que aparece cada palabra.
     # Ejemplo:
        # Entrada: "hola mundo hola"
        # Salida palabras únicas: {"hola", "mundo"}
        # Salida recuento: {"hola": 2, "mundo": 1}

indicar_inicio_ejercicio(5, "Palabras únicas y recuento")

frase = input("Ingrese una frase: ")
palabras_unicas = set(frase.split())
print(f"Palabras únicas: {palabras_unicas}")

recuento_palabras = {}
for palabra in frase.split():
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1
    else:
        recuento_palabras[palabra] = 1
print(f"Recuento de palabras: {recuento_palabras}")

# * 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, imprimí el promedio de cada alumno.
    # Ejemplo: alumnos = {"Sofia": (10, 9, 8), "Luis": (6, 7, 7)}

indicar_inicio_ejercicio(6, "Promedio de notas de alumnos")

alumnos = {}
for i in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre_alumno}: "))
        notas.append(nota)
    alumnos[nombre_alumno] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")

# * 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
    # • Imprimí los que aprobaron ambos parciales.
    # • Imprimí los que aprobaron solo uno de los dos.
    # • Imprimí la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

indicar_inicio_ejercicio(7, "Estudiantes que aprobaron parciales")

parcial_1 = {101, 102, 103, 104}
print(f"Estudiantes que aprobaron Parcial 1: {parcial_1}")
parcial_2 = {103, 104, 105, 106}
print(f"Estudiantes que aprobaron Parcial 2: {parcial_2}")

aprobados_ambos = parcial_1 & parcial_2
print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")

aprobados_solo_uno = parcial_1 ^ parcial_2
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {aprobados_solo_uno}")

aprobados_al_menos_uno = parcial_1 | parcial_2
print(f"Estudiantes que aprobaron al menos un parcial: {aprobados_al_menos_uno}")

# * 8) Crea un diccionario donde las claves sean nombres de productos y los valores su stock.
    # Permití al usuario:
        # • Consultar el stock de un producto ingresado.
        # • Agregar unidades al stock si el producto ya existe.
        # • Agregar un nuevo producto si no existe.

indicar_inicio_ejercicio(8, "Gestión de stock de productos")

stock_productos = {
    "Acrilico_Blanco_16g": 20,
    "Pinceles_set": 15,
    "Lienzos_30x40": 10,
    "Paleta_mezcla": 25,
    "Caballetes": 5,
}

while True:
    eleccion = input("Ingrese 1. Consultar, 2. Agregar o 3. Salir: ") # Menu de opciones
    if eleccion == "3": # Salir del programa
        print("Gracias por usar el sistema de gestión de stock.")
        break
    elif eleccion == "1": # Consultar stock
        input_producto = input("Ingrese el nombre del producto a consultar: ")
        if input_producto in stock_productos: # Producto existe
            print(f"El stock de {input_producto} es: {stock_productos[input_producto]}") # Mostrar stock
        else: # Producto no existe
            print(f"El producto {input_producto} no existe en el stock.") # Notificar al usuario
    elif eleccion == "2": # Agregar o actualizar stock
        input_producto = input("Ingrese el nombre del producto a agregar o actualizar: ") # Nombre del producto
        cantidad = int(input("Ingrese la cantidad a agregar: ")) # Cantidad a agregar
        if input_producto in stock_productos: # Producto existe
            stock_productos[input_producto] += cantidad # Actualizar stock
            print(f"Se han agregado {cantidad} unidades a {input_producto}. Nuevo stock: {stock_productos[input_producto]}")
        else: # Producto no existe
            stock_productos[input_producto] = cantidad # Agregar nuevo producto
            print(f"Se ha agregado un nuevo producto {input_producto} con un stock de {cantidad}.")
    else: # Opción no válida
        print("Opción no valida. Por favor, intente de nuevo.")

# * 9) Crea una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
    # Ejemplo: agenda = {("Lunes", "10:00"): "Reunión",("Martes", "15:00"): "Clase de inglés"}
    # Permití consultar qué actividad hay en cierto día y hora.

indicar_inicio_ejercicio(9, "Agenda de eventos")

agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Miércoles", "12:00"): "Almuerzo",
    ("Jueves", "19:00"): "Taekwondo",
    ("Viernes", "18:00"): "Parcial de programación",
}

dia = input("Ingrese el día del evento a consultar: ")
hora = input("Ingrese la hora del evento a consultar (formato HH:MM): ")

evento = agenda.get((dia, hora), "No hay ningún evento programado en ese día y hora.")
print(f"Evento en {dia} a las {hora}: {evento}")

# * 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
    # • Las capitales sean las claves.
    # • Los países sean los valores.
    # Ejemplo: original = {"Argentina": "Buenos Aires", "Chile": "Santiago"} invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}

indicar_inicio_ejercicio(10, "Invertir diccionario de países y capitales")

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Japón": "Tokio",
    "México": "Ciudad de México",
}

invertido = {capital: pais for pais, capital in original.items()}
print(f"Diccionario original de países y capitales: {original}")
print(f"Diccionario invertido de capitales y países: {invertido}")