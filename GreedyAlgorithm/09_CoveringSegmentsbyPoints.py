'''
Covering Segments by Points
Problem Description:
===================
You are given a set of segments on a line and your goal is to mark as few points on a
line as possible so that each segment contains at least one marked point.
Task:
-----
Given a set of n segments {[a0,b0],[a1,b1]....[an-1,bn-1]} with integer coordinates
on a line, find the minimum number 'm' of points such that each segment contains at
least one point .That is,  find a set of integers X of the minimum size such that
for any segment [ai,bi] there is a point x belongs X such that ai <= x <= bi
Output:
------
the minimum number m of points on the first line and the integer coordinates of m
points (separated by spaces) on the second line
------------------------
Sample 1
Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6

0---1---2---3---4---5---6---7---8---9---10
                4-----------7  (4,7)
    1------3  (1,3)
        2-----------5  (2,5)
                    5---6   (5,6)
output:
           3------------6 (3 and 6, these two points will touch all the lines)
Explanation:
The second and the third segments contain the point with coordinate 3 while the first
and the fourth segments contain the point with coordinate 6. All the four segments
 cannot be covered by a single point, since the segments [1,3] and [5,6] are disjoint.
*****What To Do*****
To design a greedy algorithm for this problem, consider a segment with the minimum right
endpoint. What is a safe way to cover it by a point?
'''

def calculateOptimizedPoint(numOfCordinates, cordinates):
    sortedCordinate = sorted((cordinate for cordinate in cordinates), key = lambda itm:itm[0])
    points = []
    currentRange = sortedCordinate[0][1]
    points.append(currentRange)
    for i in range(numOfCordinates-1):
        if (currentRange < sortedCordinate[i][0]) or (currentRange > sortedCordinate[i][1]):
            currentRange = sortedCordinate[i][1]
            points.append(currentRange)
    return points

numOfCordinates = int(input("How many coordinate you want to input : "))
cordinates = [(int(input("Enter the a{} cordinate".format(i))),int(input("Enter the b{} cordinate".format(i)))) for i in range(numOfCordinates)]

print(calculateOptimizedPoint(numOfCordinates,cordinates))
