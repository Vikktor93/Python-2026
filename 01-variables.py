# Apuntes Variables - 07 de Mayo 2026

# Definición de Variables
nombre = "Victor"
apellido = "Saldivia"
edad = 32

# Esto un comentario de una linea

""" Esto es un comentario
multilinea
porque sigo hacia
abajo """

# Formas de Imprimir Texto

# Forma 1: Clásica separando variables y texto por comas
print("Mi nombre es", nombre, "y mi apellido es", apellido, "y tengo", edad, "años") 

# Forma 2: Utilizando f-strings
print(f"Mi nombre es {nombre} y mi apellido es {apellido} y tengo {edad} años")

# Forma 3: Concatenación (utilizando el operador +)
# La función str() transforma el valor a Cadena de Texto
print("Mi nombre es " + nombre + " y mi apellido es " + apellido + " y tengo " + str(edad) + " años ")

# Utilizando el método input y creando una variable llamada carrera
carrera = input("¿Qué carrera estudias?")
print(f"Yo estudio la carrera de: {carrera}")

