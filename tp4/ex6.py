def produit(a,b):
	print("Appel de la fonction produit...")
	return(a*b)

def somme(a,b):
	print("Appel de la fonction somme...")
	return(a+b)

def calculer(string):
	string = string.split()
	if string[0] == "produit":
		print("Multiplication")
		print(produit(float(string[1]), float(string[2]))) #convertir en float pour eviter les problemes
	elif string[0] == "somme":
		print("Addition")
		print(somme(float(string[1]), float(string[2])))
	else:
		print("Erreur : syntaxe invalide.")

commande = input("Entrez un commande :\n")
calculer(commande)
