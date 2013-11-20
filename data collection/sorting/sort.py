import re

words_file = open('posts.data', 'rb')
sorted_file = open('sorted.data', 'w')


def featsToString(feats):
	features = ""
	for word,count in [(k, feats[k]) for k in sorted(feats, key=int)]:
		features += str(word) + ":" + count + " "
	return features

for line in words_file:
    parts = line.split()
    newStr = ""
    i = 0
    n = len(parts)
    feats = {}
    newStr = ""
    for part in parts:
    	i += 1
    	if i == 1:
    		newStr += part + " "
    		continue
    	if i == n - 1:
    		newStr += featsToString(feats) + "# "
    		continue
    	if i == n:
    		newStr += part + "\n"
    		continue
    	feat = part.split(":")
    	feats[feat[0]] = feat[1]
    sorted_file.write(newStr)
words_file.close()
sorted_file.close()