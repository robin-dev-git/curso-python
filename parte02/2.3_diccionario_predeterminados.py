from collections import defaultdict

versiones_lenguajes = defaultdict(lambda : '1.0.0')
versiones_lenguajes['Java'] = '17.0.0'
versiones_lenguajes['PHP'] = '7.1.2'
versiones_lenguajes['C#'] = '7.0.0'

print(len(versiones_lenguajes))
print(versiones_lenguajes)
print(versiones_lenguajes['Java'])
print(versiones_lenguajes['PHP'])
print(versiones_lenguajes['C#'])
print(versiones_lenguajes['Python']) # no existe version de la variable de lista

print('-'*80)

lenguajes = 'Python JavaScript PHP C# Java C++ C PHP PHP Python Pyhton JavaScript'
lenguajes = lenguajes.split()
print(lenguajes)

print('-'*80)

conteo_lenguajes = defaultdict(int)
for l in lenguajes:
    conteo_lenguajes[l] += 1

print(conteo_lenguajes)
print(conteo_lenguajes['Python'])
print(conteo_lenguajes['C'])
print(conteo_lenguajes['Kotlin'])

print('-'*80)

# Crear un diccionario preterminando con valoresL
puntajes = defaultdict(int, Edward= 80, Daniela= 85, Oliva= 90)
print(len(puntajes)) 
print()
print(puntajes['Edward'])
print(puntajes['Daniela'])
print(puntajes['Oliva'])
print(puntajes['Germán']) # No existe agregar un diccionario preterminando de lista.

puntajes['Germán'] = 75
print(puntajes['Germán']) # agregando un diccionario preterminando de lista.

print('-'*80)

for k, v in conteo_lenguajes.items():
    print('Llave : {} - Valor: {}'.format(k, v))


print('-'*80)

conteo_lenguajes = [print(f'Llave: {k} - Valor: {v}') for k, v in conteo_lenguajes.items()]

