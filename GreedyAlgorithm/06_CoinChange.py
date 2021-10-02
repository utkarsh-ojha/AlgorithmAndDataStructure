'''
Problem Description:
===================
The goal in this problem is to find the minimum number of coins needed to change the
input value (an integer) into coins with denominations 1, 5, and 10.
Input Format: The input consists of a single integer m
Constraints: 1 ≤ m ≤ 10^3
Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes m.
Sample 1
--------
Input:
2
Output:
2
Explanation:
2 = 1 + 1.
Sample 2.
Input:
28
Output:
6
Explanation:
28 = 10 + 10 + 5 + 1 + 1 + 1.
'''
#solution-1
# *******************************************
def calculateChange(amount):
    coinOfTen = amount // 10
    coinOfFive = (amount%10) // 5
    coinOfOne = (amount % 10) % 5

    return (coinOfTen+coinOfFive+coinOfOne)
# *******************************************

# Solution-2
# *******************************************

def calculateCoinChange(amount):
    count = 0
    coin = [10,5,1]
    for i in range(len(coin)):
        n = amount // coin[i]
        count += n
        amount = amount - n*coin[i]
    return count
# ********************************************
userAmount = int(input("Enter the amount"))

print(calculateChange(userAmount))
print(calculateCoinChange(userAmount))

