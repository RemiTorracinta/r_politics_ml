import praw
import csv
import calendar
import datetime
import re

#List of words in previous submissions
words_file = open('words.txt', 'rb')
#UTC of most recently polled post
last_file = open('last.txt', 'rb')
#dictionary of words mapping word -> feature index (for svm-light)
words = {}
last = 0

last = int(last_file.read().rstrip())

numWords = 0
for line in words_file:
    words[line.rstrip()] = numWords
    numWords += 1


last_file.close()
words_file.close()
words_file = open('words.txt', 'a')
last_file = open('last.txt', 'w')
#Output of results for SVM-light
results_file = open('posts.data', 'a')

user = ("Cornell ML Class politics submission analyzer"
		"by /r/jazzkingrt v0.1"
		"github.com/RemiTorracinta/r_politics_ml")
r = praw.Reddit(user_agent=user)
subreddit = r.get_subreddit('politics')
h3_ago = datetime.datetime.now() - datetime.timedelta(hours = 5)
h3_utc = calendar.timegm(h3_ago.utctimetuple())
last_file.write(str(h3_utc))
#go through submissions, append to svm-light file
for submission in subreddit.get_new(limit=None):
	created = submission.created_utc
	if created < last or created > h3_utc : continue
	target = str(float(submission.ups - submission.downs))
	content = submission.title + " " + submission.domain
	#list of words in title, + submission domain
	wordList = re.sub('[^\w]', " ",  content).split()
	wordCounts = {}
	for word in wordList:
		if word not in words:
			words[word] = numWords
			wordCounts[word] = 1
			numWords += 1
			words_file.write(word+"\n")
		else:
			if word in wordCounts:
				wordCounts[word] += 1
			else:
				wordCounts[word] = 1
	features = ""
	for word, count in wordCounts.iteritems():
		features += str(words[word]) + ":" + str(float(count)) + " "
	results_file.write(target +  " " + features + "# " + submission.id + "\n")
	
words_file.close()
last_file.close()
results_file.close()