import json
import pickle

datos = {}
datos['programadores'] = []

edward = {'id': 1001, 'nombre': 'Edward', 'apellido': 'Ortiz', 'especialidad': 'font-end', 'lenguaje': 'JavaScript', 'email': 'edward@mail.co'}

oliva = {'id': 1002, 'nombre': 'Oliva', 'apellido': 'Ordoñez', 'especialidad': 'back-end', 'lenguaje': 'Java', 'email': 'oliva@mail.co'}

juan = {'id': 1003, 'nombre': 'Juan', 'apellido': 'Urbano', 'especialidad': 'font-end', 'lenguaje': 'JavaScript', 'email': 'juan@mail.co'}

datos['programadores'].append(edward)
datos['programadores'].append(oliva)
datos['programadores'].append(juan)

print(len(datos['programadores']))

# Escribe los datos en un archivo JSON:
with open('parte01/programadores.json', 'w') as f:
    json.dump(datos, f)

print()

# Lectura de los datos de un archivo JSON:
with open('parte01/programadores.json', 'r') as f:
    datos_programadores = json.load(f)

print(len(datos_programadores['programadores']))

for p in datos_programadores['programadores']:
    print('ID: %i' % p['id'])
    print('Nombre: %s' % p['nombre'])
    print('Apellido: %s' % p['apellido'])
    print('Especialidad: %s' % p['especialidad'])
    print('Lenguaje: %s' % p['lenguaje'])
    print('Email: %s' % p['email'])
    print()

print()

# Persistencia en un archivo binario:
with open('parte01/programadores.pkl', 'wb') as f:
    pickle.dump(datos, f, protocol=pickle.HIGHEST_PROTOCOL)

# Lectura de un archivo binario:
with open('parte01/programadores.pkl', 'rb') as f:
    datos_deserializados = pickle.load(f)

print(type(datos_deserializados))
print(datos_deserializados)

print()

for p in datos_deserializados['programadores']:
    print('ID: %i' % p['id'])
    print('Nombre: %s' % p['nombre'])
    print('Apellido: %s' % p['apellido'])
    print('Especialidad: %s' % p['especialidad'])
    print('Lenguaje: %s' % p['lenguaje'])
    print('Email: %s' % p['email'])
    print()
