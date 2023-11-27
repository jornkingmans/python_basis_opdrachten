# Opdracht 4 condities
# Naam student: Jorn Kingmans
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

gevonden = False
for topping in toppings:
    if topping[0] == keuze:
        print(f"U heeft {keuze} besteld. Dat kost {topping[1]}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in osn assortiment")
