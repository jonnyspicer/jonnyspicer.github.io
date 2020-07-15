---
layout: mendokusai
author: Jonny Spicer
title: Chess Programming
tags: [ Chess, Software Development ]
---
I've recently starting trying to put together my own chess engine. Obviously on some level I knew
how complex a task this was beforehand, but I still didn't anticipate quite how many difficult
problems would need to be considered. There is;

- Board representation, either piece centric or square centric. I am most likely going to use the latter, but then there are considerations of which model to use, with a choice of 8x8 Board, 10x12 Board, Vector Attacks, and 0x88.

- Actually implementing the rules, which sounds easier than it is. 50-move and threefold repetition
draws require some persistent knowledge of previous positions in the game.

- Move generation, which can be legal, pseudo-legal, chunked or staged.

- Evaluation... insert my whole knowledge of the game here. And I have to work out how to teach that
to some silicon.

- Search, which can be depth-first, alpha-beta or best-first (including the very fashionable Monte-Carlo tree search). All of these have a bunch of different sub categories, and most of them
have ludicrous memory requirements.

- Connection to GUI, either through implementation of the Universal Chess Interface or the Chess Engine
Communication Protocol. Then I also have to pick a suitable GUI, or write my own.

- Tablebases and opening books - to at least make it a real engine.

- Performance considerations, because C# wouldn't be anybody's first choice of language to write a
highly-performant chess engine in. The language is... slow... so some kind of optimisation is a must,
and that is doubly true given it will be running on my local machine and I'm not going to give it
half a terabyte of memory to play with.

It's going to be difficult, but these are all super, super fun problems to solve. For me, anyway.
