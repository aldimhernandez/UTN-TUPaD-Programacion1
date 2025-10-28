# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 8 - Manejo de Archivos
# Actividades

print("Trabajo Práctico 8 - Manejo de Archivos")

# * 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad.

print("\n------------------------------------------------")
print("\nEjercicio 1: Crear archivo inicial con productos\n")

lineas = ["te_oolong,12.500,10", "te_pu_erh,16.200,20", "te_matcha,15.000,15"]

with open("productos.txt", "w") as archivo:
    for LINEA in lineas:
        archivo.writelines(f"{LINEA}\n")

# * 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("\n------------------------------------------------")
print("Ejercicio 2: Leer y mostrar productos\n")

with open("productos.txt", "r") as archivo:
    for LINEA in archivo:
        nombre, precio, cantidad = LINEA.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# * 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("\n------------------------------------------------")
print("Ejercicio 3: Agregar productos desde teclado\n")

nuevo_producto = input(
    "Ingrese un nuevo producto (nombre,precio,cantidad) separado por comas: "
)
with open("productos.txt", "a") as archivo:
    archivo.writelines(f"{nuevo_producto}\n")

# * 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

print("\n------------------------------------------------")
print("Ejercicio 4: Cargar productos en una lista de diccionarios\n")

productos = []
with open("productos.txt", "r") as archivo:
    for LINEA in archivo:
        nombre, precio, cantidad = LINEA.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad),
        }
        productos.append(producto)
print(productos)

# * 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

print("\n------------------------------------------------")
print("Ejercicio 5: Buscar producto por nombre\n")

nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

EXISTE = False
for producto in productos:
    if producto["nombre"] == nombre_buscar:
        print(
            f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}"
        )
        EXISTE = True
        break
if not EXISTE:
    print("Error: El producto no existe en el inventario.")

# * 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

print("\n------------------------------------------------")
print("Ejercicio 6: Guardar los productos actualizados\n")

with open("productos.txt", "w") as archivo:
    for producto in productos:
        LINEA = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.writelines(LINEA)
print("Archivo productos.txt actualizado con los productos actuales.")
