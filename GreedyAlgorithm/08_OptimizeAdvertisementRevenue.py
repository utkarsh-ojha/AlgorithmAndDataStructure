'''
Maximum Advertisement Revenue:
Problem statement:
==================
We have n advertising slots that we want to sell to advertisers. Each slot gets a
different number of clicks and each advertiser is willing to pay a different amount.
How do you pair the advertiser with the slot to maximize you click-revenue?
Input:
------
Sequence of integer prices price 1, price 2 ,…,pricen and
a sequence of click-counts count1,count2,…,countn.
Output:
-------
The maximum value achievable by matching prices with click counts

This is the more general problem statement:
==---------===========---------=========------==
Problem:
Find the maximum dot product of two sequences of numbers.
Inputs:	Two sequences of n positive integers.
Output:	The maximum sum of pair-wise multiplications of the values.
'''

def optimizeAdvertRev(clicks,prices):
    clicks.sort(reverse=True)
    prices.sort(reverse=True)
    priceClicksPair = zip(clicks,prices)
    maxRevenue = sum((clickPrice[0]*clickPrice[1]) for clickPrice in priceClicksPair)
    return maxRevenue

totalNumberOfSlots = int(input("Enter the total number of slots available for advertisment"))

clicks = [int(input("Enter the click count {} of sequence" . format(i))) for i in range(totalNumberOfSlots)]
prices = [int(input("Enter the prices list item number {}" . format(i))) for i in range(totalNumberOfSlots)]

print(optimizeAdvertRev(clicks, prices))

