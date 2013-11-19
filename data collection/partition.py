import random

n_val = 100
n_test = 100
fTrain = open('fTrain.data', 'wb')
fVal = open('fVal.data', 'wb')
fTest = open('fTest.data', 'wb')
f = open('posts.data', 'rb')

count = 0
for line in f:
	count += 1
print(count)
sample = random.sample(range(count - 1), n_val+n_test)
valis = set(sample[:(n_val)])
tests = set(sample[n_val:])

f.seek(0)
print(len(valis))
print(len(tests))
print(valis)
print(tests)
i = -1
for line in f:
	i += 1
	if (i in tests):
		fTest.write(line)
		continue
	if (i in valis):
		fVal.write(line)
		continue
	if (i == count - 1):
		print(i)
		break
	fTrain.write(line)

	
fTrain.close()
fVal.close()
fTest.close()