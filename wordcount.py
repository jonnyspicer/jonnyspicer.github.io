import os
import re
import csv
import nltk
import string
import regex
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob

# TODO:
# - strip anything in head/header/footer for old html posts
# - correct the oodles of spelling mistakes this has uncovered

# directory = input('Which directory would you like a word count for?')
wordcount = 0
uniquewords = dict()
wordsperpost = dict()
stems = dict()
nonalphabeticalremover = regex.compile('[^A-Za-z ]')
sentiments = dict()

# huge shoutout to https://stackoverflow.com/questions/25109307/how-can-i-find-all-markdown-links-using-regular-expressions
linkremover = regex.compile(
    r"(?|(?<txt>(?<url>(?:ht|f)tps?://\S+(?<=\PP)))|\(([^)]+)\)\[(\g<url>)])", re.MULTILINE)

dirs = ["mendokusai/_posts", "tartarus/_posts"]

for directory in dirs:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md") or filename.endswith(".html"):
            with open(directory + '/' + filename, 'r') as file:

                # removes line endings
                text = file.read().replace('\n', ' ')

                # selects only the portion of the file after the Jekyll front matter
                text = text.split('---', 2)

                # replace break and list tags with spaces
                text = text[2].replace('<br />', ' ')
                text = text.replace('<li>', ' ')

                text = BeautifulSoup(text, features="html.parser")

                # removes html tags
                text = text.get_text()

                # removes target=blank Markdown tags
                text = text.replace("{:target=\"_blank\"}", '')

                # removes Markdown links
                text = regex.sub(linkremover, '', text)

                # removes anything that isn't an alphabetical character and casts the remaining string to lowercase
                text = regex.sub(nonalphabeticalremover, ' ', text).lower()

                blob = TextBlob(text)

                sentiments.update({ filename: blob.sentiment.polarity})
                wordsperpost.update({ filename: len(text.split())})

                wordcount += len(text.split())

                # nltk stemming/token magic from http://ryancompton.net/2014/06/06/statistical-features-of-infinite-jest/
                tokens = nltk.word_tokenize(text)
                stemmer = nltk.stem.PorterStemmer()
                stemmed_tokens = map(lambda x: stemmer.stem(x), tokens)

                for token in stemmed_tokens:
                    if token in stems:
                        newVal = stems.get(token) + 1
                        stems.update({token: newVal})
                    else:
                        stems.update({token: 1})

                for word in text.split():
                    if word in uniquewords:
                        newVal = uniquewords.get(word) + 1
                        uniquewords.update({word: newVal})
                    else:
                        uniquewords.update({word: 1})
            continue

if wordcount < 1:
    print('That directory doesn\'t appear to have any posts in!')
else:
    print('Wordcount: ' + str(wordcount))
    print('Unique words: ' + str(len(uniquewords)))
    print('Unique stems: ' + str(len(stems)))

# sorting dictionaries is unnecessarily difficult in python
sortedtuples = sorted(uniquewords.items(), reverse=True, key=lambda x: x[1])
sortedwords = dict()

for tuple in sortedtuples:
    sortedwords.update({tuple[0]: tuple[1]})

pd.DataFrame.from_dict(data=sortedwords, orient='index').to_csv(
    'words.csv', header=False)

pd.DataFrame.from_dict(data=stems, orient='index').to_csv(
    'stems.csv', header=False)

pd.DataFrame.from_dict(data=sentiments, orient='index').to_csv(
    'sentiments.csv', header=False)

pd.DataFrame.from_dict(data=wordsperpost, orient='index').to_csv(
    'wordsperpost.csv', header=False)
