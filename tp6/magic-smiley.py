from qtido import *

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
	c=0
	cou=[1,0,0]
	
	for j in range(1,int(sys.argv[1])+1):
		for i in range(1,int(sys.argv[2])+1):
			if c:
				cou=[1,0,0]
				taille=20
			else:
				cou=[0,0.42,0.76]
				taille=30
			
			smiley(f,cou,i*60,j*60,taille)
			c=not(c)
		c=not(c)
		
	exporter_image(f,sys.argv[3])
	attendre_fermeture(f)

  
principale()