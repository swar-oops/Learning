# Tuples are similar to lists with 1 key difference, they're immutable(cannot reassign values) and the objects inside the tuples can't be changed.
# Tuple uses parenthesis = (1,2,3)
t = (1,2,3)
t1 = [1,22,33]
t.count('2') #returns the no of occurence of the number 2 in the tuple.
t1[1] = "Two" #Tuple cannot re assign the values like this.
print(t1)
print(t)