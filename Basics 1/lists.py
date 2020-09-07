#Lists are similar to arrays in general programming languages such as C, C++ & Java etc
#Lists can store data type such as string, integer & float.
#These are the basic and the most complex data structures as it is used in almost every program related to data structures.

my_list = ['three','4','five','six','7']
new_list = [] + my_list #concatenating a list
print(new_list) 
print(new_list[1:])     #printing a sliced list from index of 1 to end of the list.
print(new_list[3])      #printing index 3 of the new_list
print(new_list[0].upper()) #making the first index value to be all caps or an uppercase word.
new_list.append('eight')    #list will append a new value at the end of the list.
print(new_list)         
print(len(new_list))    #this will print the length of the list by using len(listname)
print(new_list)
new_list = ['t','m','k','g','p','b']
new_list.sort()         #This will sort the list.
print(new_list)
new_list.pop(3)         #popping the value out.
print(new_list)         
new_list.reverse()      #reverses the list.
num_list = [1,9,3,6,7,5]
num_list.sort() 
print(num_list)
char_list = ['Orange','Apple',] 
