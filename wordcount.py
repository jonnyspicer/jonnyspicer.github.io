import os
import re
import csv
import nltk
import string
import regex
import pandas as pd
from bs4 import BeautifulSoup

# TODO:
# - correct the oodles of spelling mistakes this has uncovered

directory = input('Which directory would you like a word count for?')
wordcount = 0
uniquewords = dict()
punctuationRemover = str.maketrans('', '', string.punctuation)

# huge shoutout to https://stackoverflow.com/questions/25109307/how-can-i-find-all-markdown-links-using-regular-expressions
linkRemover = regex.compile(r"(?|(?<txt>(?<url>(?:ht|f)tps?://\S+(?<=\PP)))|\(([^)]+)\)\[(\g<url>)])")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".md") or filename.endswith(".html"):
        with open(directory + '/' + filename, 'r') as file:
            # removes line endings
            text = file.read().replace('\n', '')

            # selects only the portion of the file after the Jekyll front matter
            text = text.split('---', 2)

            # removes html tags
            text = BeautifulSoup(text[2], features="html.parser").get_text()

            # removes target=blank Markdown tags
            text = text.replace("{:target=\"_blank\"}", '')

            # removes Markdown links
            text = regex.sub(linkRemover, '', text)

            # removes anything that isn't an alphabetical character
            rec = re.compile('[^A-Za-z ]')

            # casts the remaining string to lowercase
            text = re.sub(rec, ' ', text).lower()

            wordcount += len(text.split())

            tokens = nltk.word_tokenize(text)
            stemmer = nltk.stem.PorterStemmer()
            stemmed_tokens = map(lambda x: stemmer.stem(x), tokens)

            for token in stemmed_tokens:
                if token in uniquewords:
                    newVal = uniquewords.get(token) + 1
                    uniquewords.update({token: newVal})
                else:
                    uniquewords.update({token: 1})
        continue
    else:
        print('That directory doesn\'t appear to have any posts in!')


print('Wordcount: ' + str(wordcount))
print('Unique words: ' + str(len(uniquewords)))

# sorting dictionaries is unnecessarily difficult in python

sortedtuples = sorted(uniquewords.items(), reverse=True, key=lambda x: x[1])
sortedwords=dict()

for tuple in sortedtuples:
    sortedwords.update({tuple[0] : tuple[1]})

pd.DataFrame.from_dict(data=sortedwords, orient='index').to_csv(
    'words.csv', header=False)
