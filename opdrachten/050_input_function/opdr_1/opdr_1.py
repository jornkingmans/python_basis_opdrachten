# Opdracht 1 input function
# Naam student: Jorn Kingmans
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math

zijde1 = float(input("Geef de lengte van de eerste zijde: "))
zijde2 = float(input("Geef de lengte van de tweede zijde: "))

schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)

print("De lengte van de schuine zijde is:", schuine_zijde)

# de output van het laatste voorbeeld klopt niet helemaal geloof ik, er mist nog een 5 aan het einde, ik krijg de volgende output: 14.212670403551895. Iets met afronden te maken misschien?
