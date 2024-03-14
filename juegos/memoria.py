import random
def memoria():
    numero = random.randint(0,99999999)
    print('Recuerda la siguiente secuencia de numeros')
    print(numero)
    print('Inserta la secuencia')
    adivina = int(input())
    if adivina == numero:
        print('Has acertado, tienes buena memoria')
    else:
        print('Sigue intentando')