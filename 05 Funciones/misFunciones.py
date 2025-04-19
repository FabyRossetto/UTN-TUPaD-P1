
import math
#Funcion que calcula el area de un circulo
def calcular_area_circulo(radio):
   area = math.pi * (radio*radio)
   return print(" El area del circulo es ", area)

#Funcion que calcula el perimetro de un circulo
def calcular_perimetro_circulo(radio):
    perimetro= 2 * math.pi * radio
    return print(" El perimetro del circulo es ", perimetro)

#Funcion que pasa los segundos a horas
def segundos_a_horas(segundos):
    horas= (segundos/60)/60
    return print(f"{segundos} segundos son {horas} horas")

#Funcion que muestra la tabla de mutiplicar de un numero
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado=i*numero
        print(f"{numero} X {i} = {resultado}")


#Funcion que realiza las operaciones basicas
def  operaciones_basicas(a, b):
    print(f"""La suma de {a} y {b} es: {a+b} 
La resta de {a} menos {b} es: {a-b}
La multiplicación de {a} X {b} es: {a*b}
La division de {a} entre {b} es: {a/b}""")      
    

#Funcion que calcula el indice de masa corporal    
def calcular_imc(peso, altura):
   IMC = peso/(altura*altura)
   return print(" El indice de masa corporal es: ",round(IMC,2))

#Funcion que pasa de grados celsius a fahrenheit. F = (C * 9/5) + 32
def celsius_a_fahrenheit(celsius):
    return print(f"{celsius} °C son {(celsius * 9/5) + 32} °F")

#Funcion que calcula el promedio de 3 numeros
def calcular_promedio(a, b, c):
    return print("El promedio de los numeros ingresados es: ", (a+b+c)/3)
