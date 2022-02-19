import gevent

def fn1():
    print('Inicio: fn1')
    gevent.sleep(0)
    print('Fin: fn1')

def fn2():
    print('Inicio: fn2')
    gevent.sleep(0)
    print('Fin: fn2')

def fn3():
    print('Inicio: fn3')
    gevent.sleep(0)
    print('Fin: fn3')

funciones = [gevent.spawn(fn1), gevent.spawn(fn2), gevent.spawn(fn3)]

gevent.joinall(funciones)

print()

# Funciones concurrentes con solicitud de datos del usuario:

def cuadrado():
    print('Inicio funcion: Cuadrado')
    numero = int(input('Ingrese un número para elvar al cuadrado: '))
    gevent.sleep(0)
    resultado = numero ** 2
    print('El cuadrado es: %i' % resultado)

def cubo():
    print('Inicio funcion: cubo')
    numero = int(input('Ingrese un número para elvar al cubo: '))
    gevent.sleep(0)
    resultado = numero ** 3
    print('El cuadrado es: %i' % resultado)

gevent.joinall([gevent.spawn(cuadrado), gevent.spawn(cubo)])
