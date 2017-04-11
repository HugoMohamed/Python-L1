from qtido import *
from random import uniform

def losange(f,cx,cy,rh,rv):
	ligne(f,cx+rh,cy,cx,cy+rv)
	ligne(f,cx+rh,cy,cx,cy-rv)
	ligne(f,cx-rh,cy,cx,cy+rv)
	ligne(f,cx-rh,cy,cx,cy-rv)

def smiley(f,cou,cx,cy,r):
	couleur(f,cou[0],cou[1],cou[2])
	disque(f,cx,cy,r)
	couleur(f,0,0,0)
	losange(f,cx-3/12*r,cy-1/2*r,1/5*r,1/10*r)
	losange(f,cx+3/12*r,cy-1/2*r,1/5*r,1/10*r)
	disque(f,cx,cy,1/10*r)
	ligne(f,cx-1/2*r,cy+1/3*r,cx+1/2*r,cy+1/3*r)
	ligne(f,cx,cy+2/3*r,cx+1/2*r,cy+1/3*r)
	ligne(f,cx-1/2*r,cy+1/3*r,cx,cy+2/3*r)
	
def principale():
	f=creer(800,600)
	
	for i in range(100):
		smiley(f,[uniform(0,1),uniform(0,1),uniform(0,1)],uniform(50,750),uniform(50,550),uniform(25,75)) 
	
	exporter_image(f,"question-smiley.png")
	attendre_fermeture(f)

principale()