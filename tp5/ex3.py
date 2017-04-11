# 1) imports
import math

# 2) définitions de fonctions


def input_liste(texte, sep):
	liste = input(texte).split(sep)
	return liste


def en_float(liste):
	for i in range(len(liste)):
		float(liste[i])
	return liste


def au_carre(liste):
	for i in range(len(liste)):
		liste[i] = float(liste[i]) ** 2
	return liste


def afficher_liste_multiligne(liste):
	for i in range(len(liste)):
		print(i+1,"-",liste[i])
	print("Total :",sum(liste))

def input_liste_nombres():
    entrees = input_liste("Nombres (séparés par des espaces) : ", " ")
    valeurs = en_float(entrees)
    return valeurs

    
# 3 et 4) programme principal

def principale():
	nbrs = input_liste_nombres()
	carres = au_carre(nbrs)
	afficher_liste_multiligne(carres)

principale()