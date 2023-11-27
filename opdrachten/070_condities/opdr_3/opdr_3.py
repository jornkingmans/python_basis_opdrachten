# Opdracht 3 condities
# Naam student: Jorn Kingmans
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd_groepen = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

leeftijd = int(input("Voer uw leeftijd in: "))

groep = None
for g in leeftijd_groepen:
    if leeftijd_groepen[g][0] <= leeftijd <= leeftijd_groepen[g][1]:
        groep = g
        break

if groep:
    korting = kortings_percentages[groep]
    toegangsprijs = normale_toegangsprijs * (1 - korting / 100)
    print(f"U behoort tot de groep {groep}")
    print(f"U krijgt {korting}% korting")
    print(f"U betaalt daarom {toegangsprijs}")
else:
    print("Leeftijdsgroep niet gevonden")
