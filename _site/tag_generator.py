'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
Credit: qian256
Repo: https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py
'''

import glob
import os

post_dirs = ['mendokusai/_posts/', 'tartarus/_posts/']
tag_dir = 'tag/'

filenames = list()

for post_dir in post_dirs:
    filenames.extend(glob.glob(post_dir + '*md'))
    filenames.extend(glob.glob(post_dir + '*html'))

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            if line.startswith('tags:'):
                stripped_tags = line.strip('tags:').strip().replace('[', '').replace(']', '').split(',')
                for tag in stripped_tags:
                    total_tags.append(tag.strip())
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()

total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

total_tags = list(filter(None, total_tags))

for tag in total_tags:
    tag_filename = tag_dir + tag.replace(' ', '_').lower() + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\npermalink: /tag/' + tag.replace(' ', '_').lower() + '/\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
