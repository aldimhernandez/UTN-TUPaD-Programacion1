# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 1 - Estructuras Secuenciales
# Actividades
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre por favor: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("Por favor, ingrese los siguientes datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
lugar_residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("A continuación se le solicitará el radio de un círculo.")
radio = float(input("Ingrese el radio del círculo: "))
PI = 3.14159
area = PI * radio ** 2
perimetro = 2 * PI * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("A continuación se le solicitará una cantidad de segundos.")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
multiplicador = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {multiplicador}:")
for i in range(1, 11):
    resultado = multiplicador * i
    print(f"{multiplicador} x {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("A continuación se le solicitarán dos números enteros distintos de 0.")
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
if num1 == 0 or num2 == 0:
    print("Los números deben ser distintos de 0. Por favor, intente nuevamente.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2
    print("Resultados:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"División: {division}")
    print(f"Multiplicación: {multi}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal:
# IMC = peso en kg / (altura en metros)^2.
print("A continuación se le solicitarán su altura y peso.")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 Fahrenheit = 9 / 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 Celsius + 32
print("A continuación se le solicitará una temperatura en grados Celsius.")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("A continuación se le solicitarán 3 números.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números ingresados es: {promedio}")