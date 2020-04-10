---
layout: mendokusai
author: Jonny Spicer
title: 30 Days of Leetcode&#58; Days 6 to 10
tags: [ Software Development ]
---
Another five days of [Leetcoding](https://leetcode.com/discuss/general-discussion/551411/30-Day-LeetCoding-Challenge){:target="_blank"} are in the books, by and large without too much difficulty. The only
problem I spent longer than 30 minutes on was the first one in today's write-up, "Group Anagrams"
from April 6th, and the rest I found fairly straightforward, so much so that I would say some of
them (most notably today's problem, "Min Stack") are potentially a little too easy.

The experience of completing the challenge in C# is also not especially endearing me to the
language, now I can see quite how slow it is in comparison to others (even with comparatively
well-optimised code), with all my solutions taking over 200ms to execute. Combined with the
bloat that comes with both Windows and Visual Studio, I can't help but feel the language is
sluggish, and that feeling is certainly making me consider investing more of my time
into Python instead, although naturally that has its issues as well. Anyway, onto the problems:

### April 6th - [Group Anagrams](https://leetcode.com/problems/group-anagrams/){:target="_blank"}

In my opinion the most interesting of this set of five problems, and certainly the one that
took me the most time, this challenge has a fairly simple problem statement; "given an array
of strings, group anagrams together." Here's the example that's given:

```none
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

A couple of things in this problem took me a long time to figure out; namely the concept of using a Dictionary to map the value before constructing the final list after having completed iteration over the initial
array, and secondly (and more embarrassingly) to realise that I needed to use the string() constructor on each char array rather than just trying to compare the latter directly.

```csharp
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        IList<IList<string>> anagrams =
        new List<IList<string>>();

        // initialise a temporary dictionary to use as a map
        Dictionary<string, List<string>> temp =
         new Dictionary<string, List<string>>();

        // for every string in the original array
        for(int i = 0; i < strs.Length; i++){
            // rearrange the string in the original array
            //into alphabetically ordered characters
            char[] initialCharArray = strs[i].ToCharArray();
            Array.Sort(initialCharArray);
            string orderedString = new string(initialCharArray);

            if(temp.ContainsKey(orderedString)){
                // if the map contains the ordered string,
                //add this iteration of the anagram
                temp[orderedString].Add(strs[i]);
            } else {
                // if not, add the new ordered string,
                //along with its first anagram
                temp.Add(orderedString,
                new List<string>{strs[i]});
            }
        }

        // transfer the map to the results List
        foreach(var list in temp){
            anagrams.Add(list.Value);
        }

        return anagrams;
    }
}
```

### April 7th - [Counting Elements](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/){:target="_blank"}

Today's challenge was quite straightforward, although a version of me from the not-so-distant past wouldn't have been familiar enough with HashSets to reach for one straightaway when tackling
this kind of problem. The task is as follows: "Given an integer array ```arr```, count element ```x``` such that ```x + 1``` is also in ```arr```. If there are duplicates in ```arr```, count them
separately." This was also the first problem of the challenge so far to be completely new to Leetcode, with more to come - hopefully the rest are a little harder than this one!

Example:

```none
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
```

Not too much to say about this one, hopefully the code speaks for itself.

```csharp
public class Solution {
    public int CountElements(int[] arr) {
        // create a deduplicated set of numbers
        //  which we can reference
        HashSet<int> ints = new HashSet<int>();
        foreach(int i in arr){
            ints.Add(i);
        }

        int k = 0;

        // loop over the initial array again,
        // and use our reference to see
        // which values we should return
        foreach(int j in arr){
            if(ints.Contains(j + 1))
                k++;
        }

        return k;
    }
}
```

### April 8th - [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list){:target="_blank"}

This one took me a little longer than the previous day's, if only because I hadn't come across a linked list before, so I had to familiarise myself with that concept before attempting the problem. My newfound
understanding is that they are a collection of nodes, where each node holds both a value and a memory address at which the next node can be found. The goal is simply to return the middle node of such a linked
list, as shown in the example below:

```none
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  
(The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5,
and ans.next.next.next = NULL.
```

In order to find the middle of such a list, there are two
approaches; either traverse the entire list in order to deduce its length and then re-traverse it up until the midpoint, or a 2-pointer, fast and slow approach. I implemented the first for the actual challenge
and then became aware of the second, more efficient method after I'd already submitted my answer.

The traverse-twice approach:

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        int count = 1;
        ListNode resultNode = head;

        // traverse the list to find the count
        while(resultNode.next != null){
            resultNode = resultNode.next;
            count++;
        }

        // find the midpoint - the question requires that
        // if there are two midpoints we take the second one
        int midpoint = (int)Math.Ceiling((double)(count / 2));

        // traverse again, but stop at halfway
        for(int i = 0; i < midpoint; i++){
            head = head.next;
        }

        return head;
    }
}
```

And the fast-and-slow approach, which is a little more readable:

```csharp
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        var f = head;
        var s = head;

        // fast moves two steps for everyone one slow step,
        // until it reaches the end of the list, at which
        // point it is null.
        while(f?.next != null){
            s = s.next;
            f = f.next.next;
        }

        return s;
    }
}
```

### April 9th - [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare){:target="_blank"}

Backspace String Compare is my favourite of all the problems so far, because of it's clear practical application and also because I feel fairly comfortable with string manipulation, so this one was warm
and cozy. The problem statement reads: "given two strings ```S``` and ```T```, return if they are equal when both are typed into empty text editors. ```#``` means a backspace character."

For example:

```none
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
```

I actually started off on the wrong foot on this one, and began attempting to solve with the regex ```@"[a-z]{1}\#"``` before realising that of course, you can press backspace multiple times consecutively. Given
that char arrays were already fresh in my mind from the Group Anagrams challenge, that was my next idea, which worked rather nicely.

```csharp
public class Solution {
    public bool BackspaceCompare(string S, string T) {
        char[] sca = S.ToCharArray();
        char[] tca = T.ToCharArray();

        // create empty strings to write to
        string s = System.String.Empty;
        string t = System.String.Empty;

        foreach(char c in sca){
            if(c == '#'){
                if(s.Length > 0)
                    // if backspace is pressed, remove the
                    // last character of our new string
                    s= s.Remove(s.Length - 1, 1);
            } else {
                // if it's an alphabetical character,
                // append it to the new string
                s += c;
            }
        }

        foreach(char d in tca){
            if(d == '#'){
                if(t.Length > 0)
                    t = t.Remove(t.Length - 1, 1);
            } else {
                t += d;
            }
        }

        return s == t;
    }
}
```

### April 10th - [Min Stack](https://leetcode.com/problems/min-stack){:target="_blank"}

Another problem that admittedly I thought was quite easy - possibly too easy for day 10 of the challenge, which presumably is going to get progressively harder - although my implementation is definitely not
the most optimal. The task is to design a stack that supports push, pop, top and retrieving the minimum element of the stack, which in C# essentially boils down to whether or not you can construct a class correctly,
and fortunately, I can.

Example:

```none
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

Lists aren't especially fast and some of the methods I used to manipulate them are even slower, but I do think their redeeming qualities here is that the code is incredibly readable.

```csharp
public class MinStack {

    List<int> stack = new List<int>();

    public MinStack() {}

    public void Push(int x) {
        stack.Add(x);
    }

    public void Pop() {
        stack.RemoveAt(stack.Count - 1);
    }

    public int Top() {
        return stack.Last();
    }

    public int GetMin() {
        return stack.Min();
    }
}
```

### In conclusion

The past five days have certainly been less of a grind than the first five, which is hopefully a sign that I am improving, both in my knowledge of C# and in my methodology for approaching these
kinds of problems. I am hoping the next five days will see a meaningful increase in difficulty though as I'm keen to keep challenging myself, but either way, expect to see 5 more solutions
published and discussed here on April 15th!
