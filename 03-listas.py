# LISTAS

# Primera Forma de Declaración de Listas (Lista Mixta)
lista1 = ['Victor', 32, True, "Victor", "Victor", "Victor"]
ramos = [] # lista vacia

# Segunda Forma de Declaración de Listas (Lista Númerica)
n = list([5,4,3,2,1])

# MÉTODOS PARA LA LISTAS
# Imprime el primer elemento de la lista1
print(lista1[0]) 

# Contar la cantidad de concurrencias de un elemento
print(lista1.count('Victor'))
print(ramos)

# Agregar un elemento al final de la lista
ramos.append('Química')
print(ramos)

ramos.append('Habilidades Comunicativas')
print(ramos)

ramos.append('Programación')
print(ramos)

# Otra forma de insertar un elemento a la lista (De forma específica)
ramos.insert(0, 'Introducción a la Matemática')
print(ramos)

# Modificar un elemento en específico de una lista
ramos[2] = 'Habilidades Comunicativas para Ingenieros/as'
print(ramos)

# Eliminar el último elemento de la lista
ramos.pop()
print(ramos)

# Ordenar los elementos de una lista de forma descendente a ascendente
# print(ramos.sort())
ramos.sort()
print(ramos)

n.sort()
print(n)

# Ordenar elementos de una lista según la cantidad de caracteres de cada elemento
ramos.sort(key=len)
print(ramos)

# Extender una lista a partir de otra
ramos_segundo_semestre = ['Ciudadanía', 'Álgebra', 'Introducción a la Física']
print(ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)