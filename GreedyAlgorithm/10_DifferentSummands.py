'''
Maximum Number of Prizes (Different Summands)
Problem Introduction:
----------------------
This is an example of a problem where a subproblem of the corresponding greedy algorithm
is slightly distinct from the initial problem.
Problem Discription:
---------------------
The goal of this problem is to represent a given positive integer number as a sum of as many
pairwise distinct positive integers as possible. That is, to find the maximum k such
that number can be written as a(1) + a(2) + ··· + a(k) where a(1) ,…,a(k) are positive
integers and a(i) != a(j) for all 1 ≤ i < j ≤ k.
Input Format: The input consists of a single integer number.
Constraints. 1 ≤ number ≤ 10^9
Output Format:In the first line, output the maximum number k such that number can be
represented as a sum of k pairwise distinct positive integers. In the second line,
output k pairwise distinct positive integers that sum up to number (if there are many
such representations, output any of them).
Sample 1
Input:
6
Output:
3
1 2 3
Sample 2
Input:
8
Output:
3
1 2 5
'''

def optimalSummand(number):
    summands = []
    remainingSum = number
    lowerNumber = 1

    if number == 1:
        summands.append(number)
    else:
        for i in range(1, remainingSum):
            if remainingSum <= 2 * lowerNumber:
                summands.append(remainingSum)
                break
            else:
                summands.append(lowerNumber)
                remainingSum = remainingSum - lowerNumber
                lowerNumber = lowerNumber + 1

    return len(summands),summands

number = int(input("Enter your number"))
print(optimalSummand(number))