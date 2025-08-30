# Universidad Tecnológica Nacional
# Tecnicatura Universitaria en Programación
# Hernández, María Aldana

# Trabajo Práctico 3 - Estructuras Condicionales
# Actividades
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

MAYOR_EDAD = 18

edad = int(input("Ingrese su edad: "))

if edad >= MAYOR_EDAD:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

NOTA_MINIMA_APROBADO = 6
MENSAJE_APROBADO = "Aprobado"
MENSAJE_DESAPROBADO = "Desaprobado"
nota = float(input("Ingrese su nota: "))

print(MENSAJE_APROBADO if nota >= NOTA_MINIMA_APROBADO else MENSAJE_DESAPROBADO)

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

MENSAJE_NUMERO_PAR = "Ha ingresado un número par"
MENSAJE_NUMERO_IMPAR = "Por favor, ingrese un número par"

numero = int(input("Ingrese un número par: "))

print(MENSAJE_NUMERO_PAR if numero % 2 == 0 else MENSAJE_NUMERO_IMPAR)

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
"""
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
 """

MENSAJE_NINO = "Usted es un niño/a"
MENSAJE_ADOLESCENTE = "Usted es un adolescente"
MENSAJE_ADULTO_JOVEN = "Usted es un adulto/a joven"
MENSAJE_ADULTO = "Usted es un adulto/a"
MENSAJE_EDAD_INVALIDA = "Edad inválida"

EDAD_NINO_MIN = 0
EDAD_NINO_MAX = 11

EDAD_ADOLESCENTE_MIN = 12
EDAD_ADOLESCENTE_MAX = 17

EDAD_ADULTO_JOVEN_MIN = 18
EDAD_ADULTO_JOVEN_MAX = 29

EDAD_ADULTO_MIN = 30

edad = int(input("Ingrese su edad: "))

if EDAD_NINO_MIN <= edad <= EDAD_NINO_MAX:
    print(MENSAJE_NINO)
elif EDAD_ADOLESCENTE_MIN <= edad <= EDAD_ADOLESCENTE_MAX:
    print(MENSAJE_ADOLESCENTE)
elif EDAD_ADULTO_JOVEN_MIN <= edad <= EDAD_ADULTO_JOVEN_MAX:
    print(MENSAJE_ADULTO_JOVEN)
elif edad >= EDAD_ADULTO_MIN:
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_EDAD_INVALIDA)

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

MENSAJE_CONTRASENA_CORRECTA = "Ha ingresado una contraseña correcta"
MENSAJE_CONTRASENA_INCORRECTA = "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

LONGITUD_MINIMA = 8
LONGITUD_MAXIMA = 14

contrasena = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

print(MENSAJE_CONTRASENA_CORRECTA if LONGITUD_MINIMA <= len(contrasena) <= LONGITUD_MAXIMA else MENSAJE_CONTRASENA_INCORRECTA)


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
"""
En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
"""
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

SESGO_POSITIVO = "Sesgo positivo o a la derecha"
SESGO_NEGATIVO = "Sesgo negativo o a la izquierda"
SIN_SESGO = "Sin sesgo"

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print(SESGO_POSITIVO)
elif media < mediana < moda:
    print(SESGO_NEGATIVO)
elif media == mediana == moda:
    print(SIN_SESGO)
