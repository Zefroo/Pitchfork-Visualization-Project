# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:47:25 2020

@author: Paul
"""
import csv
from collections import Counter
from textblob import TextBlob

review_dict = {}
with open('pitchfork_best.csv', encoding='utf8') as pitch_file:
    csv_reader = csv.reader(pitch_file,delimiter=',')
    next(csv_reader) # skip header
    for row in csv_reader:
        text = TextBlob(row[8])
        # don't care about cleaning - just gettin adjectives
        all_tags = text.tags
        adjs = [tag[0] for tag in all_tags if tag[1] == 'JJ' ]
        counter = Counter(adjs)
        review_dict[row[0]] = dict(counter)

pitch_file.close()
#-------------------------------------------
#create a new file with the reviewID, adjective, count of adjective, and sentiment
with open('pitchfork_adjs.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["reviewID","adjective","count","sentiment"])
    for id,words in review_dict.items():
        for word,count in words.items():
            if word.isalpha() and len(word) > 2:
                word_blob = TextBlob(word)
                writer.writerow([id, word, count, word_blob.sentiment.polarity])
            else:
                pass
file.close()