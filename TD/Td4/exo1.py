from math import *

# Question 1 :

def principal():
	resultat = []
	lesCarrees = [10,1.414,9,10.10]

	for i in range(len(lesCarrees)):
		resultat.append(lesCarrees[i] **2)
	
principal()


#Question 2 :

def principal():
	resultat = []
	leslogs = [100,1.414,9,10.10]

	for i in range(len(leslogs)):
		resultat.append(log10(leslogs[i]))

principal()


#Question 3 :

def principal():
	resultat = []
	tousFloat = [100,1.414,9,10.10,999]

	for i in range(len(tousFloat)):
		resultat.append(float(tousFloat[i]))

principal()

