import os
from bs4 import BeautifulSoup

directory = input('Which directory would you like a word count for?')
wordcount = 0
uniquewords = set([])

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
            for words in text[2].lower().split():
                uniquewords.add(words)
        continue
    else:
        print('That directory doesn\'t appear to have any posts in!')

print('Wordcount: ' + str(wordcount))
print('Unique words: ' + str(len(uniquewords)))
