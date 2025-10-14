# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 5 - Listas
# Actividades
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

print("Trabajo Práctico 5 - Listas")

print("\nEjercicio 1\n")

# * 1) Crear una lista con las notas de 10 estudiantes.
## • Mostrar la lista completa.
## • Calcular y mostrar el promedio.
## • Indicar la nota más alta y la más baja.

# Lista de notas de 10 estudiantes
notas = [9, 10, 7, 6, 9, 8, 5, 4, 10, 10]

# Mostrar la lista completa
print(f"Lista de notas: {notas}")

# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print(f"Promedio de notas: {promedio:.2f}")

# Indicar la nota más alta y la más baja
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 2\n")

# * 2) Pedir al usuario que cargue 5 productos en una lista.
## • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
## • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# Lista para almacenar productos
productos = []

# Pedir al usuario que cargue 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente
productos_ordenados = sorted(productos)
print(f"Lista de productos ordenada alfabéticamente: {productos_ordenados}")

# Preguntar al usuario qué producto desea eliminar
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"Producto eliminado. Lista actualizada: {productos}")
else:
    print(f"El producto no se encuentra en la lista: {producto_a_eliminar}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 3\n")

# * 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
## • Crear una lista con los pares y otra con los impares.
## • Mostrar cuántos números tiene cada lista.

# Importar el módulo random para generar números al azar
import random

# Generar una lista con 15 números enteros al azar entre 1 y 100
numbers = [random.randint(1, 100) for _ in range(15)]

# Crear listas para pares e impares
pares = [num for num in numbers if num % 2 == 0]
impares = [num for num in numbers if num % 2 != 0]

# Mostrar cuántos números tiene cada lista
print(f"Números generados: {numbers}")
print(f"Lista de números pares: {pares}")
print(f"Cantidad de números pares: {len(pares)}")
print(f"Lista de números impares: {impares}")
print(f"Cantidad de números impares: {len(impares)}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 4\n")

# * 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
## • Crear una nueva lista sin elementos repetidos.
## • Mostrar el resultado.

# Lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crear una nueva lista sin elementos repetidos
datos_sin_repetidos = list(set(datos))

# Mostrar el resultado
print(f"Lista original: {datos}")
print(f"Lista sin elementos repetidos: {datos_sin_repetidos}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 5\n")

# * 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
## • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
## • Mostrar la lista final actualizada.

# Lista de estudiantes presentes en clase
estudiantes = [
    "Aldana",
    "María",
    "Julio",
    "Eduardo",
    "Emanuel",
    "Ricardo",
    "Gimena",
    "Belén",
]

print(f"Lista inicial de estudiantes: {estudiantes}")

# Preguntar al usuario si quiere agregar o eliminar un estudiante
choice = input(
    "¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)?"
).upper()
if choice == "A":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante agregado: {nuevo_estudiante}")
elif choice == "E":
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print(f"Estudiante eliminado: {estudiante_a_eliminar}")
    else:
        print(f"El estudiante no se encuentra en la lista: {estudiante_a_eliminar}")
else:
    print(f"Acción no válida: {choice}")

# Mostrar la lista final actualizada
print(f"Lista final de estudiantes: {estudiantes}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 6\n")

# * 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

# Lista con 7 números
lista_siete_numeros = [9, 79, 44, 28, 17, 15, 23]

print(f"Lista original: {lista_siete_numeros}")

# Rotar los elementos una posición hacia la derecha
# Eliminar el último elemento
ultimo_elemento = lista_siete_numeros.pop()
# Insertar el último elemento al inicio
lista_siete_numeros.insert(0, ultimo_elemento)
print(f"Lista rotada hacia la derecha: {lista_siete_numeros}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 7\n")

# * 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
## • Calcular el promedio de las mínimas y el de las máximas.
## • Mostrar en qué día se registró la mayor amplitud térmica.

# Matriz de 7x2 con temperaturas mínimas y máximas
temperaturas = [[1, 8], [3, 10], [5, 12], [2, 9], [0, 7], [4, 11], [6, 13]]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Mostrar las temperaturas por cada día de la semana
for i, (temp_min, temp_max) in enumerate(temperaturas):
    print(f"{dias_semana[i]}: Mínima = {temp_min}, Máxima = {temp_max}")

# Calcular el promedio de las mínimas y el de las máximas
suma_min = sum(temp[0] for temp in temperaturas)
suma_max = sum(temp[1] for temp in temperaturas)
promedio_min = suma_min / 7
promedio_max = suma_max / 7
print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")

# Mostrar en qué día se registró la mayor amplitud térmica
mayor_amplitud = 0
dia_mayor_amplitud = 0

for i, (temp_min, temp_max) in enumerate(temperaturas):
    amplitud = temp_max - temp_min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

