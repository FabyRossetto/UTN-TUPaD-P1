#Práctico 3: Estructuras condicionales 

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese su edad"))
if edad > 18:
    print("Es mayor de edad")
else:
    print(" Es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.

nota=int(input("Ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print(" Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par"

num = int(input("Ingrese un numero par"))

if num % 2 == 0:
    print("Ha ingresado un numero par")
else :
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años. 

edad=int(input("Ingrese su edad"))
if edad >= 0 and edad < 12:
    print("Categoria: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoria: Adolescente")
elif edad >=18 and edad < 30 :
    print("Categoria: Adulto/a joven")
elif edad >=30 :
     print("Categoria: Adulto/a")
else:
    print(" La edad no es valida")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

con=input("Ingrese una contraseña")
if len(con)>=8 and len(con)<=14 :
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

import random 
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
media=mean(numeros_aleatorios) 
moda=mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
print(f"La media es {media}, la moda { moda } , y la mediana es {mediana}")

# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# Sin sesgo: cuando la media, la mediana y la moda son iguales.

if media>mediana and mediana>moda:
    print("Sesgo positivo")
elif media<mediana and mediana<moda:
    print("Sesgo negativo")
elif media == mediana == moda :
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 

frase=input(" Ingrese una frase ")
long=len(frase)
if frase[long-1]=="a" or frase[long-1]=="e" or frase[long-1]=="i" or frase[long-1]=="o" or frase[long-1]=="u":
    print(frase + "!")
else:
    print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre= input("Ingrese su nombre")
opcion=input("Ingrese una opcion: \n 1) Si quiere su nombre en mayúsculas\n 2) Si quiere su nombre en minúsculas\n 3) Si quiere su nombre con la primera letra mayúscula" )
if opcion=="1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion=="3":
    print(nombre.title())      
else :
    print("La opcion indicada es incorrecta")



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#Menor que 3: "Muy leve" (imperceptible). 
#Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud= int(input("ingrese la magnitud del terremoto"))
if magnitud < 3 :
    print(" Muy leve (imperceptible)")
elif magnitud >=3 and magnitud<4: 
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud<7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >=7:
    print("Extremo (puede causar graves daños a gran escala)")

    
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N para norte, S para sur): ").upper()
dia = int(input("Ingrese qué día es: "))
mes = int(input("Ingrese qué mes es: "))


if (1 <= dia <= 31) and (1 <= mes <= 12):
    if ((mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20)):  
        estacion_n = "Primavera"
        estacion_s = "Otoño"
    elif ((mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20)):  
        estacion_n = "Verano"
        estacion_s = "Invierno"
    elif ((mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20)):  
        estacion_n = "Otoño"
        estacion_s = "Primavera"
    else: 
       estacion_n = "Invierno"
       estacion_s = "Verano"

    if hemisferio == "N":
        print(estacion_n)
    elif hemisferio == "S":
        print(estacion_s)
    else:
        print("Error: Hemisferio no válido.")
else:
    print("Los datos proporcionados son incorrectos.")
