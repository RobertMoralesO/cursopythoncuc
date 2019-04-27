
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
    








