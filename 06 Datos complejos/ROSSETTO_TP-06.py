#Trabajo practico: Estructuras de datos complejas

#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#Naranja = 1200 Manzana = 1500 Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# Banana = 1330 Manzana = 1700 Melón = 2800 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios. 
lista_de_frutas = precios_frutas.keys()
print(lista_de_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#Luego, pedí un nombre y mostrale el número asociado, si existe. 
Lista_de_contactos={}
for i in range (5) :
    nombre=input("Ingrese un nombre ")
    tel=input("Ingrese el numero de telefono ")
    Lista_de_contactos[nombre]=tel

nombre=input("Escriba el nombre del contacto que desea buscar")
if (nombre in Lista_de_contactos):
    print (f"El numero telefonico de {nombre} es :{ Lista_de_contactos[nombre]}")
else:
    print("El nombre no esta en su agenda")

#5) Solicita al usuario una frase e imprime: 
#Las palabras únicas (usando un set). 
#Un diccionario con la cantidad de veces que aparece cada palabra. 
 
frase= input("Ingrese una frase")   
palabras = frase.split()
palabras_unicas = set(palabras)
print (f"Palabras únicas:{palabras_unicas}")

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1


print(f"Recuento: {contador_palabras}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.
alumnos = {}
for i in range(3):
    nombre_alumno=input("Ingrese el nombre del alumno")
    nota1=int(input("ingrese la primer nota"))
    nota2=int(input("ingrese la segunda nota"))
    nota3=int(input("ingrese la tercer nota"))
    alumnos[nombre_alumno]=(nota1,nota2,nota3)
print (alumnos)

for nombre_alumno in alumnos:
    notas = alumnos[nombre_alumno]
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre_alumno} es: {promedio:}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#Mostrá los que aprobaron ambos parciales. 
#Mostrá los que aprobaron solo uno de los dos. 
#Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

# Aprobó ambos parciales: Intersección
ambos = parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", ambos)

# Aprobó solo uno de los dos : Diferencia simétrica
solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno de los dos:", solo_uno)

# Aprobó al menos uno : Unión
al_menos_uno = parcial1.union(parcial2)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#Consultar el stock de un producto ingresado. 
#Agregar unidades al stock si el producto ya existe. 
#Agregar un nuevo producto si no existe
stock = {
    "paquetes de fideos": 10,
    "paquetes de azucar": 5,
    "cafe": 8
}

producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("Queres agregar unidades? (si/no): ").lower()
    if agregar == "si":
        cantidad = int(input("Cuantas unidades queres agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")
    elif agregar=="no" :
        pass
else:
    nuevo = input(f"{producto} no existe. Queres agregarlo? (si/no): ").lower()
    if nuevo == "si":
        cantidad = int(input("Cuantas unidades tiene?: "))
        stock[producto] = cantidad
        print(f"{producto} agregado con stock: {cantidad}")
    elif nuevo=="no" :
        print("no ha sido agregado ningun producto")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("lunes", "10:00"): "Tango",
    ("martes", "14:00"): "Ingles",
    ("viernes", "18:00"): "Yoga"
}

dia = input("Ingresá el dia: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

evento = agenda.get((dia, hora))
if evento:
    print(f"Actividad: {evento}")
else:
    print("No hay actividad registrada en ese horario.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: Las capitales sean las claves y los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio",
    "Inglaterra":"Londres"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido :")
print(capitales)
