#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")
print("Résultat sur le calcul d'un intervalle de fluctuation")
echantillons = ouvrirUnFichier("data/Echantillonnage-100-Echantillons.csv")
print(echantillons)
# calcul de la moyenne pour chaque colonne
moyenne_pour = round(echantillons["Pour"].mean(), 0)
print("Moyenne des personnes pour :", moyenne_pour)
moyenne_contre = round(echantillons["Contre"].mean(), 0)
print("Moyenne des personnes contre :", moyenne_contre)
moyenne_sans_opinion = round(echantillons["Sans opinion"].mean(), 0)
print("Moyenne des personnes sans opinion :", moyenne_sans_opinion)

# calcul somme moyennes
total = moyenne_pour + moyenne_contre + moyenne_sans_opinion
# calcul fréquences
frequence_pour = round(moyenne_pour / total, 2)
frequence_contre = round(moyenne_contre / total, 2)
frequence_sans_opinion = round(moyenne_sans_opinion / total, 2)
print("Fréquence Pour :", frequence_pour)
print("Fréquence Contre :", frequence_contre)
print("Fréquence Sans opinion :", frequence_sans_opinion)

# calcul fréquences pop mère
population_pour = 852
population_contre = 911
population_sans_opinion = 422
total_population = 2185
frequence_population_pour = round(population_pour / total_population, 2)
frequence_population_contre = round(population_contre / total_population, 2)
frequence_population_sans_opinion = round(population_sans_opinion / total_population, 2)
print("Fréquence Pop mère Pour :", frequence_population_pour)
print("Fréquence Pop mère Contre :", frequence_population_contre)
print("Fréquence Pop mère Sans opinion :", frequence_population_sans_opinion)


# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")
print("Résultat sur le calcul d'un intervalle de confiance")

# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")

# Question bonus
print("Question bonus")
