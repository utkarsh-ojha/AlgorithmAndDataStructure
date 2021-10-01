'''
Problem Definition:
To print nth Fibonacci Series.
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers,
starting with 0, and 1.
The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

# ***************************************************
# Solution-1 (worst solution)                                     *

def worstFibonacci(n):
    if n <=1:
        return n
    else:
        return worstFibonacci(n-1)+worstFibonacci(n-2)

# ***************************************************
# Solution-2 (Best Solution)                                      *

def bestFibonacci(n):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]
# ****************************************************

print(worstFibonacci(9))

print(bestFibonacci(10))