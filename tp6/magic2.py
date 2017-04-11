from qtido import *
import sys

def losange(f,x,y,h,l):
	ligne(f,x-l,y,x,y+h)
	ligne(f,x+l,y,x,y+h)
	ligne(f,x-l,y,x,y-h)
	ligne(f,x+l,y,x,y-h)

def principale():
	f = creer(800,600)
	
	for i in range(int(sys.argv[1])):
		if i%2==0:
			losange(f,400,300,(i+1)*25,(i+1)*25+30)
		else:
			cercle(f,400,300,i*25)
	
	exporter_image(f, sys.argv[2])
	attendre_fermeture(f)

principale()