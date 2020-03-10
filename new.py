import datetime
import re
import os
import sys
import subprocess

date = datetime.date.today().strftime('%Y-%m-%d')

blog_set = False
while blog_set != True:
    flavour = input('Which blog are you writing in today?')
    flavour = flavour.lower()
    if flavour in 'mendokusai':
        flavour = 'mendokusai'
        blog_set = True
    elif flavour in 'tartarus':
        flavour = 'tartarus'
        blog_set = True

name = input('What\'s the title of your blog post?')
tags = input('What topics are you writing about today (separated by a comma)?')

title_name = re.sub('[^a-zA-Z\s\d]', '', name)
title_name = re.sub('\s', '-', title_name).lower()

title = date + '-' + title_name + '.md'

if flavour == 'mendokusai':
    path = os.getcwd() + '/mendokusai/_posts/' + title
    if not os.path.exists(path):
        open(path, 'w')
elif flavour == 'tartarus':
    path = os.getcwd() + '/tartarus/_posts/' + title
    if not os.path.exists(path):
        open(path, 'w')

if os.path.exists(path):
    f = open(path, 'a')
    f.write('---\n')
    f.write('layout: ' + flavour + '\n')
    f.write('author: Jonny Spicer\n')
    f.write('title: ' + name + '\n')
    f.write('tags: [ ' + tags + ' ]\n')
    f.write('---\n')

    subprocess.call(('nano'), path)

    # if sys.platform == "win32":
    #     os.startfile(path, 'open')
    # elif sys.platform == "darwin":
    #     subprocess.call(('open', path))
    # else:
    #     subprocess.call(('xdg-open', path), shell=True)
