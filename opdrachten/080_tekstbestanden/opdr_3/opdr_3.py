# Opdracht 3 Tekst opslaan
# Naam student: Jorn Kingmans
# Groep:

def encrypt_tekst(tekst, verschuiving):
    resultaat = ""
    for teken in tekst:
        if teken.isalpha():
            code = ord(teken.lower()) + verschuiving
            if code > ord('z'):
                code -= 26
            resultaat += chr(code)
        else:
            resultaat += teken
    return resultaat

invoer_tekst = input("Geef de tekst die je wilt encrypten:\n")

encrypted_tekst = encrypt_tekst(invoer_tekst, 5)

print("Geëncrypteerde tekst:", encrypted_tekst)
