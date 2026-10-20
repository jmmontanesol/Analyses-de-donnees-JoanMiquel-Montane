# coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
from pathlib import Path

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding='utf-8') as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

# Question 2
print("Question 2")
iles = ouvrirUnFichier("data/island-index.csv")
print(iles)

# Question 3
print("\nQuestion 3")
df = pd.DataFrame({
    "Identifiant": iles["Identifiant"],
    "Surface (km²)": iles["Surface (km²)"],
})
# Nouvelle ligne à ajouter
nouvelle_ligne = pd.DataFrame({"Identifiant": ["Asie/Afrique/Europe", "Amérique", "Antarctique", "Australie"], "Surface (km²)": [85545323, 37856841, 7768030, 7605049]})
df = pd.concat([df, nouvelle_ligne], ignore_index=True)
print("\nDataFrame après ajout de la nouvelle ligne :")
print(df)

# Question 4
print("\nQuestion 4")

# Question 5
print("\nQuestion 5")
Path("img").mkdir(exist_ok=True)

# Question 6
print("\nQuestion 6")


# Question 7
print("\nQuestion 7")
# Mettre ici votre réponse argumentée

# Question 9
print("\nQuestion 9")

# Question 10
print("\nQuestion 10")

# Question 11
print("\nQuestion 11")

# Question 12
print("\nQuestion 12")

# Question 13
print("\nQuestion 13")

# Question 14
print("\nQuestion 14")
