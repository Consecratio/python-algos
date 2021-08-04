'''
SIMILAR
-------------------------------------------------------------------------
https://leetcode.com/problems/prison-cells-after-n-days/

PROMPT
-------------------------------------------------------------------------
Write a function that takes two values, an array (arr) and an int (days).
The array will have only 0's and 1's [1, 0, 0, 0, 1, 0, 0]
And the days will be positive numbers > 0.

Each day check each number's neighbors, if they're the same (both 0's or both 1's)
then the number will change to 0.
If they are not the same, the number will change to 1.

Return the array after n days
'''