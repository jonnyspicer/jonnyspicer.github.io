---
layout: mendokusai
author: Jonny Spicer
title: Chess Programming II&#58; The Competition
tags: [ Chess, Software Development ]
---
The bad news for any of my regular readers who are interested in neither chess nor programming is that
I am probably going to be writing about it quite a bit in the next week or two. The good news for any
of my regular readers who interested in both chess *and* programming is... that I am probably going to
be writing about it quite a bit in the next week or two.

Having looked at some implementations of chess engines in C# on Github, I am very confident I can
write one that's better than everything I found in my admittedly non-extensive search. People have
implemented the game of chess in just [288 bytes](https://leanchess.github.io/){:target="_blank"}
(well, sort of - Leanchess only knows most of the rules of the game, not all of them) and most
of the alternatives on Github takes thousands, if not tens of thousands, of *lines* to simply
generate something that can understand the rules, let alone evaluate moves or generate search trees.

Obviously, this is because C# is a terrible language to write a chess engine in. Anybody seriously
undertaking to make a solid engine would write it in C or C++, however sadly I don't know either
of those languages, and I rather like the shortcuts that C# makes available to programmers, even if
those come at a massive cost in terms of efficiency and performance.

Writing a chess engine is probably about as close to the silicon as you can realistically get in C#.
I'm going to be using bitboards, representations of aspects of a chess game in a mere 64 bits (pretty 
convenient that everyone uses 64 bit processor architecture these days eh?) that can then have various
bitwise operations performed on them in order to produce a full representation of a game of chess.
While at the moment I only have aspirations for the engine to be able to generate a complete list of
legal moves in each position (rather than perform any kind of search or evaluation), I am confident
that if I can implement this minimalist approach to game state representation well, then it would
lay the foundation to be potentially the best available open source C# chess engine.
