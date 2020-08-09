from math import * # Pour importer la fonction sqrt

print("RESOLUTION D'UNE EQUATION DU SECOND DEGRE")

print("a.x^2 + b.x + c = 0") # Formule d'une equation du second degré

print("Entrer la valeur de a")
a = float(input("valeur de a : "))
print("Entrer la valeur de b")
b = float(input("valeur de b : "))
print("Entrer la valeur de c")
c = float(input("valeur de c : "))

if a == 0 :
    if b == 0 :
        if c == 0 : 
            print("Tous reels est une Solution")
        else :
            print("Pas de solution")
    else :
        print("L'equation admet une solution unique :", -b/a)
else :
    delta = b*b - 4*a*c
    print("delta =", delta)
    if delta > 0 :
        if b < 0 :
          x1 = (-b+sqrt(delta)/2*a) # Pour b etant negative
          x2 = c/a
        else :
          x1 = (-b-sqrt(delta)/2*a) # Pour b etant positive
          x2 = c/a
        print("Les deux solutions sont :", x1, " et ", x2)
    else :
        if delta == 0 :
            print("L'equation admet une double solution :", -b/2*a)
        else :
                if delta < 0 :
                    print("L'equation n'admet pas de solution")
        
    
    