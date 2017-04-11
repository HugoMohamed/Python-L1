from qtido import *
import sys


def magic1(f,nb):
	for i in range(nb+1):
		
		cercle(f,400,300,i*25)



def principale():
	f = creer(800,600)
	x = int(sys.argv[1])
	magic1(f,x)
	
	exporter_image(f,sys.argv[2])
	attendre_fermeture(f)
	
principale()