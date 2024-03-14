import random
def juego_del_dado():
    suma1 = 0
    suma2 = 0
    while suma1 < 30 and suma2 < 30:
        print('')
        print('Aprieta enter para tirar el dado')
        boton = input()
        numero1 = random.randint(1,6)
        print('Has obtenido el numero', numero1)
        suma1 += numero1
        numero2 = random.randint(1,6)
        print('Tu rival ha obtenido el numero', numero2)
        suma2 += numero2
    if suma1 >= 30:
        print('Has ganado con', suma1, 'puntos')
    elif suma2 >= 30:
        print('Tu rival ha ganado con', suma2, 'puntos')
