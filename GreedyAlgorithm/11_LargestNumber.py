'''
Problem Definition :
Given an array of numbers, arrange them in a way that yields the largest value.
For example, if the given numbers are {54, 546, 548, 60},
the arrangement 6054854654 gives the largest value.
And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
then the arrangement 998764543431 gives the largest value

**************************************************************
map() function returns a map object(which is an iterator) of the results after applying the given function to each
item of a given iterable (list, tuple etc.)
Syntax :
=======
map(fun, iter)
Parameters :
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
Note: You can pass one or more iterable to the map() function.

The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.

UsefulLink refered while solving the problem: https://www.geeksforgeeks.org/python-map-function/
https://www.w3schools.com/python/ref_string_join.asp
https://www.geeksforgeeks.org/permutation-and-combination-in-python
https://docs.python.org/3/library/itertools.html
'''
from itertools import permutations


def largestvalue(values):
    lst = []
    for i in permutations(values, len(values)):
        lst.append("".join(map(str, i)))
    return max(lst)


inputValuesCount = int(input("How many number you want to enter"))

values = [int(input("Enter your number")) for value in range(inputValuesCount)]

print(largestvalue(values))
