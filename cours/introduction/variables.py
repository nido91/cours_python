# -*- coding: utf-8 -*-

import datetime

def exercice():

#----------affectation de variables--------
# sous Python le typage est dynamique voir ci-dessous
    librairie = "Montlhéry"                      #type string
    hote = "localhost"
    heure_ouverture = datetime.time(9, 00)       #type date
    heure_fermeture = datetime.time(16, 30)
    nbre_livres = 120                            #type int
    port = 12800
    prix_adherent = 52.68                        #type float
    reduction = 20.68

#affectation multiple et de type different
    init_cpt, ouverture = 0, True                #type int et Boolean
    prix_etudiant = prix_adherent - reduction


#affichage d'une donnée avec la fonction print()
    print("affiche le prix étudiant : ", prix_etudiant, "€")

    return librairie, heure_fermeture, nbre_livres, prix_etudiant, ouverture

