'''
Problem Definition:
In the "Long Hike" problem, we were given food items, their total weights and energy values,
and we wanted to maximize the total energy value of fractions of food items that fit into
the knapsack of capacity W.

To solve the problem we have converted this problem in mathematical problem :
In the new mathematical formulation, we are again given a knapsack of capacity W
and some items. We know the weights and values of the items, and we want to maximize
the total value of fractions of items that fit into the knapsack.

This is a fractional Knapsack problem
'''

def calculateFNP(knapsackCapacity, weight, value):
    remainingKnapsackCapacity = knapsackCapacity
    maxValue = 0
    while remainingKnapsackCapacity != 0:
        for pair in sorted(zip(weight, value), key=lambda itm: itm[1] / itm[0], reverse= True):
            if pair[0] <= remainingKnapsackCapacity:
                maxValue += pair[1]
                remainingKnapsackCapacity -= pair[0]
            else:
                maxValue += remainingKnapsackCapacity* (pair[1]/pair[0])
                remainingKnapsackCapacity = 0
    return maxValue


knapsackCapacity = float(input("Enter your knapsack capacity"))
noOfItems = int(input("How many items with value you want to enter : "))
valueUponWeight = []
weight = []
value = []
for i in range(noOfItems):
    weight.append(int(input("Enter the item weight ")))
    value.append(int(input("Enter the value of the amount ")))
print(calculateFNP(knapsackCapacity, weight, value))
