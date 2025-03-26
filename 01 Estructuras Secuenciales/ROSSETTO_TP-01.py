#Práctico 1: Estructuras secuenciales  
import math

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 


print("Hola Mundo !")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla. 

nombre = input(" Ingrese su nombre ")
print (f"Hola, {nombre} !")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

nombre = input(" Ingrese su nombre ")
apellido = input(" Ingrese su apellido ")
edad = input(" Ingrese su edad ")
lugar = input(" Ingrese su lugar de residencia ")

print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar} ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.

radio = float(input( " Ingrese el radio de un circulo"))
area =  math.pi * (radio**2)
perimetro = 2* math.pi * radio
print ( f"El area del circulo es {area} y el perimetro {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

segundos = int(input( "Ingrese una cantidad de segundos "))
horas= (segundos/60)/60
print(f" {segundos} segundos equivale a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

numero= int(input (" Ingrese un numero "))
resultado=0
for i in range (1,11): 
  resultado= numero * i
  print(f"{numero} x {i} = {resultado}") 

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1= int(input( " Ingrese un numero" ))
num2= int(input( " Ingrese otro numero" ))
if (num1!= 0 and num2!=0) :

    print(f" La suma de {num1} y {num2} es: {num1+num2}, el resultado de la division entre {num1} y {num2} es : {num1/num2}, la multiplicacion entre {num1} y {num2} es : {num1*num2}, el resultado de restar {num2} a {num1} es {num1-num2}")
else:
     print(" Ambos numeros deben ser distintos de 0")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.

altura= float(input(" Ingrese su altura "))
peso= float(input(" Ingrese su peso "))

print(f" el indice de masa corpotal es {peso/(altura**2)}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit.

tempCelsius= float(input( " Ingrese una temperatura en grados Celsius por favor"))
print (f"{tempCelsius} C° equivale a {(tempCelsius * 9/5) + 32} F° ")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

num1= float(input( " Ingrese un numero" ))
num2= float(input( " Ingrese otro numero" ))
num3= float(input( " Ingrese otro numero" ))

print(f" El promedio de los tres numeros ingresados es: {(num1+num2+num3)/3} ")
