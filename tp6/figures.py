from qtido import *
from random import *


def losange(f,x,y,h,l):
	ligne(f,x-l,y,x,y+h)
	ligne(f,x+l,y,x,y+h)
	ligne(f,x-l,y,x,y-h)
	ligne(f,x+l,y,x,y-h)


def principale():
	f = creer(800, 600);
	
	cercle(f, 100, 300, 50)
	couleur(f, 1, 1, 0)
	disque(f, 200, 200, 50)
	couleur(f, 0, 1, 0)
	ligne(f, 400, 200, 450, 250)
	cadre(f, 500, 200, 550, 250)
	rectangle(f, 450, 250, 500, 300)
	
	couleur(f,random(),random(),random())
	losange(f,400,300,50,20)
	
	couleur(f,random(),random(),random())
	losange(f,500,200,10,200)
	
	couleur(f,random(),random(),random())
	losange(f,300,400,100,20)
	
	couleur(f,random(),random(),random())
	losange(f,400,300,250,50)
	
	couleur(f,random(),random(),random())
	losange(f,400,300,200,50)
	
	couleur(f,random(),random(),random())
	losange(f,400,300,150,50)
	
	couleur(f,random(),random(),random())
	losange(f,400,300,100,50)
	
	exporter_image(f, "question-losange.png")
	
	attendre_fermeture(f)



principale()

