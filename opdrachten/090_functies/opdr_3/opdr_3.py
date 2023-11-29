# Opdracht 1 functies
# Naam student: Jorn Kingmans
# Groep:


import math

def kubus_vol(m):
    """
    Bereken het volume van een kubus.

    Args:
    m: De lengte van de zijden van de kubus.

    Returns:
    Het volume van de kubus.
    """
    return m ** 3

def bol_vol(r):
    """
    Bereken het volume van een bol.

    Args:
    r: De straal van de bol.

    Returns:
    Het volume van de bol.
    """
    return (4/3) * math.pi * r ** 3

kubus_volume = kubus_vol(5)
bol_volume = bol_vol(4)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")
