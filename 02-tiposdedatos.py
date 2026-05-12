# DATOS NÚMERICOS 

# Números Enteros
edad = 32
annio_nacimiento = 1993

# Números Flotantes (Reales)
estatura = 1.75  # el decimal se utiliza punto y no coma

# Números Complejos
num_complejo = 4 + 2j        # primera forma de crear un número complejo
otro_complejo = complex(4,2) # segunda forma de crear un número complejo

print("------- DATOS NÚMERICOS ----- ")
print(num_complejo)
print(otro_complejo)

# Operacíón Arimetica Básica (Área de un Triángulo)
PI = 3.14159
base = 8
altura = 12.5

area = (base * altura) / 2
print(f"El área del triángulo es de {area} cm")

# Formatos de Salida de Números
# Salida del número PI con 4 décimales
print(f"El número PI tiene un valor de {PI:.3f}")

# El método de Redondeo
print(round(PI, 2))
print(f"El área del triángulo es de {round(area)} cm")

# Transformaciones de Números
print(float(edad))

# CADENA DE TEXTO (STRINGS)
carrera = "Ingenieria Civil en Informática"
institucion = "Universidad de los Lagos"

print("------- CADENAS DE TEXTO (STRING) ----- ")
# Imprimir la posición del caracter
print(carrera[0]) # se imprime la primera letra
print(carrera[-1]) # se imprime la última letra

# Aplicando Método Split 
print(carrera.split())     # se divide la cadena en subcadenas (se genera una lista)
print(institucion.split())

print("Hola" * 4)    # multiplicación de un string por un entero
# print ("Hola" / 2) # esto no se puede hacer

print(carrera[0:10]) # Obteniendo una sub cadena (Cortando Strings)

# Método len() permite contar carácteres
print(len(institucion))


# ARREGLOS (LISTAS)
print("------- ARREGLOS (LISTAS) ----- ")
colores = ["Azul", "Rojo", "Verde", "Amarillo"] # arreglo de strings
numeros = [1,2,3,4,5,6]                         # arreglo númerico
lista_mixta = ["Gato", 2, 67.0, True]           # arreglo mixto de elementos

print(colores[0])  # se imprime el primer elemento de la lista colores
print(numeros[-1]) # se imprime el último elemento de la lista números
print(lista_mixta)

# Booleanos (Lógicos)
luz_electrica = True
interruptor = False

print("------- BOOLEANOS ----- ")
print(luz_electrica)
print(interruptor)

# Método Type que permite saber el tipo de dato de una variable
print(f"El tipo de dato es {type(num_complejo)}")

print("------- EVALUANDO DATOS BOOLEANOS ----- ")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("False"))
print(bool(3000))