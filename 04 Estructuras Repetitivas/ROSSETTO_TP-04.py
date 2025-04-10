#  Trabajo Práctico	n° 4:	Estructuras	repetitivas	

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

numero_entero= int(input(" Ingrese un numero entero por favor "))

contador = 0
n = abs(numero_entero)

while n > 0:
    n = n // 10
    contador += 1

print("Cantidad de digitos:", contador)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.  

num1= int(input("Ingrese un numero entero"))
num2= int(input("Ingrese otro numero entero"))
suma=0
if num1>num2:
    aux=num1
    num1=num2
    num2=aux

for i in range (num1+1,num2):
    suma+=i
print(f"la suma de todos los numeros entre {num1} y {num2} (excluyendo los mismos) es : {suma}")    

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

numero= int(input("ingrese un numero"))
suma=0
while numero!= 0 :
    suma+=numero
    numero= int(input("ingrese un numero"))

print(" El total acumulado es :" , suma)    

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
contador=1
numero_aleatorio= random.randint(0, 9)
numero_usuario= int(input(" Ingrese un numero entre 0 y 9"))

if numero_usuario <0 or numero_usuario>9:
    print(" El numero ingresado debe ser entre 0 y 9")

while numero_usuario != numero_aleatorio:
    contador=contador+1
    numero_usuario= int(input(" Ingrese un numero entre 0 y 9"))
    if numero_usuario <0 or numero_usuario >9:
        print(" El numero ingresado debe ser entre 0 y 9")

print(" Los intentos para adivinar el numero fueron " , contador)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 
i=100
while i<=100 and i>=0 :
    print (i)
    i=i-2

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 


num_usuario= int(input("Ingrese un numero entero positivo"))

suma=0
if num_usuario<0 :
    print(" El numero ingresado debe ser positivo")
else:
    for i in range (0,num_usuario+1):
        suma+=i
    print(f"la suma de todos los numeros entre 0 y {num_usuario}  es : {suma}")    


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. 

CANT_NUMERO=10
esPar=0
esImpar=0
esNegativo=0
esPositivo=0
print(f" Usted debera ingresar {CANT_NUMERO} numeros ")
for i in range (0,CANT_NUMERO):
    if i < CANT_NUMERO:
        num= int(input(f" Ingrese el numero {i+1}"))
    else:
        num= int(input(f" Ingrese el ultimo numero"))
        
    if num % 2==0:
        esPar=esPar+1
    else:
        esImpar= esImpar+1

    if num > 0:
        esPositivo= esPositivo+1
    else:
        esNegativo= esNegativo+1

print(f" De {CANT_NUMERO} numeros ingresados, los numeros pares son : {esPar} \n Los impares : {esImpar} \n Los positivos : {esPositivo} \n Los negativos : {esNegativo}" )

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. 

CANTIDAD_NUMERO= 5
contador=1
suma=0
print(f" Usted debera ingresar {CANTIDAD_NUMERO} numeros ")

while contador <= CANTIDAD_NUMERO:

    numero_ing = int(input(f" Ingrese el numero {contador}"))
    suma= suma + numero_ing
    contador+=1

print("La media de los numeros ingresados es : ", (suma/CANTIDAD_NUMERO))

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_usuario2= int(input(" Ingrese un numero"))
numero_invertido = 0

while numero_usuario2 > 0:

    digito = numero_usuario2 % 10 #esto deja en "digito" el ultimo
    numero_invertido = numero_invertido * 10 + digito # aca se multiplica *10 para moverlo a la izquierda y se le suma el nuevo digito al final
    numero_usuario2 = numero_usuario2 // 10 # aca se elimina el ultimo digito, que ya fue invertido

print("El número invertido es:", numero_invertido)

