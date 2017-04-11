from qtido import *

def principale():
	
	f=creer(800,600)

	for i in range(int(sys.argv[1]),0,-1):
		if i%2==0:
			couleur(f,1,0,0)
		else:
			couleur(f,0,1,0)
		disque(f,400,300,i*25)

	exporter_image(f,sys.argv[2])
	attendre_fermeture(f)

principale()