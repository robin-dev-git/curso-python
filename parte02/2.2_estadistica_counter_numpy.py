from collections import Counter
import numpy as np
from scipy import stats



lista_letras = ['t', 'u', 't', 'w', 'x', 'x', 'w', 't', 'y', 'y', 'z']
contador = Counter(lista_letras)
print(contador)

print('-'*80)

dict_letra = {'t': 3, 'u': 1, 'w': 2, 'x': 2, 'y': 2, 'z': 1}
contador = Counter(dict_letra)
print(contador)

print('-'*80)

contador = Counter(t= 3, u= 1, w= 2, x= 2, y= 2, z= 1)
print(contador)

print('-'*80)

cadena = 'tutwxxwtyyz'
contador = Counter(cadena)
print(contador)

print('-'*80)

print(contador['x'])
print(contador.most_common(3))

print('-'*80)

for k, v in contador.most_common():
    print('Llave: {} - Valor: {}'.format(k, v) )

print('-'*80)

conteos = [v for k, v in contador.most_common()]
print(len(conteos))
print(conteos)

print('-'*80)

# Otras operaciones estadísticas:

promedio = np.mean(conteos)
mediana = np.median(conteos)
minimo = np.min(conteos)
maximo = np.max(conteos)

print('Prmedio: %f' % promedio)
print('Mediana: %f' % mediana)
print('Minimo: %f' % minimo)
print('Máxino: %f' % maximo)

print('-'*80)

# pip install scipy

print('-'*80)

moda = stats.mode(conteos)
print('Moda: {}'.format(moda.mode[0]))