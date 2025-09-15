# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 4 - Estructuras Repetitivas
# Actividades

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
num_entero = input("Por favor, ingrese un número entero: ")
longitud = len(str(num_entero))
print("El número tiene", longitud, "dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

suma = 0
for i in range(num1 + 1, num2):
    print(i)
    suma += i
    print("Suma parcial:", suma)
print("La suma de los números entre", num1, "y", num2, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma = 0
while True:
    numero_entero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero_entero == 0:
        break
    suma += numero_entero
    print("Suma parcial:", suma)
print("La suma total es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print(f"No es {intento}. Intentos hasta ahora: {intentos}. Proba de nuevo :)")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero_inicio = 0
numero_final = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero_inicio, numero_final + 1):
    suma += i
print("La suma de los números entre", numero_inicio, "y", numero_final, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
num_a_ingresar = 100
pares, impares, negativos, positivos = 0, 0, 0, 0
for _ in range(num_a_ingresar):
    numero_entero = int(input("Ingrese un número entero, por favor: "))
    if numero_entero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero_entero < 0:
        negativos += 1
    elif numero_entero > 0:
        positivos += 1
print(f"Números pares: {pares}, Números impares: {impares}, Números negativos: {negativos}, Números positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
num_a_ingresar = 100
suma = 0
for _ in range(num_a_ingresar):
    numero_entero = int(input("Ingrese un número entero: "))
    suma += numero_entero
media = suma / num_a_ingresar
print(f"La media de los {num_a_ingresar} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero_entero = input("Ingrese un número entero: ")
numero_invertido = numero_entero[::-1]
print("El número invertido es:", numero_invertido)