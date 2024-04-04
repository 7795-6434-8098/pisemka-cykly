from math import ceil

def nater():
    a=int(input("Zadej šířku plotu"))
    b=int(input("Zadej délku plochy"))
    plocha=a*b
    pl=ceil(plocha/5)
    print ("Na vypalování tohoto plotu budeš potřebovat",pl,"plechovek. (1 plechovka - 5 m2)")


nater()
