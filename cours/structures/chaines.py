# -*- coding: utf-8 -*-

# Différentes manipulation possible avec les données de type string délimitées par des ""
texte1 = "Quel est votre prénom ? "
texte2 = "Je m'appelle Jean"                #entre les " on écrit le texte normalement
texte3 = 'le message reçu est: "OK"'        #pour que OK s'affiche entre " il faut que la phrase soit délimitée par '

print(texte1, texte2)                       #le texte2 démarre avec un blanc dû à la fonction print
print(texte1 + texte2)                      #concaténation texte1 et texte2
print(texte3)

#utilisation de \n pour saut de ligne
print(texte1, "\n", texte2)                 #le texte2 démarre après un saut de ligne avec un blanc cf. fct. print
print(texte1 + "\n" + texte2)               #concaténation texte1 saut de ligne et texte2

#remplace le séparateur standard par un caractère choisi
print(texte1, texte2, sep="| ")             #ajoute un - entre les 2 phrases

#suppression du saut à la ligne par l'argument end=""
i = 0
while i < 5:
    print(texte3, end="--")                 #remplacement du saut de ligne par --
    i += 1

#Extraction d'un caractère ou d'un fragment d'une chaîne
caract = texte1
msg_radio_recu = "1234567891446710055"
semaphore = False

print("\n", caract[0], caract[2], caract[5], caract[13], caract[17], caract[22])  #extrait 1 car par 1 car

if msg_radio_recu[9:17] == "14467100":                                      #extrait d'un fragment
    semaphore = True
    print("le message reçu", msg_radio_recu, "est", semaphore)


#Opérations élémentaires sur les chaînes (concaténation
repertoire = "/home/pi/Majordome/MJDprg/"
nom_fichier = "chaine"
option = ".py"
concat = repertoire + nom_fichier + option

print(repertoire + nom_fichier + option)
print(concat)
print(caract[0] + caract[2] + caract[5] + caract[13] + caract[17] + caract[22])

#connaître longueur d'une chaîne  (len)
print("Le texte suivant: ", concat, "\n", "contient", len(concat), "lettres")   #la sortie est de type int

#afficher le nombre de voyelles contenues dans un texte
i, cpt_voy1, cpt_voy2 = 0, 0, 0
voy1, voy2 = "a", "e"
while i < len(caract):
    if caract[i] == voy1:
        cpt_voy1 = cpt_voy1 + 1
    elif caract[i] == voy2:
        cpt_voy2 = cpt_voy2 + 1
    i += 1
print("le nombre de fois que la lettre", voy1, "est présente dans le texte est :", cpt_voy1)
print("le nombre de fois que la lettre", voy2, "est présente dans le texte est :", cpt_voy2)

#parcours d'une chaîne avec insertion d'un caractère
index = 1
new_caract = caract[0]                                  #init avec 1er caractère
while index < len(caract):
    new_caract = new_caract + "_" + caract[index]
    index += 1
print(new_caract)

#inversion d'une phrase (methode avec boucle)
i = len(caract) - 1
phrase_inverse = ""

while i >= 0:
    phrase_inverse = phrase_inverse + caract[i]
    i -= 1
print("la phrase inverse :", phrase_inverse)
if caract == phrase_inverse:
    print("Le mot ou phrase", caract, " est un palindrome")
else:
    print("Ce mot ou cette phrase n'est pas un palindrome")

#inversion d'une phrase (méthode pythoneste)
print(caract[::-1])

#conversion d'une chaîne en nombre
mot_passe = '3586'                          #type string
offset = 91                                 #type int
#pour faire addition il faut convertir en type int la chaîne
mot_passe_int = int(mot_passe)
print(mot_passe_int + offset)

#fonction intéractive avec l'utilisateur (input)
prenom = input(texte1)                               #attente entrée clavier
chiffre = input(" Entrez un chiffre entre 0 et 9  ")    #le type retourné par input est string

print(prenom, "Le cube de", chiffre, "vaut ", int(chiffre)**3)  #besoin de transformer type string en int pour opération