print(
    f"Día con mayor amplitud térmica: Día {dia_mayor_amplitud} con una amplitud de {mayor_amplitud}"
)

print("------------------------------------------------------------------------------")

print("\nEjercicio 8\n")

# * 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
## • Mostrar el promedio de cada estudiante.
## • Mostrar el promedio de cada materia.

# Matriz con las notas de 5 estudiantes en 3 materias
notas_estudiantes = [[10, 10, 10], [10, 8, 9], [10, 7, 10], [9, 5, 10], [7, 9, 8]]

# Mostrar el promedio de cada estudiante
for i, notas in enumerate(notas_estudiantes):
    promedio_estudiante = sum(notas) / len(notas)
    print(f"Promedio del estudiante {i + 1}: {promedio_estudiante:.2f}")

# Mostrar el promedio de cada materia
for j in range(3):
    suma_materia = sum(notas_estudiantes[i][j] for i in range(5))
    promedio_materia = suma_materia / 5
    print(f"Promedio de la materia {j + 1}: {promedio_materia:.2f}")

print("------------------------------------------------------------------------------")

print("\nEjercicio 9\n")

# * 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
## • Inicializar con guiones "-" representando casillas vacías.
## • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
## • Mostrar el tablero después de cada jugada.

# Inicializar el tablero de Ta-Te-Ti con guiones "-"
tablero = [["-" for _ in range(3)] for _ in range(3)];

# Lista de jugadores
jugadores = ["X", "O"]

# Bucle para permitir que los jugadores ingresen posiciones
turno = 0
while True:
    # Mostrar el tablero
    for fila in tablero:
        print(" | ".join(fila))
    print()

    # Determinar el jugador actual
    jugador_actual = jugadores[turno % 2] # Alterna entre "X" y "O"
    # Pedir al jugador que ingrese la fila.
    fila = int(input(f"Jugador {jugador_actual}, ingrese la fila (1-3): ")) - 1 # Restar 1 para ajustar al índice de la lista
    # Pedir al jugador que ingrese la columna.
    columna = int(input(f"Jugador {jugador_actual}, ingrese la columna (1-3): ")) - 1

    # Verificar si la posición está vacía
    if tablero[fila][columna] == "-":
        # Colocar la marca del jugador en la posición indicada
        tablero[fila][columna] = jugador_actual

        # Verificar si hay un ganador (filas, columnas y diagonales)
        ganador = None
        for i in range(3):
            # Verificar filas
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
                ganador = tablero[i][0]
                break
            # Verificar columnas
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
                ganador = tablero[0][i]
                break
        # Verificar diagonales
        if not ganador:
            # Verificar diagonal de izquierda a derecha
            if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
                ganador = tablero[0][0]
            # Verificar diagonal de derecha a izquierda
            elif tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
                ganador = tablero[0][2]

        if ganador:
            # Mostrar el tablero final
            for fila in tablero:
                print(" | ".join(fila))
            print()
            print(f"¡Ha ganado el jugador {ganador}!")
            break

        # Cambiar de turno
        turno += 1
        # Verificar si hay empate
        if turno == 9:
            # Mostrar el tablero final
            for fila in tablero:
                print(" | ".join(fila))
            print()
            print("¡Empataron!")
            break
    else:
        # Mensaje para indicar que la casilla está ocupada
        print("Casilla ocupada. Intente de nuevo.")

print("------------------------------------------------------------------------------")

print("\nEjercicio 10\n")

# * 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
## • Mostrar el total vendido por cada producto.
## • Mostrar el día con mayores ventas totales.
## • Indicar cuál fue el producto más vendido en la semana.

# Matriz de 4x7 con las ventas de 4 productos durante 7 días
ventas = [
    [5, 2, 2, 2, 3, 7, 8],
    [2, 4, 6, 8, 10, 12, 14],
    [11, 12, 1, 13, 1, 16, 18],
    [1, 5, 8, 5, 9, 3, 2],
]

# Mostrar el total vendido por cada producto
for i, producto in enumerate(ventas):
    total_producto = sum(producto)
    print(f"Total vendido del producto {i + 1}: {total_producto}")

# Mostrar el día con mayores ventas totales
ventas_diarias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_mayores_ventas = ventas_diarias.index(max(ventas_diarias)) + 1
print(
    f"Día con mayores ventas totales: Día {dia_mayores_ventas} con ventas de {max(ventas_diarias)}"
)

# Indicar cuál fue el producto más vendido en la semana
total_ventas_productos = [sum(producto) for producto in ventas]
producto_mas_vendido = total_ventas_productos.index(max(total_ventas_productos)) + 1
print(
    f"Producto más vendido en la semana: Producto {producto_mas_vendido} con ventas de {max(total_ventas_productos)}"
)

print("------------------------------------------------------------------------------")
