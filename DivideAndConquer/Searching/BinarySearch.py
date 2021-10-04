'''
Definition:
===========
Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key
is less than the item in the middle of the interval, narrow the interval to the lower
half. Otherwise, narrow it to the upper half. Repeatedly check until the value is
found or the interval is empty.
'''

listLen = int(input("Enter the list of your length : "))
userList = [int(input("Enter item number {} ".format(i))) for i in range(listLen)]
userList.sort()
itemToSearch = int(input("Enter the item to search"))

# *********************************************************************
# Solution-1
# *********************************************************************
def recursiveBinarySearch(sortedAry,beg,end,itemToSearch):
    if end >= 1:
        mid = ((end-1)+beg) // 2
        if itemToSearch == sortedAry[mid]:
            return mid
        elif itemToSearch < sortedAry[mid]:
            return recursiveBinarySearch(sortedAry,beg,(mid - 1),itemToSearch)
        else:
            return recursiveBinarySearch(sortedAry,(mid+1),end,itemToSearch)
    else:
        return -1
# *********************************************************************
# Solution-2
# *********************************************************************
def iterativeBinarySearch(sortedAry,beg,end,itemToSearch):
    while beg <= end:
        mid = beg+(end-1) // 2

        if itemToSearch == sortedAry[mid]:
            return mid
        elif itemToSearch < sortedAry[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

# *********************************************************************


recursiveResult = recursiveBinarySearch(userList, 0, len(userList)-1, itemToSearch)

if recursiveResult == -1:
    print("Not found")
else:
    print("Item found at index : ",recursiveResult)


# *********************************************************************

iterativeResult = iterativeBinarySearch(userList, 0, len(userList)-1, itemToSearch)

if iterativeResult == -1:
    print("Not found")
else:
    print("Item found at index : ",iterativeResult)

# *********************************************************************

assert iterativeResult == recursiveResult, "Result from both the function is different"