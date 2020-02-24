import os
import csv
import string
from bs4 import BeautifulSoup

# TODO:
# - strip markdown syntax (links etc)
# - strip URLs
# - correct the oodles of spelling mistakes this has uncovered

directory = input('Which directory would you like a word count for?')
wordcount = 0
uniquewords = set([])
punctuationRemover = str.maketrans('', '', string.punctuation)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".md") or filename.endswith(".html"):
        with open(directory + '/' + filename, 'r') as file:
            # This is a bit of a mouthful... it takes the raw text, uses BS4 to strip out
            # html tags, replaces line endings to it's on a single line, then selects
            # everything after the Jekyll front matter
            text = BeautifulSoup(file.read().replace(
                '\n', ''), features="html.parser").get_text().split('---', 2)
            wordcount += len(text[2].split())
            # strips punctuation then splits by space
            for words in text[2].lower().translate(punctuationRemover).split():
                uniquewords.add(words)
        continue
    else:
        print('That directory doesn\'t appear to have any posts in!')


print('Wordcount: ' + str(wordcount))
print('Unique words: ' + str(len(uniquewords)))

uniquewords = sorted(list(uniquewords))
with open('words.csv', 'w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for word in uniquewords:
        wr.writerow([word, ])
