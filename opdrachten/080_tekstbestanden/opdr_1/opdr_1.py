# Opdracht 1 while-loops
# Naam student: Jorn Kingmans
# Groep:

# Jouw code komt hier

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []
for vraag in vragen:
    antwoord = input(vraag + "\n")
    antwoorden.append(antwoord)

    bestandspad = r"C:\temp\enquete_resultaten.txt"
    with open(bestandspad, "w") as bestand:
        for vraag, antwoord in zip(vragen, antwoorden):
            bestand.write(vraag + "\n" + antwoord + "\n\n")

print("De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")
