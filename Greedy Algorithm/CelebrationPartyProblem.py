'''
Problem Definition:
==================
Let's consider the following situation. You've invited a lot of children to a celebration party,
and you want to entertain them and also teach them something in the process. You are going to
hire a few teachers and divide the children into groups and assign a teacher to each of the groups.
This teacher will work with this group through the whole party.

But you know that for a teacher to work with a group of children efficiently children of that
group should be of relatively the same age. More specifically age of any two children in the
same group should differ by at most, one year.

Also, you want to minimize the number of groups. Because you want to hire fewer teachers,
and spend the money on presents and other kinds of entertainment for the children.
So, you need to divide children into the minimum possible number of groups.
Such that the age of any two children in any group differs by at most one year.
'''

def min_no_of_child_group(agesOfChildren):
    ageRange = agesOfChildren[0] + 1
    i = 0
    group = 1
    while i < len(agesOfChildren):
        if agesOfChildren[i] <= ageRange:
            i +=1
        else:
            ageRange = agesOfChildren[i]+1
            group += 1
            i += 1
    return group

totalNoOfChildern = int(input("Enter the total no of children in party"))
agesOfChildren = [float(input("Enter the age of child {}".format(childAge))) for childAge in range(totalNoOfChildern)]
agesOfChildren.sort()
print(min_no_of_child_group(agesOfChildren))