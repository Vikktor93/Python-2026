# DICCIONARIOS

# Primera forma de declarar un diccionario
paciente = {
    'nombre':'Benjamin Bahamonde',
    'edad': 18,
    'ciudad': 'Ancud',
    'fechas_atencion': [5,8,12],
    'diagnostico': ('resfrío común'),
    'informacion_extra':{ # creación de un sub-diccionario
        'tipo_de_sangre' : 'A+',
        'hemograma': False
    }
}

# Segunda forma de declarar un diccionario
medico = dict(
    nombre = 'Ignacio Saez',
    edad = 19,
    especialidad = 'Cardiologo'
)

print(type(paciente))
print(f"===== FICHA PACIENTE ===== \n{paciente}\n")
print(f"===== FICHA MÉDICO ===== \n{medico}\n")

# CONSULTA DE INFORMACIÓN A DICCIONARIOS

# ¿Cómo consulto solo el nombre del paciente sin traer el diccionario completo?
print(paciente['nombre'])

# A diferencia de [], este método no genera error si no existe la clave
# Método get() obtiene el valor de una clave, si no existe retorna None (o un valor por defecto en vez de un error)
print(paciente.get('Nombre'))
print(paciente.get('rut', 'N/D (No Data)'))

# Retornar las claves, los valores o ambas como pares
print(paciente.keys())   # dict_keys(['nombre', 'edad' ...]) -> sólo claves
print(paciente.values()) # dict_values(['Benjamin', '18' ...]) -> sólo valores
print(paciente.items())  # dict_items([('nombre', 'Benjamin), ...]) -> par clave-valor -> lista de tuplas

# Retorna el número de claves que tiene el diccionario (igual que las listas)
print(len(medico))
print(len(paciente))

# MODIFICACIÓN DEL DICCIONARIO
# Agregar una clave nueva al diccionario paciente
paciente['telefono'] = '+56936361020'

print("===== FICHA PACIENTE CON TELEFONO ===== \n")
print(paciente)

# Sobrescribir y/o actualizar valor de una clave existente (Forma N°1)
paciente['edad'] = 20

print("\n===== FICHA PACIENTE CON EDAD ACTUALIZADA ===== \n")
print(paciente)

# Fusiona otro diccionario (o pares clave-valor) en el actual
# Útil para actualizar varios campos a la vez (actualizar varias claves)
paciente.update({'edad': 21, 'ciudad': 'Castro'})
print(paciente['edad'])
print(paciente['ciudad'])
print(paciente)

# Eliminar una clave sin retorno
del(paciente['informacion_extra'])
print(paciente)

# Eliminar una clave y retornar su valor (a diferencia de del, que no lo retorna) -> pop()
edad_eliminada = paciente.pop('edad')
print(f'Edad eliminada: {edad_eliminada}') # se recupera el valor antes de borrarla
print(paciente)

# OTRAS UTILIDADES DEL DICCIONARIO

# Con in se verifica si una clave existe en el diccionario (sin usar condicionales todavia)
print('nombre' in paciente)
print('rut' in paciente)

# Con copy() se crea una copia independiente del diccionario
paciente2 = paciente.copy()
paciente2['nombre'] = 'Javiera'
print(paciente['nombre'])
print(paciente2['nombre'])
print(paciente2)

# Con clear() elimina todos los elementos del diccionario, dejandolo vacio (a diferencia del() que elimina solo la clave)
medico2 = medico.copy()
print("\n===== DICCIONARIO COPIA (MEDICO2) ===== \n")
print(medico2)
medico2.clear()
print(medico2) # -> {}