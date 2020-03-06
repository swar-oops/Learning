#Sets are unordered collection of unique elements.
#Only 1 representative of any object.

#Creating a set

new_set = set()
#Append new element in a set
new_set.add(1) 
new_set.add(3)
new_set.add(4)
new_set.add(3) # This action will not be performed as it only takes unique elements, meaning things cannot be repeatedly used.
mylist = [1,2,3,1,3,2,4,5,6]
set(mylist)
print(mylist)
print(set(mylist))
print(new_set)
