/*
 Codingame challenge
 Name : Kolakoski Sequence
 Category : Community puzzles
 URL : https://www.codingame.com/training/easy/kolakoski-sequence
 Selected programming language : Python 3.5.3
*/
/* -----------------------------------------------------------------------------------	
Goal

A Kolakoski sequence, named after William Kolakoski, is an infinite sequence of digits whose run lengths reduce to the sequence itself.

For example, the Kolakoski sequence for the numbers 1 and 2 is
1,2,2,1,1,2,1,2,2,1,2,2,1,1,2,1,1,2,2,1,2,1,1,2,1,2,2,1,1…
because, when writing down the successive run lengths of 1s and 2s, you get the same sequence back:

Sequence:    1  2 2  1 1  2  1  2 2  1  2 2 …
             ↕   ↕    ↕   ↕  ↕   ↕   ↕   ↕
Run lengths: 1   2    2   1  1   2   1   2  …  ← same sequence
Your goal is to output the first N elements of the Kolakoski sequence given its first two distinct digits A and B.
Input
Line 1: The number N of digits to output
Line 2: The digits A and B which will form the sequence, in that order
Output
The Kolakoski sequence, without any separator.
Constraints
1 ≤ N ≤ 1000
1 ≤ A ≤ 9
1 ≤ B ≤ 9
A ≠ B
Example
Input
10
1 2
Output
1221121221
-----------------------------------------------------------------------------------	
*/

using System;

class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());  // the number of digits to output
        string[] inputs = Console.ReadLine().Split(' '); // the digits A and B
        int[] pair={int.Parse(inputs[0]),int.Parse(inputs[1])};  // split A and B in pair[] array
        int alternateseqidx = 0;    // alternating 0 and 1
        string nextruns = "";   // next sequence of digits to run
        int idxrun = 0;
        int runlength = pair[0];
        int c = pair[0];

        while(true)
        {
            for (int i = 0; i < runlength; i++)
            {
                nextruns += pair[alternateseqidx].ToString();
                if (nextruns.Length >= N)
                {
                    Console.WriteLine(nextruns);
                    return;
                }
            }

            alternateseqidx = (alternateseqidx + 1) % 2;
            idxrun += 1;
            c = pair[alternateseqidx];

            if(idxrun == nextruns.Length)
            {
                nextruns += c.ToString();
                runlength = c - 1;
            }
            else
            {
                runlength = (int)Char.GetNumericValue(nextruns[idxrun]);
            }    
        }
    }
}