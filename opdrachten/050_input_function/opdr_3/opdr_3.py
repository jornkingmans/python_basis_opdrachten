# Opdracht 3 input functie
# Naam student: Jorn Kingmans
# Groep:

# Hier komt je code...

steden = []

for i in range(5):
    stad = input(f"Voer stad nummer {i+1} in: ")
    steden.append(stad)

steden.sort(reverse=True)

print(steden)
