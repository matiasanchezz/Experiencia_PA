from random import randint 
def adivinar_numero():
    condicion=0
    c=randint(1,10)
    while condicion!=1:
        n=int(input(""))
        if n==c:
            print("correcto")
            condicion+=1
        else:
            print("nope")