def suma (*cisla):
    soucet=0
    for cislo in cisla:
        soucet=soucet+cislo
    print(f"Součet čísel {soucet}")
    
suma(3,5,9,4,8)