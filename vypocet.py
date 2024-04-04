def vypocet(a,b,x):
    if x == "+":
        vysledek=a+b
        print(f"Výsledek dělení je {vysledek}")
    elif x=="/":
        if b==0:
            print("Chyba")
        else:
            vysledek=a/b
            print (f"Výsledek dělení je {vysledek}")
vypocet(540,684,"+")
vypocet(12,24,"/")
vypocet(1224,0,"/")
