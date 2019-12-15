def totfuel (x):
	fuel = 0
	while x > 8:
		x = x // 3 - 2
		fuel += x
	return fuel

file = open("inputDay1","r")
mass = file.readlines()
file.close()
mass = map(lambda x : int(x),mass)
fueltot = sum(map(totfuel, mass))
print(fueltot)