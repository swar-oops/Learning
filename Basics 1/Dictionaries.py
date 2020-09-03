#Dictionaries are unordered non sequential type of structure which holds a key and a value assigned to the key,
#however list can use index to print the value of a certain index, same thing doesn't apply to dictionary,it is completely different compared to lists.
#You've to assign the key inside the "[]" to call the value inside the key of a dictionary element.
#It can store different types of elements inside the dictionary including floats, strings, lists and int etc..


#Creating a dictionary and adding elements of type string, numbers and of type list.
d = {'name1':'amazing','name2':38,'name3':[100,200,300]}     
#Re-assigning the value of name1. 
d['name1'] = 'not so amazing' 
#changing the value of list items inside a dictionary, stacking the brackets would go inside the key value and choose the index to be changed.
#We're going to change the value of index 2 to type of a string.
d['name3'][2] = "Three-Hundred"
print(d['name3'])
#to show all the keys in the dictionary.
print(d.keys())
#show all the values in dictionary
print(d.values())
#show all the items with the values in a dictionary
print(d.items())
