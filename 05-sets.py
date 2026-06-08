# SETS (CONJUNTOS)

# Creando los primeros conjuntos (de dos formas diferentes)
colores_primarios = {'Azul', 'Rojo', 'Amarillo'}
colores_secundarios = set({'Naranja', 'Verde', 'Violeta'})
print(type(colores_primarios))

print(f"CONJUNTO 1: {colores_primarios}")
print(f"CONJUNTO 2: {colores_secundarios}")

# Creando un Conjunto Nuevo con Duplicados 
# Respuesta: en los sets no se considerán duplicados
colores_nuevos = {'Azul', 'Rojo', 'Celeste', 'Azul', 'Rojo'}
print(f"CONJUNTO 3: {colores_nuevos}")

# Agregando un nuevo elemento al set colores_nuevos add()
colores_nuevos.add('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")

# Eliminando un elemento del set colores_nuevos discard()
colores_nuevos.discard('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")

# Aplicando el Método Intersection()
interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUNTO INTERSECTADO: {interseccion}")