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

The neighbors out of bounds (-1) and (len(array)) are always 0's

Return the array after n days
'''

def houseComp(num, array):
    memo = {0: array}
    new_arr = array

    for j in range(num):

        array = new_arr
        new_arr = []

        for i in range(len(array)):
            if i == 0:
                if array[i + 1] == 0:
                    new_arr.append(0)
                else:
                    new_arr.append(1)
            elif i == len(array) - 1:
                if array[i - 1] == 0:
                    new_arr.append(0)
                else:
                    new_arr.append(1)
            elif array[i - 1] == array[i + 1]:
                new_arr.append(0)
            else:
                new_arr.append(1)

        # base case
        # check a memo object to see if we have seen this patern before (day 0)
        if memo[0] == new_arr:
            print("FOUND")
            return memo[num % (j + 1)]
        else:
            memo[j + 1] = new_arr

    print("Not Found")
    print(memo)

    return new_arr


print(houseComp(3, [1, 0, 0, 1, 1])) # should return [1, 1, 1, 1, 0]
# print(houseComp(4000000, [1, 0, 0, 1, 1])) # leave commented out until you've got a fast solution