from qtido import *
import sys


def spirale(t,x):
	tortue_trace(t)
	for i in range(1,x+1):
		tortue_avance(t,i*6+50)
		tortue_gauche(t,90)


def principale():
	f = creer(800,600)
	t = creer_tortue(f)
	x = int(sys.argv[1])
	spirale(t,x)
	
	exporter_image(f,sys.argv[2])
	attendre_fermeture(f)
	
principale()