else:
    print("No se puede determinar el sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase and frase[-1] in vocales:
    frase += "!"
    print(frase)
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
"""
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
"""
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")

match opcion:
    case "1":
        print(nombre.upper())
    case "2":
        print(nombre.lower())
    case "3":
        print(nombre.title())
    case _:
        print("Opción inválida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
"""
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

MENSAJE_MUY_LEVE = "Muy leve (imperceptible)"
MENSAJE_LEVE = "Leve (ligeramente perceptible)"
MENSAJE_MODERADO = "Moderado (sentido por personas, pero generalmente no causa daños)"
MENSAJE_FUERTE = "Fuerte (puede causar daños en estructuras débiles)"
MENSAJE_MUY_FUERTE = "Muy Fuerte (puede causar daños significativos)"
MENSAJE_EXTREMO = "Extremo (puede causar graves daños a gran escala)"
MENSAJE_MAGNITUD_INVALIDA = "Magnitud inválida"

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 0:
    print(MENSAJE_MAGNITUD_INVALIDA)
elif magnitud < 3:
    print(MENSAJE_MUY_LEVE)
elif 3 <= magnitud < 4:
    print(MENSAJE_LEVE)
elif 4 <= magnitud < 5:
    print(MENSAJE_MODERADO)
elif 5 <= magnitud < 6:
    print(MENSAJE_FUERTE)
elif 6 <= magnitud < 7:
    print(MENSAJE_MUY_FUERTE)
else:
    print(MENSAJE_EXTREMO)


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
"""
Periodo del año                                                   | Estación en el hemisferio norte   | Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)         | Invierno                          | Verano
Desde el 21 de marzo hasta el 20 de junio (incluidos)             | Primavera                         | Otoño
Desde el 21 de junio hasta el 20 de septiembre (incluidos)        | Verano                            | Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)    | Otoño                             | Primavera
"""
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

MENSAJE_OTONO = "Usted se encuentra en Otoño"
MENSAJE_INVIERNO = "Usted se encuentra en Invierno"
MENSAJE_PRIMAVERA = "Usted se encuentra en Primavera"
MENSAJE_VERANO = "Usted se encuentra en Verano"

HEMISFERIO_NORTE = "N"
HEMISFERIO_SUR = "S"
HEMISFERIOS_VALIDOS = [HEMISFERIO_NORTE, HEMISFERIO_SUR]

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio not in HEMISFERIOS_VALIDOS:
    print("Hemisferio inválido. Debe ingresar 'N' o 'S'.")
elif not (1 <= dia <= 31):
    print("Día inválido. Debe ingresar un valor entre 1 y 31.")
else:
    match mes:
        case 1 | 2:
                mensaje = MENSAJE_INVIERNO if hemisferio == HEMISFERIO_NORTE else MENSAJE_VERANO
        case 3:
                if dia < 21:
                    mensaje = MENSAJE_INVIERNO if hemisferio == HEMISFERIO_NORTE else MENSAJE_VERANO
                else:
                    mensaje = MENSAJE_PRIMAVERA if hemisferio == HEMISFERIO_NORTE else MENSAJE_OTONO
        case 4 | 5:
                mensaje = MENSAJE_PRIMAVERA if hemisferio == HEMISFERIO_NORTE else MENSAJE_OTONO
        case 6:
                if dia < 21:
                    mensaje = MENSAJE_PRIMAVERA if hemisferio == HEMISFERIO_NORTE else MENSAJE_OTONO
                else:
                    mensaje = MENSAJE_VERANO if hemisferio == HEMISFERIO_NORTE else MENSAJE_INVIERNO
        case 7 | 8:
                mensaje = MENSAJE_VERANO if hemisferio == HEMISFERIO_NORTE else MENSAJE_INVIERNO
        case 9:
                if dia < 21:
                    mensaje = MENSAJE_VERANO if hemisferio == HEMISFERIO_NORTE else MENSAJE_INVIERNO
                else:
                    mensaje = MENSAJE_OTONO if hemisferio == HEMISFERIO_NORTE else MENSAJE_PRIMAVERA
        case 10 | 11:
                mensaje = MENSAJE_OTONO if hemisferio == HEMISFERIO_NORTE else MENSAJE_PRIMAVERA
        case 12:
                if dia < 21:
                    mensaje = MENSAJE_OTONO if hemisferio == HEMISFERIO_NORTE else MENSAJE_PRIMAVERA
                else:
                    mensaje = MENSAJE_INVIERNO if hemisferio == HEMISFERIO_NORTE else MENSAJE_VERANO
        case _:
            mensaje = "Mes inválido"
    print(mensaje)