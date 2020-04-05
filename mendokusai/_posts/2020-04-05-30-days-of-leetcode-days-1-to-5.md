---
layout: mendokusai
author: Jonny Spicer
title: 30 Days of Leetcode&#58; Days 1 to 5
tags: [ Software Development ]
---
There's quite a few 30-days-of-code challenges popping up this week, given that April looks set
to be the first full month in which the entire world is forbidden from leaving our houses. As
I already have a Leetcode account and have done a very small number of the easy problems on
there, I thought I'd take a stab at [theirs](https://leetcode.com/discuss/general-discussion/551411/30-Day-LeetCoding-Challenge){:target="_blank"}, and will share some or all of my solutions here.

### April 1st - [Single Number](https://leetcode.com/problems/single-number/){:target="_blank"}

Today's problem is very simple; given a non-empty array of integers, every element appears twice except for one. Find that single one.
For example;

```none
    Input: [4,1,2,1,2]
    Output: 4
```

I'd actually already completed this problem on Leetcode a few months ago, however I'd used a Linq query which aren't exactly the most performant things in the world:

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        // I think this is pretty self explanatory!
        return nums.GroupBy(e => e)
                   .Where(e => e.Count() == 1)
                   .Select(e => e.First())
                   .First();
    }
}
```

I decided to retry without using Linq (at least until the end), and this solution works (and works faster than its predecessor), however I think it nicely illustrates one of the points I
made in [yesterday's blog,](/mendokusai/2020/04/04/think-deeply-about-simple-things){:target="_blank"} because I have made a pretty embarrassing oversight here - ```exists``` should simply
be a List, and then rather than incrementing an index's count if it already exists, I should remove it from the list instead, which would leave only one number left. Ultimately, this is why
doing these kinds of problems are useful - it's quick and easy to compare your code to others' afterwards, and making silly mistakes like this one in a sandbox environment are much loss
costly than making them in a professional context.

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        // create a Dictionary for every number in the array
        // and how many times it appears
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

There is actually a much simpler solution to this using bitwise XOR, but I think it's a lot less intuitive, and from the discussions I've seen around this question it seems like
you essentially have to know that you should use XOR here rather than be able to figure it out. This works based off the idea that XOR of a number with itself is 0, and XOR of a number
with 0 is the original number - so as we go through the list, each number will cancel itself out, until only the unpaired one remains in the result value.

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        int result = 0;
        foreach (var i in nums)
            result ^= i;
        return result;
    }
}
```

### April 2nd - [Happy Number](https://leetcode.com/problems/happy-number){:target="_blank"}

The problem statement here is simply to write an algorithm that returns true if a number is "happy", and false otherwise. As per the problem itself: "a happy number is a number defined by the
following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which process ends in 1 are happy numbers."

And the example given:

```none
Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

For this one I managed to think a little deeper before beginning to type, and realised that once any number has been repeated in a cycle, the cycle will loop endlessly, therefore the number
cannot be happy (and conversely, were the cycle to never repeat, obviously eventually it would hit 1).

```csharp
public class Solution {
    public bool IsHappy(int n) {
        List<int> seen = new List<int>();
        while (n != 1){
            // j is the value into which we are calculating the
            // sum of the squares of digits
            int j = 0;
            while (n > 0){
                // using modulus, we can process each digit on
                // its own rather than doing something ham-fisted
                // like splitting the int into a char[]
                j += ((n % 10) * (n % 10));
                n -= (n % 10);
                n /= 10;
            }
            if(seen.Contains(j)){
                return false;
            } else {
                seen.Add(j);
            }
            n = j;
        }
        return true;
    }
}
```

### April 3rd - [Maximum Subarray](https://leetcode.com/problems/maximum-subarray){:target="_blank"}

For today's entry we must take an array of integers and find the contiguous subarray with the largest sum, which we must then return. This is also one that I feel like I did a
little clumsily (and indeed one it took me significantly longer than the first two problems to solve), but the consensus is that the optimal solution (which implements [Kadane's Algorithm,](https://algorithms.tutorialhorizon.com/kadanes-algorithm-maximum-subarray-problem/){:target="_blank"}) is again fairly hard to intuit.

Example:

```none
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Using nested for loops always makes me feel a little queasy, and I knew while doing it that this brute force method of checking every possible subarray was not going to be the most efficient
way to solve the problem - but it does solve the problem.

