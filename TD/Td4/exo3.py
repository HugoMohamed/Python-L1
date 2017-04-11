#Question 4 :
def liste_carres(liste_carres):
	resultat = []
	
	for i in range(len(liste_carres)):
		resultat.append(float(liste_carres[i]) ** 2)
	
	return resultat


#Question 5
def liste_floats(liste_floats):
	resultat = []
	
	for i in range(len(liste_floats)):
		resultat.append(float(liste_floats[i]))
	
	return resultat


#Question 6
def principale():
	liste_carres = input("Entrez une liste de nombre :\n").split()
	liste_carres(liste_carres)
	
	liste_floats = input("Entrez une liste de nombre : \n").split()
	liste_floats(liste_floats)


#Question 7
def input_floats():
	liste = input("Entrez un ordre suivi d'une liste de nombre : \n").split()

	return liste
	

#Question 8
def tousSaufUn(liste):
	resultat = []
	
	for i in range(1,len(liste),1):
		resultat.append(liste[i])

	return resultat


#Question 9
def un_sur_deux(liste):
	resultat = []
	
	for i in range(0,len(liste),2):
		resultat.append(liste[i])
		
	return resultat 


def deux_sur_un(liste):
	resultat = []
	
	for i in range(1,len(liste),2):
		resultat.append(liste[i])
		
	return resultat