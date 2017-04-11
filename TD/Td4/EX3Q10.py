from math import *
from exo3 import *

def principale():
	
	liste = input_floats()
	ordre = liste[0]
	
	liste = liste_floats(tousSaufUn(liste))
	
	if ordre == "somme":
		resultat = sum(liste)
		print(resultat)
		
	elif ordre == "norme":
		resultat = sqrt(sum(liste_carres(liste)))
		print(resultat)
		
	elif ordre == "alt":
		resultat = sum(un_sur_deux(liste)) - sum(deux_sur_un(liste))
		print(resultat)
	
	else:
		print("ERREUR")

principale()