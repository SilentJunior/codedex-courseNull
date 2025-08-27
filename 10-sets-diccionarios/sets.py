""" 
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni indice ni orden
"""

personas = {
    'Jose',
    'Jo',
    'Gar'
}

personas.add('Nav')
personas.add('Arro')
personas.remove('Arro')

print(type(personas))
print(personas)
