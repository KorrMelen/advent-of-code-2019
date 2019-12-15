def day2 (n,v) :
	file = open("inputDay2","r")
	intcode = file.read()
	file.close()
	intcode = intcode.split(",")
	intcode = map(lambda x : int(x),intcode)
	intcode[1] = n
	intcode[2] = v
	i = 0
	while intcode[i] != 99 :
		opcode = intcode[i]
		pos1 = intcode[i+1]
		pos2 = intcode[i+2]
		pos3 = intcode[i+3]
		if (opcode != 1 and opcode != 2) or pos1 > len(intcode) or pos2 > len(intcode) or pos3 > len(intcode) :
			return 0
		if opcode == 1 :
			intcode[pos3] = intcode[pos1] + intcode[pos2]
		else :
			intcode[pos3] = intcode[pos1] * intcode[pos2]
		i += 4
	return(intcode[0])

n = -1
v = -1
output = 0
while n < 99 and output != 19690720:
	n += 1
	v = -1
	while v < 99 and output != 19690720:
		v += 1
		output = day2(n,v)

print(n*100 + v)