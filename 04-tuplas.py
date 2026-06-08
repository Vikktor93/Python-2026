# TUPLAS

# Creando una tupla de tipo String
estudiantes = ("Matias", "Francisco", "Alan", "Maykol")
print(type(estudiantes))
print(f"TUPLA: {estudiantes}")

# Creando una tupla compleja con datos estructurados
datos = ([1,2,3,4,5], ("Queilen", "Castro"), ("Universidad de Los Lagos", "AIEP"))

# También se puede consultar la posición de un elemento al igual que la lista
print(datos[0])
print(f"TUPLA: {datos}\n")

# Con las listas se puede eliminar elementos
lista_asignaturas = ['Programación', 'Química', 'Introducción a la Matemáticas']
print(f"LISTA: {lista_asignaturas}")

lista_asignaturas.pop()
print(f"LISTA CON ÚLTIMO ELEMENTO ELIMINADO: {lista_asignaturas}")

# ¿Qué pasa si quiero eliminar el último elemento de una tupla?
# Respuesta: como es inmutable no se puede eliminar elementos en una tupla
"""estudiantes.pop()
print(f"TUPLA CON ÚLTIMO ELEMENTO ELIMINADO: {estudiantes}")"""

# Ocuparemos el método index para consultar la posición de un elemento
print(estudiantes.index('Alan')) # se encuentra en la posición 2

# Método Sorted() para ordenar elementos de una tupla
print(sorted(estudiantes))