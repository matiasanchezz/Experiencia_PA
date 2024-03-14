from random import *

def cachipun(eleccion):
    lista = ['piedra', 'papel', 'tijera']
    a = randint(0,2)
    b = lista[a]
    if eleccion == b:
        return cachipun(eleccion)
    elif eleccion == 'tijera' and b == 'piedra':
        return 'Perdiste'
    elif eleccion == 'tijera' and b == 'papel':
        return 'Ganaste'
    elif eleccion == 'piedra' and b == 'papel':
        return 'Perdiste'
    elif eleccion == 'piedra' and b == 'tijera':
        return 'Ganaste'
    elif eleccion == 'papel' and b == 'tijera':
        return 'Perdiste'
    elif eleccion == 'papel' and b == 'piedra':
        return 'Ganaste'
    