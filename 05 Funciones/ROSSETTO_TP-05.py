#FUNCIONES
import misFunciones as fx

def imprimir_hola_mundo():
    print("Hola mundo!")

def saludar_usuario(nombre):
    print(f" Hola {nombre} !")

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#PROGRAMA PRINCIPAL
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
#devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

saludar_usuario(" Fabiana")

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados

nombre=input(" Ingrese su nombre ")
apellido=input(" Ingrese su apellido ")
edad=input(" Ingrese su edad ")
residencia=input(" Ingrese su lugar de residencia ")
informacion_personal(nombre,apellido,edad,residencia)

#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como 
#parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que 
#reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones 
# para mostrar los resultados.
radio=float(input(" Ingrese el radio "))
fx.calcular_area_circulo(radio)
fx.calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
#Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos=int(input(" Ingrese la cantidad de segundos que quiera convertir "))
fx.segundos_a_horas(segundos)

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
numero=int(input(" Ingrese un numero "))
fx.tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

fx.operaciones_basicas( 5,6)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
#Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales
peso=float(input(" Ingrese su peso "))
altura=float(input(" Ingrese un altura "))
fx.calcular_imc (peso,altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
cel=float(input(" Ingrese los grados celsius que desea convertir "))
fx.celsius_a_fahrenheit(cel)

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función
print("ingrese tres numeros ")
num1=int(input())
num2=int(input())
num3=int(input())
fx.calcular_promedio(num1,num2,num3)
