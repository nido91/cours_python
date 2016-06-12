# -*- coding: utf-8 -*-
from math import pi

#Nouvelles structures de données composites (liste [])

inventaire = ['PC', 'Clavier', 'Souris', 'écran', 'disque dur', 'clé USB', 'Windows']
liste_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août',
              'Septembre', 'Octobre','Novembre', 'Décembre']
nbre_jours_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
liste_chiffre = [12, 34, 56.6, 78, 98, 76, 54, 32.0, 10, 15, 36, 5, 8, 45.5, 1, 6, 0.5, 75]
liste_composite = ['Linux', 'Octobre', 12800, True, 76.2, pi, 'Lundi', 'Jeudi']

#Opérations sur les listes (connaitre taille)
for i in range(len(inventaire)):
    print(inventaire[i], "  nombre de lettres dans", inventaire[i], "=", len(inventaire[i]))

#modification des termes d'une liste
liste_composite[2] = liste_composite[2] + liste_chiffre[4]
liste_composite[0] = inventaire[6]
print(liste_composite)


# concaténation de 2 listes avec methode append (ajout)
liste_mois_jour = []                                    #initialisation de la nouvelle liste
index = 0
while index < len(nbre_jours_mois):
    liste_mois_jour.append(liste_mois[index])
    liste_mois_jour.append(nbre_jours_mois[index])
    index += 1
print(liste_mois_jour)


# recherche du + grand et plus petit élément d'une liste
index, major = 0, 0
minor = liste_chiffre[0]                            #init de la variable avec 1ere donnée de la liste

while index < len(liste_chiffre):
     if major < liste_chiffre[index]:
         major = liste_chiffre[index]
     elif minor > liste_chiffre[index]:
         minor = liste_chiffre[index]
     index += 1

print(" Le chiffre le plus grand de la suite:", liste_chiffre, "est :", major)
print(" Le chiffre le plus petit de la suite:", liste_chiffre, "est :", minor)

# séparer les éléments pairs et impairs d'une liste
liste_pair = []
liste_impair = []
index = 0

while index < len(liste_chiffre):
    if liste_chiffre[index] % 2 == 0:
        liste_pair.append(liste_chiffre[index])
    else:
        liste_impair.append(liste_chiffre[index])
    index += 1

print("Liste pair", liste_pair)
print("Liste impair", liste_impair)


# tri à bulles     tri croissant par permuttation
permutation = True
index, pointeur = 0, 0
courant = 0

while permutation:
    permutation = False
    for index in range(len(liste_chiffre) - 1):
        courant = liste_chiffre[index]
        pointeur = index + 1
        if liste_chiffre[index] > liste_chiffre[pointeur]:
            liste_chiffre[index] = liste_chiffre[pointeur]
            liste_chiffre[pointeur] = courant
            permutation = True

print("Liste croissante", liste_chiffre)

# tri à bulles     tri decroissant par permuttation
permutation = True
index, pointeur = 0, 0
courant = 0

while permutation:
    permutation = False
    for index in range(len(liste_chiffre) - 1):
        courant = liste_chiffre[index]
        pointeur = index + 1
        if liste_chiffre[index] < liste_chiffre[pointeur]:
            liste_chiffre[index] = liste_chiffre[pointeur]
            liste_chiffre[pointeur] = courant
            permutation = True

print("Liste décroissante", liste_chiffre)

#créer une liste de chiffre entrée au clavier et arrêt par touche "entrée"
liste_ch = []
ch = "None"                             #initialise la variable ch à ch non vide
while ch != "":
    ch = input("Entrez une valeur")
    if ch != "":
        liste_ch.append(float(ch))
print("Voici la liste", liste_ch)

#optimisation (ch:) vérif si chaine non vide
liste_ch = []

while ch:
    ch = input("Entrez une valeur")
    if ch:
        liste_ch.append(float(ch))
print("Voici la liste", liste_ch)