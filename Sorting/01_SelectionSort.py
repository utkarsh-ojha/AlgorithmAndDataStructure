'''
The selection sort algorithm sorts an array by repeatedly finding the minimum
element (considering ascending order) from unsorted part and putting it at the beginning.
The algorithm maintains two sub arrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order)
from the unsorted subarray is picked and moved to the sorted subarray.

RunTime complexity is: O(n^2)

Advantages -
++++++++++++
* Selection sort algorithm is 60% more efficient than bubble sort algorithm.
* Selection sort algorithm is easy to implement.
* Selection sort algorithm can be used for small data sets, unfortunately Insertion sort algorithm best suitable for it.
Disadvantages -
--------------
* Running time of Selection sort algorithm is very poor of 0 (n2).
* Insertion sort algorithm is far better than selection sort algorithm.
'''

noOfElements = int(input("How many elements you wanted to insert"))
myList = [int(input("Enter your element {}".format(i))) for i in range(noOfElements)]

def selectionSort(myList):
    for i in range(len(myList)):
        minIndex = i
        for j in range(i+1, len(myList)):
            if myList[minIndex] > myList[j]:
                minIndex = j

        myList[i], myList[minIndex] = myList[minIndex], myList[i]
    return myList

print(selectionSort(myList))