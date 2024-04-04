def suma (*cisla):
    soucet=0
    for cislo in cisla:
        soucet=soucet+cislo
    return soucet
    
x=suma(3,5,9,4,8)
print(f"součet čísel je {x}")