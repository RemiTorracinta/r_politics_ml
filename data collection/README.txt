Do not edit or delete words.csv or last.csv!!!!!

Run poll.py to add the most recent 1000 posts /r/politics >3 hours old to posts.data.
Install praw , a reddit api wrapper for python, before doing so. Written for python 2.7.

words.csv and last.csv keep records of previous polling so that submissions are not repeated and features (words) are numbered appropriately.

posts.data is formatted for svm-light.

get_uniques.py and random_unique_ids.txt are old files for an abandonded endeavor.