#the algorithm for binary search

#Binary Search Algorithm:

search = input("Get search from user!")

min = 0
max = records - 1       #can also use len(listName) for 'records' value

mid = int((min + max) / 2)

#this is for INCREASING order
while (min < max and search != listName[mid]):

   if search < listName[mid]:
       max = mid - 1
   else:
       min = mid + 1

   mid = int((min + max) / 2)

if search == listName[mid]:
    #found them! use 'mid' for index of found search item
    print()

else:
    #boooo not found
    print()