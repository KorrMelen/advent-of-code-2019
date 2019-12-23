import sys

file = open("inputDay3","r")
path1 = file.readline()
path2 = file.readline()
file.close()

croisement = sys.maxsize
minstep = sys.maxsize

coori1 = 0
coorj1 = 0
i = 0
nbstep1 = 0
while i < len(path1):
	dir1 = path1[i]
	i += 1
	long1 = ""
	while i < len(path1) and path1[i] != ",":
		long1 += path1[i]
		i += 1
	coori1bis = coori1
	coorj1bis = coorj1
	if dir1 == 'U':
		coori1bis = coori1 - int(long1)
	elif dir1 == 'D':
		coori1bis = coori1 + int(long1)
	elif dir1 == 'L':
		coorj1bis = coorj1 - int(long1)
	else :
		coorj1bis = coorj1 + int(long1)

	coori2 = 0
	coorj2 = 0
	j = 0
	nbstep2 = 0
	while j < len(path2):
		dir2 = path2[j]
		j += 1
		long2 = ""
		while j < len(path2) and path2[j] != ",":
			long2 += path2[j]
			j += 1
		coori2bis = coori2
		coorj2bis = coorj2
		if dir2 == 'U':
			coori2bis = coori2 - int(long2)
		elif dir2 == 'D':
			coori2bis = coori2 + int(long2)
		elif dir2 == 'L':
			coorj2bis = coorj2 - int(long2)
		else :
			coorj2bis = coorj2 + int(long2)
		
		if coori2 == coori2bis :
			if min(coorj2,coorj2bis) < coorj1 < max(coorj2,coorj2bis) and min(coori1,coori1bis) < coori2 < max(coori1,coori1bis):
				if (nbstep1 + nbstep2 + abs(coori2 - coori1) + abs(coorj1 - coorj2)) < minstep :
					minstep = nbstep1 + nbstep2 + abs(coori2 - coori1) + abs(coorj1 - coorj2)
				if abs(coori2) + abs(coorj1) < croisement:
					croisement = abs(coori2) + abs(coorj1)
		else:
			if min(coorj1,coorj1bis) < coorj2 < max(coorj1,coorj1bis) and min(coori2,coori2bis) < coori1 < max(coori2,coori2bis):
				if (nbstep1 + nbstep2 + abs(coori2 - coori1) + abs(coorj1 - coorj2)) < minstep :
					minstep = nbstep1 + nbstep2 + abs(coori2 - coori1) + abs(coorj1 - coorj2)
				if abs(coori1) + abs(coorj2) < croisement:
					croisement = abs(coori1) + abs(coorj2)

		j += 1
		nbstep2 += int(long2)
		coori2 = coori2bis
		coorj2 = coorj2bis
	i += 1
	nbstep1 += int(long1)
	coori1 = coori1bis
	coorj1 = coorj1bis

print (minstep)
print (croisement)