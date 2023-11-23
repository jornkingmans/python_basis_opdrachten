# Opdracht 3 input functie
# Naam student: Jorn Kingmans
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

for i in range(3, 82, 3):
    resultaat = (i**2) / 3
    if resultaat > 2028.2:
        break
    my_list.append(resultaat)

print (my_list)
