f = open('fVal.data', 'rb')
newF = open('Val.data', 'w')
words = open('words.txt', 'rb')
count = -1
minval = 0
for line in f:
	val = int(float(line.split()[0]))
	if val < minval:
		minval = val
f.seek(0)
for line in words:
	count += 1
for line in f:
	lst = line.split()
	i = 0
	j = 1
	for word in lst:
		if not (i == 0 or i >= len(lst) - 2):
			feat = word.split(':')
			key = int(feat[0])
			while j <= count:
				if j == key:
					newF.write(word + " ")
					j += 1
					break
				newF.write(str(j) + ':0.0 ')
				j += 1
		elif (i == 0):
			newF.write(str(int(float(word))-minval+1) + " ")
		i += 1
	while j <= count:
		newF.write(str(j) + ':0.0 ')
		j += 1
	newF.write("\n")

f.close()
newF.close()