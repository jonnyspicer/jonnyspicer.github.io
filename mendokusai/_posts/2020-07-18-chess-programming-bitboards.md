---
layout: mendokusai
author: Jonny Spicer
title: Chess Programming&#58; Bitboards
tags: [ Chess, Software Development ]
---
Today the engine work began in earnest, and I've already made some decent progress. It can already hold a representation of a chessboard in memory, and tell you the position of
the pieces on it - it can "see" the board if you will. It still has no idea about any of the rules of the game but, you know, baby steps.

It works using [bitboards,](https://www.chessprogramming.org/Bitboards){:target="_blank"} as mentioned in previous entries. Each of these bitboards are 64-bit binary integers, and
there are 12 that define the board state - one for each type of piece, for either colour. Each of these can then be iterated over to build up a representation of the board, and for
now they are being cast into a multidimensional array to be written to my console for debugging.

So, how do you tell if there is, for example, a white rook on a certain square, just by looking at a 64 bit integer? Take the white rook bitboard for the starting position:

```csharp
0000000000000000000000000000000000000000000000000000000010000001
```

Well, it turns out you can do some neat stuff with bitwise operators (which seems to be a big theme in writing performant chess engines from what I can tell). If we think of each
digit in the bitboard as a square on a chessboard, obviously each time the digit is a '1', that means a white rook is on that square. In order to check every square, we can write a
for loop that right-shifts each square one at a time, and then checks to see if a one is present by using the logical and operator ```&``` to see if the relevant digit is a '1', like
so:

```csharp
for (int i = 0; i < 64; i++)
    {
        if (((wRook >> i) & 1) == 1)
        {
            Console.WriteLine("There's a white rook here!");
        } else
        {
            Console.WriteLine("No white rook to be found...)
        }
    }
```

The challenge for tomorrow is to teach it how the pieces move - which is going to involve a whole lot more bitboards and bitwise operations. Wish me luck!
