import os
import re
import string
import regex
from bs4 import BeautifulSoup

# a datacleaning script so blog posts can be fed into an RNN

linkremover = regex.compile(
    r"(?|(?<txt>(?<url>(?:ht|f)tps?://\S+(?<=\PP)))|\(([^)]+)\)\[(\g<url>)])", re.MULTILINE)

md_link = regex.compile(r"\[([^\]]+)\]\(([^)]+)\)")

dirs = ["mendokusai/_posts", "tartarus/_posts"]

for directory in dirs:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md") or filename.endswith(".html"):
            with open(directory + '/' + filename, 'r') as file:

                # removes line endings
                # text = file.read().replace('\n', ' ')
                text = file.read()

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
                # text = regex.sub(linkremover, '', text)
                text = regex.sub(md_link, '\g<1>', text)

                # todo: replace code blocks, hashes, HRs

                text = regex.sub(r"```(.*)```", '', text)
                text = regex.sub(r"#{2,}", '', text)
                text = text.replace("___", '').replace("---", '')

                textfile = open('data.txt', 'a')
                textfile.write(text)
                textfile.close()
            continue
