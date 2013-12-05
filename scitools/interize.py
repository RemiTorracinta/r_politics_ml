f = open('fTrain.data', 'rb')
newF = open('train.data', 'w')
for line in f:
	lst = line.split()
	i = 0
	j = 1
	for word in lst:
		if not (i == 0 or i >= len(lst) - 2):
			newF.write(word + " ")
		elif (i == 0):
			newF.write(str(int(float(word))) + " ")
		i += 1
	newF.write("\n")

f.close()
newF.close()