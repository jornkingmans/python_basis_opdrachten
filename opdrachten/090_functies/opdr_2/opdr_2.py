# Opdracht 1 functies
# Naam student: Jorn Kingmans
# Groep:


def kilometers_naar_miles(km):
    """
    Zet kilometers om naar miles.
    
    Args:
    kilometers: Het aantal kilometers.

    Returns:
    Het aantal miles.
    """
    miles = kilometers / 1.609344
    return miles

def miles_naar_kilometers(miles):
    """
    Zet miles om naar kilometers.
    
    Args:
    miles: Het aantal miles.

    Returns:
    Het aantal kilometers.
    """
    kilometers = miles * 1.609344
    return kilometers

kilometers = 1223
miles = 867
omgezette_miles = kilometers_naar_miles(kilometers)
omgezette_km = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {omgezette_miles} miles")
print(f"{miles} miles = {omgezette_km} kilometers")
