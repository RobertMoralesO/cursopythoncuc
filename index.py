
# Comentario de linea
"""
Comentario
de Parrafo
"""

# Hola Mundo
print("Hola Mundo")

# Variables

x = 4  # int
y = "Texto"  # String
z = 4.5  # float
a = True  # boolean
b = False  # boolean
c = 4+5j  # complejo

print(x, y, z, a, b, c)

# Conocer el tipo de dato de una variable
print(type(b))

# Conversiones de tipos de datos

# Enteros
x = int(2)
print(x)
x = int(2.8)
print(x)
x = int("2")
print(x)

# Float
x = float(2)
print(x)
x = float(2.8)
print(x)
x = float("2")
print(x)
x = float("2.5")
print(x)

# String
x = str(2)
print(x)
y = str(2.8)
print(x)
x = str("2")
print(x)

# Manejo de cadenas de texto y algunos métodos

cad = "Hello World"
print(cad[0])
print(cad[2])
print(cad[0:5]) # No toma el último valor

cad = "    Hello World   "
cad = cad.strip()
print(cad)
print(cad[0])

cad = "Hello World"
print(len(cad))
print(cad.lower())
print(cad.upper())
print(cad.replace('l', 'Y'))
print(cad.split(" "))
print(cad.split("l"))

# Operaciones
import math
# Operaciones Aritméticas
a = 2
b = 3
c = a + b
c = a - b
c = a * b
c = a / b #Cociente
c = a//b #Parte entera
c = a % b #Reciduo
c = a ** b # Exponente
c = math.sqrt(a) #Raiz
c = math.pi

# Captura por consola
print("Digite el nombre")
nombre = input()
print("Hola "+nombre+"!")

print("Digite el número uno")
n1 = input()
n1 = float(n1)
print("Digite el número dos")
n2 = input()
n2 = float(n2)
print(n1+n2)

# Condiciones

a = 2
b = 5

if a > b:
    print(a,'Es mayor que',b)
else:
    print(b,'Es mayor que',a)
    
if b > a:
    if b > 1:
        print (b,"Es mayor que 1 y es mayor que",a )

if a == b:
    print("Son Iguales")
elif a > b:
    print(a, " es mayor que ",b)
else:
    print(b, "es mayor que ",a)
    
if a == b and a >2:
    print (a,"Es igual a",b,"Mayor que 2")
    
if a == b or a >2:
    print (a,"Es igual a",b,"Mayor que 2")
    
# Arrays
    
v = ["Hola", "Mundo", 4, 3.4, True, ["Otro", "Array", "Dentro"]]
v2 = ["Hola", "Mundo"]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Acceder al elemento
print (v2[0])

# Modificar el elemento
v2[1]= "Roberto"

# Eliminar elemento
v2.remove("Hola")

# Eliminar el último elemento
v.pop()
v.pop(4)

# Agregar elemento
v.append(5)
v.insert(1,"Roberto")
# Borrar elementos
v.clear()
# Conocer la posición de un elemento
v.index('Mundo')
# Número de elementos de un array
len(v)
# Cuantas veces aparece un elemento en el vector
v.append('Mundo')
v.count('Mundo')

# Ordenar un vector
a = [5, 9, 6, 7, 11]

# Ordenar un vector
a.sort()
# Preguntas si existe un elemento dentro de un array
res = 6 in a
print(res)

# Acceder al último elemento de un Vector
a[-1]

# Accedar a un elemento de un array interno
v = ["Hola", "Mundo", 4, 3.4, True, ["Otro", "Array", "Dentro"]]
# Forma 1
aux = v[-1]
aux = aux[0]
print (aux)

# Forma 2
aux = v[-1][0]
print (aux)

# Matriz
m = [[2, 4], [4, 2]]

# Recorrer Vector

for x in v[:5]:
    print (x)
    
# Recorrer con saltos
a = [5, 9, 6, 7, 11]

# Recorre de dos en dos hasta la posicion n-1
for x in a[0:3:2]:
    print (x)
    
# Recorre de dos en dos hasta el final del array
for x in a[0::2]:
    print (x)
    
    
print("Digite el valor final de la sumatoria")
a = int(input())
suma =0
for x in range(a+1):
    suma = suma + x
print("La sumatoria es: ",suma)

    
print("Digite el valor final de la sumatoria")
a = int(input())
sumatoria = sum(range(a+1))
print("La sumatoria es: ",sumatoria)


# While
i = 1
while i<5:
    print(i)
    i = i +1
    
# Métodos

# Procedimientos no retorna valor
def hola_mundo():
    print("Hola Mundo")

#Invocar el procedimiento
hola_mundo()

# Funcion que retorna valor
def elevar_cuadrado(numero):
    return numero ** 2


elevar_cuadrado(3)



























