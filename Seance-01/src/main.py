"""Exercices personnels - initiation a Python, M1 EnviTERR.

Exercices realises pendant la prise en main, regroupes dans un seul fichier.
"""

print("\n1. PREMIERS AFFICHAGES ET COMMENTAIRES")
# Python ignore cette ligne de commentaire.
print("Analyse de donnees geographiques")
print("Etude des temperatures en montagne")
print(2500)

print("\n2. VARIABLES ET TYPES")
altitude = 7134
massif = "Pamir"
temperature = -12.5
neige = True
print("Altitude :", altitude, "m ; massif :", massif)
print("Types :", type(altitude), type(temperature), type(massif), type(neige))
altitude = altitude + 100  # Reaffectation (exemple fictif)
print("Altitude apres ajout de 100 m :", altitude)

print("\n3. CONVERSION ET SAISIE")
altitude_texte = "4400"
altitude_camp = int(altitude_texte)
print("Altitude convertie : {} m".format(altitude_camp))
# Variante interactive deja etudiee (a activer si tu souhaites saisir la valeur) :
# altitude_camp = int(input("Altitude du camp en metres : "))
SOMMET = 7134
difference = SOMMET - altitude_camp
print("La difference d'altitude entre le sommet et le camp est de {} metres.".format(difference))

print("\n4. OPERATEURS : STATIONS METEOROLOGIQUES")
altitude_A = 3200
altitude_B = 4400
temperature_A = -4
temperature_B = -11
difference_altitude = altitude_B - altitude_A
difference_temperature = temperature_B - temperature_A
print("Difference d'altitude : {} metres".format(difference_altitude))
print("Difference de temperature (B - A) : {} degres C".format(difference_temperature))
print("B > 4000 m et B < 0 degre C ?", altitude_B > 4000 and temperature_B < 0)
print("A > 4000 m ou A < 0 degre C ?", altitude_A > 4000 or temperature_A < 0)

print("\n5. CONDITIONS : CLASSER UNE STATION")
# Pour remplacer par une saisie interactive :
# altitude_station = int(input("Altitude de la station (m) : "))
altitude_station = 3000
if altitude_station < 1500:
    print("Basse altitude")
elif 1500 <= altitude_station < 3000:
    print("Moyenne altitude")
else:
    print("Haute altitude")

print("\n6. BOUCLE FOR : ALTITUDE DES CAMPS")
camps = [3600, 4400, 5300, 6100]
for altitude in camps:
    print("Le camp se situe a {} metres d'altitude.".format(altitude))

print("\n7. FOR + CONDITION : CLASSER LES CAMPS")
for altitude in camps:
    if altitude < 5000:
        print("Camp de basse altitude :", altitude)
    else:
        print("Camp de haute altitude :", altitude)

print("\n8. BOUCLE WHILE : MONTEE PAR PALIERS")
altitude = 3600
while altitude < 6000:
    print("Altitude actuelle :", altitude)
    altitude += 500
print("Altitude atteinte apres la boucle :", altitude)

print("\n9. BREAK ET CONTINUE")
print("Break : arret au premier camp >= 5000 m")
for altitude in camps:
    if altitude >= 5000:
        break
    print(altitude)
print("Continue : ne pas afficher le camp de 4400 m")
for altitude in camps:
    if altitude == 4400:
        continue
    print(altitude)

print("\n10. FONCTIONS : DIFFERENCE D'ALTITUDE")
def difference_altitude_fonction(sommet, camp):
    return sommet - camp

resultat = difference_altitude_fonction(7134, 4400)
print("Denivele : {} m".format(resultat))

print("\n11. FONCTION : TEMPERATURE MOYENNE")
temperature_A = -8
temperature_B = -12
temperature_C = -4

def moyenne_temperature(a, b, c):
    temperature = (a + b + c) / 3
    return temperature

temperature = moyenne_temperature(temperature_A, temperature_B, temperature_C)
print("Temperature moyenne : {} degres C".format(temperature))

print("\nFIN DES EXERCICES\n")