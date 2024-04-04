def sude_liche(cislo):
    if cislo%2==0:
        return "sudé"
    else:
        return "liché"
        
    
print(f"Číslo je {sude_liche(5)}")