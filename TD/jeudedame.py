from qtido import *
from random import *

def pions(f,bleu,rouge):
    d1 = random()
    d2 = random()
    d3 = random()
    d21 = random()
    d22 = random()
    d23 = random()
    
    for i in range(10):
        for j in range(10):
            if [i,j] in bleu:
                couleur(f,d1,d2,d3)
                disque(f,i*50+25,j*50+25,20)
            elif [i,j] in rouge:
                couleur(f,d21,d22,d23)
                disque(f,i*50+25,j*50+25,20)
    

def damier_vide(f):
    H = 50
    c1 = random()
    c2 = random()
    c3 = random()
    c21 = random()
    c22 = random()
    c23 = random()
    
    for i in range(10):
        for j in range(10):
            if(i+j)%2 == 0:
                couleur(f,c1,c2,c2)
            else:
                couleur(f,c21,c22,c23)
            rectangle(f,i*H,j*H,i*H+H,j*H+H)
    
def principale():
    f = creer(500,500)
    bleu = [[0,0],[2,0],[4,0],[6,0],[8,0],[1,1],[3,1],[5,1],[7,1],[9,1]]
    rouge = [[1,9],[3,9],[5,9],[7,9],[9,9],[0,8],[2,8],[4,8],[6,8],[8,8]]
    
    damier_vide(f)
    pions(f,bleu,rouge)
    
    while not est_fermee(f):
        attendre_evenement(f,100)
        e = dernier_evenement(f)
        
        if est_souris(f,e,"PRESS"):
            xy = coordonnees_souris(f,e)
            i = xy[0]//50
            j = xy[0]//50
            ij =[i,j]
            if ij in bleu :
                bleu.remove(ij)
            elif ij in rouge :
                rouge.remove(ij)
        pions(f,bleu,rouge)
        #attendre_fermeture(f)
principale()