# 1) imports
from math import *




# 2) définitions de fonctions

def carre(nombre):
	return(nombre ** 2)

def cube(nombre):
	return(nombre ** 3)

def logbase(nombre,base):
	return(log10(nombre) / log10(base))

def aire_disque(rayon):
	return(pi*rayon**2)

def volume_cylindre(rayon, hauteur):
	return(aire_disque(rayon)*hauteur)

### NE PAS MODIFIER CETTE FONCTION ###
def verifie_presque_egal(a, b):
    if round(a, 5) != round(b, 5):
        raise ValueError("ERREUR : «"+str(a)+"» != «"+str(b)+"»")
######################################


    
# 3 et 4) programme principal

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions

verifie_presque_egal( carre(8), 64)
verifie_presque_egal( carre(-10), 100)
verifie_presque_egal( cube(10), 1000)
verifie_presque_egal( cube(-0.1), -0.001)
verifie_presque_egal( logbase(1024, 2), 10)
verifie_presque_egal( logbase(1024, 1024), 1)
verifie_presque_egal( aire_disque(2.5), 19.634954084936208)
verifie_presque_egal( volume_cylindre(2.5, 100), 1963.4954084936208)

### Ajouter vos propres tests ci-dessous

print(cube(logbase(volume_cylindre(10,2),aire_disque(42.42))))
