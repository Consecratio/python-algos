'''
Write a function, that takes an integer (n), and returns
the n'th number in the fibonacci sequence.

For example, fib(5) would return 5 as 5 is the fifth number
in the fibonacci sequence.

Params:
1 <= n <= 100
'''

def fib(n, memo = {}):
    # base cases
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    
    return memo[n]


print(fib(3))
print(fib(4))
print(fib(8))
print(fib(100))