# -*- coding: utf-8 -*-
from math import pi, sin, cos

#-------------- les différentes boucles (while, for in range)---------------
#                Attention une boucle infinie ==> while 1:

#boucle while  (tant que condition vraie faire)
loop = 1

while loop:
    msg_recu = input("entrez mot fin pour rester dans la boucle ")
    if msg_recu != "fin":
        print("Erreur de réception")
        loop = 0                                                #arrêt de la boucle
print("sortie de boucle")

#utilisation de while pour écrire des tables
# calcul des carrés et cubes des nombres de 1 à 10

x, taille = 1, 10

while x < taille:
    print("nombre" ,x, " son carré = ", x**2, "  et son cube = ", x**3)
    x = x + 1

# suite dont chaque terme est égal à la somme des 2 termes qui le précède
# pour avoir les éléments d'une liste à la queue leu leu il faut ajouter une virgule (b,)
# pour la suppression du saut de ligne utiliser  end (end(" ")

a, b, i, taille = 1, 1, 1, 10
print("Suite de Fibonacci")
while i < taille:
    print(b, end="  ")
    a, b, i = b, a + b, i + 1
print("\n")

#---------------- boucle for cpt in range (départ et fin) ---------------
depart, fin, delta = 1, 5, 10.
angle = float(input("Entrez une valeur d'angle en ° : "))
alfa_rad = angle * 2 * pi / 360

print("La valeur en radian de", angle, "° est de: ", alfa_rad)

for i in range(depart, fin):
    print("Pour", angle, "°", "le sinus vaut:", sin(alfa_rad), "et le cosinus:", cos(alfa_rad))
    angle = angle + delta

#------ boucle itérative de 0 à fin -------------
for i in range(fin):
    print("i= ", i)
print("\n")

#------------ boucle de décomptage (depart à arrivée taille d'incrément) ------
for i in range(15, 2, -2):
    print("i= ", i)