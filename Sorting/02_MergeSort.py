'''
Merge sort is the algorithm which follows divide and conquer approach.
Consider an array A of n number of elements. The algorithm processes the elements
in 3 steps.

1> If A Contains 0 or 1 elements then it is already sorted, otherwise,
   Divide A into two sub-array of equal number of elements.
2> Conquer means sort the two sub-arrays recursively using the merge sort.
3> Combine the sub-arrays to form a single final sorted array maintaining the
   ordering of the array.

The main idea behind merge sort is that, the short list takes less time to be sorted.

MERGE_SORT(ARR, BEG, END)
Step 1:
IF BEG < END
SET MID = (BEG + END)/2
CALL MERGE_SORT (ARR, BEG, MID)
CALL MERGE_SORT (ARR, MID + 1, END)
MERGE (ARR, BEG, MID, END)
[END OF IF]
Step 2: END
'''


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        leftHalf = myList[:mid]
        rightHalf = myList[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                myList[k] = leftHalf[i]
                i += 1
                k += 1
            else:
                myList[k] = rightHalf[j]
                j += 1
                k += 1

        while i < len(leftHalf):
            myList[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            myList[k] = rightHalf[j]
            j += 1
            k += 1
        return myList
    else:
        return myList

noOfElements = int(input("How many elements you wanted to insert"))
myList = [int(input("Enter your element {}".format(i))) for i in range(noOfElements)]

print(mergeSort(myList))


















