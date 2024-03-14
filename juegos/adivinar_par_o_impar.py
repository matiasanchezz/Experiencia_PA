import random
def adivinar_par_o_impar():
    print('Ingresa en minusculas si crees que el numero sera par o impar')
    opcion = str(input())
    numero = random.randint(0,10000000000000000000000000000000000000000000)
    if numero%2 == 0 and opcion == 'par':
        print('Has acertado, el numero es par')
    elif numero%2 != 0 and opcion == 'impar':
        print('Has acertado, el numero es impar')
    else:
        print('Has fracasado, no adivinaste la naturaleza del numero')