def mocniny():
    a=int(input("Zadej mocněné číslo"))
    b= int(input("Zadej mocninu"))
    k= a**b
    print("Umocněné číslo je",k)
    
mocniny()

def podil():
    a1=int(input("Zadej dělené číslo"))
    b1=int(input("Zadej dělitele"))
    if b1==0:
        print(Chyba)
    else:
        k1=a1/b1
        print("Dělené číslo je",k1)
        
podil()