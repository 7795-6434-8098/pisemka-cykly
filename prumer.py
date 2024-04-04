def prumer (*cisla):
    if len(cisla)==0:
        return 0
    else:
        return sum(cisla)/len(cisla)
vypis=prumer(1,2,3)
print(f"Průměe čísla je:{vypis}")