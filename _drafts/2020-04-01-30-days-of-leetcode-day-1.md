---
layout: mendokusai
author: Jonny Spicer
title: 30 Days of Leetcode&#58; Day 1
tags: [ Software Engineering ]
---
There's quite a few 30-days-of-code challenges popping up today, given that April looks set
to be the first full month in which the entire world is forbidden from leaving our houses. As
I already have a Leetcode account and have done a very small number of the easy problems on
there, I thought I'd take a stab at theirs, and will share some or all of my solutions here.

### April 1st - Single Number

Today's problem is very simple; given a non-empty array of integers, every element appears twice except for one. Find that single one.
For example;

```none
    Input: [4,1,2,1,2]
    Output: 4
```

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> exists = 
            new Dictionary<int, int>();
        foreach (int i in nums){
            if (!exists.ContainsKey(i)){
                exists.Add(i, 1);
            } 
            else {
                exists[i] += 1;
            }
        }
        
        return exists.FirstOrDefault(x => x.Value == 1).Key;
    }
}
```

```csharp
    public class Solution {
    public int SingleNumber(int[] nums) {
        return nums.GroupBy(e => e)
                   .Where(e => e.Count() == 1)
                   .Select(e => e.First())
                   .First();
    }
}
```