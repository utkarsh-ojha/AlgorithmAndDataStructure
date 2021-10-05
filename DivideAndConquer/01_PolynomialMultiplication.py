'''
Problem definition:
multiply two polynomials equation.

A[] represents coefficients of first polynomial
B[] represents coefficients of second polynomial
sizeOfA and sizeOfB are sizes of A[] and B[] respectively

Important Links:
https://www.geeksforgeeks.org/strassens-matrix-multiplication/
'''

orderOfA = int(input("Enter the order of Polynomial equation A : "))
orderOfB = int(input("Enter the order of Polynomial equation B : "))

A = [int(input("Enter the {} order coeficient".format(orderOfA - i))) for i in range(orderOfA)]
B = [int(input("Enter the {} order coeficient".format(orderOfB - i))) for i in range(orderOfB)]


# Solution-1 (Worst method to use)
# Time complexity of the below solution is O(orderOfA * orderOfB). (mn)
# If size of two polynomials are of same order, then time complexity is O(n^2).)
# ********************************************************************************************
def worstPolynomialMultiply(A, orderOfA, B, orderOfB):
    product = [0] * orderOfA + orderOfB - 1

    for i in range(orderOfA):
        for j in range(orderOfB):
            product += A[i] * B[j]
    return product

# ********************************************************************************************
# Solution-2 (Divide and conquer method)
# This solution is based on Karatsuba algorithm
# ********************************************************************************************
# def polynomialMultiplication(A, orderOfA, B, orderOfB):
#     D1 = A[0:(((orderOfA+1)//2)+1)]
#     D0 = A[(((orderOfA+1)//2)+1):]
#
#     E1 = A[:(((orderOfB + 1) // 2) + 1)]
#     E0 = A[(((orderOfB + 1) // 2) + 1):]

