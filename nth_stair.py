'''
SIMILAR
-------------------------------------------------------------------------
https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/

PROMPT
-------------------------------------------------------------------------
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
'''

def solution(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    
    memo[n] = solution(n - 3, memo) + solution(n - 2, memo) + solution(n - 1, memo)

    return memo[n]


print(solution(4)) # should return 7
print(solution(3)) # should return 4
print(solution(40))
