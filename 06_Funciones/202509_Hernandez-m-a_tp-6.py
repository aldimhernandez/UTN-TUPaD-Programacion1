# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 6 - Funciones
# Actividades

#* 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

print("------------------------------------------------------------------------------")
print("\nEjercicio 1 - Hola Mundo\n")

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#* 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

print("------------------------------------------------------------------------------")
print("\nEjercicio 2 - Saludar Usuario\n")

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

#* 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

print("------------------------------------------------------------------------------")
print("\nEjercicio 3 - Información Personal\n")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#* 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

print("------------------------------------------------------------------------------")
print("\nEjercicio 4 - Calcular área y perímetro\n")

def calcular_area_circulo(radio):
    area = 3.1416 * radio ** 2
    return print(f"El área del círculo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    return print(f"El perímetro del círculo es: {perimetro}")

radio = float(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#* 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

print("------------------------------------------------------------------------------")
print("\nEjercicio 5 - Convertir segundos a horas\n")

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(f"{segundos} segundos son {horas} horas.")

segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

#* 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

print("------------------------------------------------------------------------------")
print("\nEjercicio 6 - Tabla de multiplicar\n")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#* 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

print("------------------------------------------------------------------------------")
print("\nEjercicio 7 - Operaciones básicas\n")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else "Error (división por cero)"
    return suma, resta, producto, division

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Producto: {resultados[2]}")
print(f"División: {resultados[3]}")
print(f"Resultados completos: {resultados}")

#* 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

print("------------------------------------------------------------------------------")
print("\nEjercicio 8 - Calcular Indice de Masa Corporal\n")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)

#* 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

print("------------------------------------------------------------------------------")
print("\nEjercicio 9 - Convertir Celsius a Fahrenheit\n")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius}°C son {fahrenheit}°F.")

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)

#* 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

print("------------------------------------------------------------------------------")
print("\nEjercicio 10 - Calcular promedio de 3 números\n")
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return print(f"El promedio de {a}, {b} y {c} es: {promedio}")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
calcular_promedio(num1, num2, num3)