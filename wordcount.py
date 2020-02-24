import os

directory = input('Which directory would you like a word count for?')
wordcount = 0
uniquewords = set([])

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".md") or filename.endswith(".html"):
        with open(directory + '/' + filename, 'r') as file:
            text = file.read().replace('\n', '').split('---', 2)
            wordcount += len(text[2].split())
            for words in text[2].lower().split():
                uniquewords.add(words)
        continue
    else:
        print('That directory doesn\'t appear to have any posts in!')

print('Wordcount: ' + str(wordcount))
print('Unique words: ' + str(len(uniquewords)))
