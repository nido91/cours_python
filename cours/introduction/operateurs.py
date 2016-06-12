# -*- coding: utf-8 -*-
from math import *

def exercice():
# differents opérateurs mathématiques (+, -, *, /, %, **, //)
    a, b, c = 15, 2.5, 8.

# somme et difference
    result = a + c - b
    print("Le résultat = :", result, "et le type :", type(result))

# multiplication et division
    result = a * b / c
    print("Le résultat = :", result, "et le type :", type(result))
    print(int(result))

# si on cast les variables séparéments la précision est perdue
    cast_result = a * int(b) / int(c)
    print("Le résultat = :", cast_result, "et le type :", type(cast_result))
    print("Ecart = ", result - cast_result)

# exposant
    print("surface cercle", a ** 2 * pi)  # pas besoin init pi car fait auto par import math

# opérateur division entiere et reste de la division (// et %)
    print("division entière:", a // b, "---", "reste ", a % b)
    print("division entière:", a // c, "---", "reste ", a % c)

# connaitre parité d'une valeur avec modulo pair si reste = 0
    print("Nombre c est pair:", c % 2)
    print("Nombre a est impair:", a % 2)

# Priorité des opérateurs de la plus haute à la plus basse :  (), exposant, multiplication ou division, addition ou soustraction
    print("parenthèse =", a * (b - c))
    print("parenthèse exposant", (a - (b - 0.5)) ** (c - 6))
    print("priorité exposant", a * 2 ** 3)

    x = 7 + 6 * 2 // 3  # ordre réel 6*2//3+7
    y = (7 + 6) * 2 // 3  # ordre réel 7+6*2//3
    print("resultat sans parenthèse", x, "\n", "valeur avec parenthèse", y)

# ----------------------- opérateur Boolean (True, False) -------------------
    GPIO_22 = 1

    Button_off = GPIO_22
# la condition if fonctionne pour Button_off = 1 sinon pour 0 c'est le else
    if Button_off:
        intrusion_garage = False
        intrusion_portail = True
        print("valeur 1 sur pin GPIO_22", Button_off, intrusion_garage, intrusion_portail)
    else:
        intrusion_garage = True
        intrusion_portail = False
        print("valeur 0 sur pin GPIO_22", Button_off, intrusion_garage, intrusion_portail)

# les differents opérateurs de comparaison (==, !=, >, <, >=, <=)
# opérateurs servant à des tests

    received_msg = "OK"

# traitement de la parité avec opérateur égal
    if a % 2 == 0:
        print(a, " est pair car le reste est nul")
    else:
        print(a, " est impair")

# utilisation opérateur différent
    if received_msg != "fin":
        print("Erreur le message reçu est mauvais")
    else:
        print(received_msg)

    return received_msg, Button_off
# utilisation de comparaisons imbriquées if elif (else if) avec de oprateurs logiques (and, or)
# si triangle constructible test du type de triangle
#  si 3 côtes egaux (equilatéral)
#  sinon si 2 côtes egaux (isocèle)
#  sinon si pythagore OK (rectangle)
#  sinon triangle quelconque
# sinon triangle impossible

cote_a, cote_b, cote_c = 5, 6, 9  # triangle quelconque
# cote_a, cote_b, cote_c = 6, 6, 9        #triangle isocèle
# cote_a, cote_b, cote_c = 5, 5, 5        #triangle équilatéral
# cote_a, cote_b, cote_c = 5, 4, 3        #triangle rectangle
# cote_a, cote_b, cote_c = 5, 6, 12        #triangle impossible

if cote_a < cote_b + cote_c and cote_b < cote_a + cote_c and cote_c < cote_a + cote_b:
    print("c'est un triangle")
    if cote_a == cote_b and cote_b == cote_c:
        print("Ce triangle est équilatéral")
        print("Le périmètre =", cote_a + cote_b + cote_c)
    elif cote_a == cote_b or cote_a == cote_c or cote_b == cote_c:
        print("Ce triangle est isocèle")
        print("Le périmètre =", cote_a + cote_b + cote_c)
    elif cote_a ** 2 + cote_b ** 2 == cote_c ** 2 or cote_a ** 2 + cote_c ** 2 == cote_b ** 2 or cote_b ** 2 + cote_c ** 2 == cote_a ** 2:
        print("Ce triangle est rectangle")
        print("Le périmètre =", cote_a + cote_b + cote_c)
    else:
        print("C'est un triangle quelconque")
        print("Le périmètre =", cote_a + cote_b + cote_c)
else:
    print("Impossible de construire ce triangle car un côté est > à la somme des 2 autres")
