'''
Problem Introduction:
===================
A thief finds much more loot than his bag can fit. Help him to find the most valuable
combination of items assuming that any fraction of a loot item can be put into his bag.
Problem Description:
-------------------
Task: The goal of this code problem is to implement an algorithm for the fractional
knapsack problem.
Input Format:
-----------
The first line of the input contains the number 𝑛 of items and the
capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items.
The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item,respectively.
Constraints: 1≤𝑛≤103,0≤𝑊 ≤2·106;0≤𝑣𝑖 ≤2·106,0<𝑤𝑖 ≤2·106 for all 1≤𝑖≤𝑛.All the numbers are integers.
Output Format:
-------------
Output the maximal value of fractions of items that fit into the knapsack.
The absolute value of the difference between the answer of your program and the
optimal value should be at most −3 your answer, while being computed correctly,
can turn out to be wrong because of rounding issues).
Sample 1.
Input:
3 50
60 20
100 50
120 30

Output:
180.0000
To achieve the value 180, we take the first item and the third item into the bag.
'''
# Complexity: nlogn
def calculateMaxValue(totalKnapsackCapacity, weight, values):
    currentKnapsackCapacity = totalKnapsackCapacity
    maxValueGained = 0
    while currentKnapsackCapacity !=0:
        for pair in sorted(zip(weight,values), key = lambda itm:itm[1]/itm[0],reverse=True):
            if pair[0] <= currentKnapsackCapacity:
                maxValueGained += pair[0]* (pair[1]/pair[0])
                currentKnapsackCapacity -= pair[0]
            else:
                maxValueGained += currentKnapsackCapacity * (pair[1]/pair[0])
                currentKnapsackCapacity = 0
    return maxValueGained



totalNumOfItems = int(input("Enter the total number items"))
totalKnapsackCapacity = int(input("Enter the knapsack capacity"))
weight = []
values = []
for i in range(totalNumOfItems):
    values.append(int(input("Enter the value of item {}".format(i))))
    weight.append(int(input("Enter the weight of item {}".format(i))))

print(calculateMaxValue(totalKnapsackCapacity,weight,values))