```csharp
public class Solution {
    public int MaxSubArray(int[] nums) {
        int currentMax = nums[0];
       // for every int in nums...
        for(int i = 0; i < nums.Length; i++ ){
            int j = 0;
            //...check every subarray by moving
            // forward in the nums array...
            for (int k = 0; k < (nums.Length - i); k++){
                j += nums[k + i];
                // ...and see what's biggest
                if(currentMax < j)
                    currentMax = j;
            }
        }
        return currentMax;
    }
}
```

An implementation of Kadane's Algorithm, both easier to grok for humans as well as more efficient for machines:

```csharp
public class Solution{
    public int MaxSubArray(int[] nums){
        int current = 0;
        int currentMax = nums[0]

        for(int i = 0; i < nums.Length; i++){
            // add this value in the array to the current sum
            current += nums[i];
            // if this value in the array is bigger than
            // the current sum...
            if(nums[i] > current){
                //...then this value becomes the current sum
                current = nums[i];
            }
            if(current > currentMax){
                currentMax = current;
            }
        }
        return currentMax;
    }
}
```

### April 4th - [Move Zeroes](https://leetcode.com/problems/move-zeroes/){:target="_blank"}

Another short and sweet problem statement: "given an array ```nums```, write a function to move all ```0```'s to the end of it while maintaing the relative orrder of the non-zero elements.

Example:

```none
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

This one seems simple, but I ended up wrestling with it for hours - again, largely because I did not fully think through the problem before I began writing code to try and solve it, and then
became stuck viewing the problem only through the lens of the code I'd already written. For example, I spent a long time checking to see whether or not a value *was* 0 in the array rather
than was *not*, and similarly it took me an embarassingly long time to realise that I had ```j > zeroCount``` instead of ```j >= zeroCount``` in the second for loop. Still, I got there in the
end.

```csharp
public class Solution {
    public void MoveZeroes(int[] nums) {
        int zeroCount = 0;
        for(int i = 0; i < nums.Length; i++){
            //if a value isn't 0...
            if(nums[i] != 0){
                //move it to the next available index
                nums[zeroCount++] = nums[i];
            }
        }
        // fill the rest of the array with 0s
        for (int j = nums.Length - 1; j >= zeroCount; j--){
            nums[j] = 0;
        }
    }
}
```

### April 5th - [Best Time To Buy And Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/){:target="_blank"}

Today's problem: design an algorithm to find the maximum profit from buying and selling stocks from an array in which each element corresponds to the stock price for that day. Any number
of transactions can be made, however only one transaction can be made at a time (eg once you have bought once, you must sell once before you can buy again).

Example:

```none
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1)
             and sell on day 3 (price = 5),
             profit = 5-1 = 4.

             Then buy on day 4 (price = 3)
             and sell on day 5 (price = 6),
             profit = 6-3 = 3.
```

This is the first problem I solved after yesterday's blog, and consequently the first one which I was determined to consider for a meaningful amount of time before writing any code. It may
be a fluke, or possibly this was an easier problem than the previous two days', however it seemed to pay off as I solved this one basically instantly. The important thing to realise here is
that we have the gift of omniscience, and at every point in time we can know what is happening at every other point in time - including seeing into the future by reading the rest of the array!

```csharp
public class Solution {
    public int MaxProfit(int[] prices) {
        bool bought = false;
        int profit = 0;
        int buyPrice = 0;

        for(int i = 0; i < prices.Length; i++){
            if(bought == false){
                // we want to buy the dip; if we know the price
                // is going to go up tomorrow, we should buy now!
                // (unless there ominously is no tomorrow)
                if((i + 1) < prices.Length &&
                prices[i + 1] > prices[i])
                {
                    bought = true;
                    buyPrice = prices[i];
                }
            } else {
                // similarly, if the price is about to go down,
                // it's time to dump our whole portfolio
                // (which we should also do if the world
                // is about to end)
                if((i + 1) == prices.Length ||
                ((i + 1) < prices.Length &&
                prices[i + 1] < prices[i]))
                {
                    bought = false;
                    profit += (prices[i] - buyPrice);
                }
            }
        }

        return profit;
    }
}
```

If you made it this far, thank you for reading! I will be endeavouring to do all 30 days of the challenge and plan to keep writing up my solutions in this blog every few days or so.
