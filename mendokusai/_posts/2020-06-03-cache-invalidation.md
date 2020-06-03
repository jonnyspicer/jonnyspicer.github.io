---
layout: mendokusai
author: Jonny Spicer
title: Cache Invalidation
tags: [ Software Development ]
---
If you didn't already know, there is a famous quote in the software world attributed to Phil Karlton that goes like this;

> There are only two hard things in Computer Science; cache invalidation and naming things.

Whether or not there are other, unmentioned difficulties in the field, cache invalidation is an absolute nightmare. Everytime I rebuild the solution for the application I am working in my day job, it rebuilds the entire cache, which takes 15-20 minutes. Before I can
see whether any of my changes have taken effect. Yuck.
