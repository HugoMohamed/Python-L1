from qtido import *

def principale():
	f=creer(800,600)
	couleur(f,1,1,1)

	for i in range(1,int(sys.argv[1])+1):
		for j in range(1,int(sys.argv[2])+1):
			rectangle(f,j*30,i*30,j*30+25,i*30+25)

	exporter_image(f,sys.argv[3])
	attendre_fermeture(f)
  
principale()
