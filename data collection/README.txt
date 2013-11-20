Do not (manually) edit or delete words.csv, last.csv, or posts.data!!!!!

Run poll.py to add the most recent 1000 posts /r/politics >3 hours old to posts.data.
Install praw , a reddit api wrapper for python, before doing so. Written for python 2.7.
Run partition.py to partition posts.data into a train, validation, and test sets. (Adjustable sizes are vars at start of script.)

sorting was used to fix up previously incorrect files, no need for these scripts anymore.

words.csv and last.csv keep records of previous polling so that submissions are not repeated and features (words) are numbered appropriately.

posts.data is formatted for svm-light, as is fVal, fTrain, and fTest.