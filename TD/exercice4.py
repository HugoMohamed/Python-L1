# Question 10 :

coeffNote = input("coeff note coeff note coeff note etc... \n").split()

for i in range(0,len(coeffNote),2) :
	print("une note de",float(coeffNote[i+1]),"avec un coeff de",float(coeffNote[i]))


# Question 11 :

note = input("NOTEEEEEEEEbiteEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe\n").split()
sommePoids = 0
sommePonderee = 0

for i in range(0,len(note),2):
	sommePonderee += float(note[i]) * float(liste[i+1])
	sommePoids += float(liste[i])

print("moyenne =",sommePonderee / sommePoids)


