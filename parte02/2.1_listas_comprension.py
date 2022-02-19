<<<<<<< HEAD
numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(type(numeros))
print(len(numeros))
print(numeros)

print('-'*50)

pares_triplicados = []

for n in numeros:
    if n % 2 == 0:
        pares_triplicados.append(n * 3)

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

print('-'*50)

pares_triplicados = [n * 3 for n in numeros if n % 2 == 0]

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

print('-'*50)

# Solución con ciclos for (iterativa):
numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [2, 7, 13, 19, 23, 3]
interseccion = []

for  n1 in numeros_1:
    for n2 in numeros_2:
        if n1 == n2 and n1 not in interseccion:
            interseccion.append(n1)

print(len(interseccion))
print(interseccion)

print('-'*50)

# Solución con listas comprensión:
interseccion = []
resultado = [n1 for n2 in numeros_2 for n1 in numeros_1 if n1 == n2 and n1 not in interseccion]

print(len(resultado))
print(resultado)

print('-'*50)

resultado = set(numeros_1) & set(numeros_2)
print(len(resultado))
print(resultado)

=======
numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(type(numeros))
print(len(numeros))
print(numeros)

print('-'*50)

pares_triplicados = []

for n in numeros:
    if n % 2 == 0:
        pares_triplicados.append(n * 3)

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

print('-'*50)

pares_triplicados = [n * 3 for n in numeros if n % 2 == 0]

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

print('-'*50)

# Solución con ciclos for (iterativa):
numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [2, 7, 13, 19, 23, 3]
interseccion = []

for  n1 in numeros_1:
    for n2 in numeros_2:
        if n1 == n2 and n1 not in interseccion:
            interseccion.append(n1)

print(len(interseccion))
print(interseccion)

print('-'*50)

# Solución con listas comprensión:
interseccion = []
resultado = [n1 for n2 in numeros_2 for n1 in numeros_1 if n1 == n2 and n1 not in interseccion]

print(len(resultado))
print(resultado)

print('-'*50)

resultado = set(numeros_1) & set(numeros_2)
print(len(resultado))
print(resultado)

>>>>>>> 8113dfd2700952f2bf17cd720b08ef02e77afbcd
