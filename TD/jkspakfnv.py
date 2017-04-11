from qtido import *
from random import *

def carreR(x,y):
	a = random()
	b = random()
	c = random()
	couleur(f,a,b,c)
	rectangle(f,x,y,x+50,y+50)

def carreG(x,y):
	a = random()
	b = random()
	c = random()
	couleur(f,a,b,c)
	rectangle(f,x,y,x+50,y+50)

f = creer(400,400)
	
for i in range(0,401,50):
	for j in range(0,401,50):
		
		if (i%100 == 0 and j%100 == 0) or (i%100 != 0 and j%100 != 0):
			carreR(i,j)
		else:
			carreG(i,j)
		
attendre_fermeture(f)