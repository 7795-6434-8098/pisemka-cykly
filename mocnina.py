x=int(input("Zadej číslo, které chceš umocňovat"))
n=int(input("Zadej číslo, kterým chceš umocňovat"))
h=x
for i in range(n-1):
    h=h*x
print("Umocněné číslo je",h)