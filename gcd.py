'''
SIMILAR
-------------------------------------------------------------------------
https://www.codewars.com/kata/5849169a6512c5964000016e

PROMPT
-------------------------------------------------------------------------
Write a function that returns the greatest common factor of an array of positive integers. Your return value should be a number, you will only receive positive integers.
'''

import math

def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    new_dict = {1: num - 1}
    largest_num = 1
    smallest_num = 100000
    
    for i in range(num):
        if arr[i] < smallest_num:
            smallest_num = arr[i]

        for j in range(2, (smallest_num + 1)):
            if arr[i] % j == 0:
                if j in new_dict:
                    new_dict[j] += 1
                    if new_dict[j] >= new_dict[largest_num] and j > largest_num:
                        largest_num = j
                else:
                    new_dict[j] = 1
                    if new_dict[j] >= new_dict[largest_num] and j > largest_num:
                        largest_num = j
    
    return largest_num


print(generalizedGCD(5, [10, 8, 6, 4, 2]))