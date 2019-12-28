import sys

posibilite = 0
nombre = [1,9,7,4,8,7]
nombreDebut = [1,9,7,4,8,7]
nombreFin = [6,7,3,2,5,1]

def testNombre ():
	pred = 0
	nb = 1
	passe = False
	for i in range(0, len(nombre)):
		if nombre[i] == pred:
			if nb < 2:
				passe = True
				nb += 1
			else:
				passe = False
		else:
			if passe:
				return True
			pred = nombre[i]
			nb = 1
	return passe

def recursive (digit, posibilite):
	for i in range(nombre[digit-1],10):
		nombre[digit] = i
		if nombre >= nombreDebut:
			if nombre > nombreFin:
				print posibilite
				sys.exit()
			if digit != 5:
				posibilite = recursive(digit+1, posibilite)
			else:
				if testNombre():
					posibilite += 1
	return posibilite

for i in range(nombre[0],10):
	nombre[0] = i
	posibilite = recursive(1,posibilite)
