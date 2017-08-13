/*
 Codingame challenge
 Name : Temperatures
 Category : Classic puzzle - easy level
 URL : https://www.codingame.com/training/easy/temperatures
 Selected programming language : Python 3.5.3
*/
/* -----------------------------------------------------------------------------------	
The Goal

In this exercise, you have to analyze records of temperature to find the closest to zero.

	
Sample temperatures
Here, -1 is the closest to 0.
 	Rules

Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
 	Game Input

Your program must read the data from the standard input and write the result on the standard output.
Input
Line 1: N, the number of temperatures to analyze

Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
Example
Input
5
1 -2 -8 4 5
Output
-----------------------------------------------------------------------------------	
*/

#include <iostream>
using namespace std;

int main()
{
    int n; // the number of temperatures to analyse
    cin >> n;
    
    if (n == 0)
    {
        cout << 0 << endl;
        return 0;
    }
    cin.ignore();
    int max;
    int val;
    
    cin >> max;

    for (int i = 1; i < n; i++)
    {
        cin >> val;    
        if(abs(val) < abs(max) || max < 0 && val == -max)
        {
            max = val;
        }
    }

    cout << max << endl;
    return 0;
}