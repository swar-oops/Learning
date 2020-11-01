#Methods are actions on a data type in python.
Cart = ['l','k','h','p','x','t']

print(Cart.index('x')) #The index method prints the index of the available data inside the list.
print(Cart.index('k',0,3)) #This index method has array.index('string', start of the string index, end of the string index)
print(Cart.count('k')) #Count returns the number of occurences of the value in the array.
print(len(Cart)) #len() method signifies the length of the string element.
Cart.append(25) #append() method adds an element in the end of the list. 
print(Cart)
nlist = Cart.append(26)
#This way of assigning will not work as the the new list is assigning Cart.append(26) as 26 is not in the list and it modifies the list but not assign. 
print(Cart)
print(nlist)
nlist = Cart[:] #This way you can copy all the nlist elements and start applying methods.
print(nlist) 
nlist.insert(3,37) #Insert is used to insert in a specific location of the string.
print(nlist)
#You can't modify and assign a list concurrently, it has to be discretely done.


