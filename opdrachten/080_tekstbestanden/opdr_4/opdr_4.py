# Opdracht 4 Tekst opslaan
# Naam student: Jorn Kingmans
# Groep:


# Party enquete

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

antwoorden = {}

for i, vraag in enumerate(vragen, start=1):
    antwoord = input(f"{i}. {vraag}\n")
    sleutel = vraag.split()[-1].lower()
    antwoorden[sleutel] = antwoord

print("\nBedankt voor het invullen!\nSee you at the party.")

pad = r"C:\temp\feestgangers.txt"
with open(pad, "w") as bestand:
        bestand.write("----\n")
        for sleutel, waarde in antwoorden.items():
            bestand.write(f"{sleutel}: {waarde}\n")

# hier had ik telkens het probleem dat de bedanktekst na elke vraag terug kwam,
# dit gefixt door de print functie te verplaatsen zodat hij niet meer in de for-loop staat
