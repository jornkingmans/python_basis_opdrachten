# Opdracht 2 lists
# Naam student: Jorn Kingmans
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

# Print de naam van de 1e rivier en het 2e land waar deze doorheen stroomt
print("De rivier", rivieren[0].title(), "stroomt onder andere door", rivier_info[rivieren[0]][1].title())

# Print de naam van de 2e rivier en het 1e land waar deze doorheen stroomt
print("De rivier", rivieren[1].title(), "stroomt onder andere door", rivier_info[rivieren[1]][0].title())

# Print de naam van de 3e rivier en het 3e land waar deze doorheen stroomt
print("De rivier", rivieren[2].title(), "stroomt onder andere door", rivier_info[rivieren[2]][2].title())

#hoofdletters zijn blijkbaar ook mogelijk met .capitalize zie ik op internet? Hoe zit dit precies?
