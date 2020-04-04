---
layout: mendokusai
author: Jonny Spicer
title: Build All The Things IV
tags: [ Software Development ]
---
I'm super lazy about checking whether or not these posts actually get published successfully, I essentially run `git push` and then go do something else with my life. Despite doing this every day, it turns out that I am incapable of doing it correctly consistently, and frequently receive messages from concerned readers that I have not published a post for that day or the previous.

To try and rectify this, as well as learn some Python/get into the habit of automating things, I've written a script that should hopefully handle publishing as well as testing any new posts -
you can view it [here.](https://github.com/jonnyspicer/jonnyspicer.github.io/blob/master/publish.py) This post was in fact published using the script - I didn't have to enter a single git command, it's all handled in one block of Python code.

Said code is admittedly very, very bad - I should use unittest or py.test rather than a DIY one, but I couldn't get the latter working and it seemed relatively trivial to do myself. I also shouldn't repeat myself so much and I think my method of handling the git commands is exceptionally ugly, but I still know barely any of this language so please be gentle with me!
