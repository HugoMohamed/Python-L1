# 1) imports
from qtido import *
from outils import que_des_zeros, afficher_grille
from outils import init_boucle_deux_iterations, init_stable, init_devient_stable_en_trois, init_se_deplace_jusquau_bord
import copy

# 2) définitions de fonctions
# fonction qui renvoie le nombre de voisin d'une cellule
def nb_voisin(courant, y, x):
	voisin=0
	for ligne in range(-1, 2):
		for colonne in range(-1, 2):
			if courant[y+colonne][x+ligne]>=1:
				voisin+=1
	if courant[y][x]>=1:
		return voisin-1
	else:
		return voisin

# fonction qui affiche la grille et permet accessoirement d'ajouter l'age des cellules
def grillage(grille,f,H,L):
	for k in range(1,40):
		couleur(f, 0, 0, 1)
		ligne(f, k*20, 0, k*20, 300)
		ligne(f, 0, k*20, 400, k*20)
	afficher_grille(f,grille)
		
	for y in range(1, H-1):
		for x in range(1, L-1):
			if grille[y][x]>0:
				couleur(f, 1, 0, 0)
				texte_centre(f, 20*x+10, 20*y+15, 12, str(grille[y][x]))
		re_afficher(f)
        
def evolution(courant, H, L):
    # l'état suivant est VIDE pour l'instant
	suivant = que_des_zeros(H, L) # état suivant
	# on considère toutes les cases, sauf les bords (celà simplifie les choses)
	for y in range(1, H-1):
		for x in range(1, L-1):
		        # règle simple et juste cette fois
			age=courant[y][x]
			if courant[y][x]>0:
				if (nb_voisin(courant, y, x)<2 or nb_voisin(courant, y, x)>3): #meurt
					suivant[y][x]=0
				else:#survivre
					age+=1
					suivant[y][x]=age
			elif courant[y][x]==0 and nb_voisin(courant, y, x)==3: #naissance
				suivant[y][x]=1
	return suivant


# 3 et 4) programme principal

# état initial
def principale():
	H = 15
	L = 20
	f = creer(400, 300)
	grille = que_des_zeros(H, L)
	#init_boucle_deux_iterations(grille)
	#init_stable(grille)
	#init_devient_stable_en_trois(grille)
	init_se_deplace_jusquau_bord(grille)
	age=0
	grillage(grille,f,H,L)
	attendre_pendant(f,1000)
		
	while not est_fermee(f):
		# affichage
		effacer(f)
		grillage(grille,f,H,L)
		re_afficher(f)
		# événements
		attendre_evenement(f, 1000)
		e = dernier_evenement(f)
		if e == 16777216: # touche ECHAP
				exit()
		grille = evolution(grille, H, L)
		re_afficher(f)
principale()
