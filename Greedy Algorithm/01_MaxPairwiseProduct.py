'''
Problem Definition:
Given a list of numbers, find the product of two number
which is maximum product which can be obtained by multiplying any two number in the given list.
'''


#solution1
# Just find the two max numbers in the list and multiply
# def maxPairwiseProduct(numbers):
#     max1 = max(numbers)
#     nums = numbers.remove(max1)
#     max2 = max(numbers)
#     return max1*max2
                           
#solution2

def maxPairwiseProduct(numbers):
    maxProduct = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            maxProduct = max(maxProduct, numbers[i]*numbers[j])
    return maxProduct

input_n = input()
input_numbers = [int(x) for x in input_n.split()]
print(input_numbers)
print(maxPairwiseProduct(input_numbers))








