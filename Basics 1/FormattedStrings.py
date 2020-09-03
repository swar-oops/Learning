name =  'Swaroop'
age = 24
#The Formatted string can perform better variable assignment. 
#Without using mutliple concatenation operator in the function by minimising the clutter and maximising the readability of the format.
print(f'My name is {name},my age is {age} years old')
#There are multiple ways to use formatted strings.
print("These are the different ways{Happy} and {Lame}".format(Happy ="(*.*)" ,Lame = '("-.-)' ))
#Using formatted string i've created 2 new variables Happy and Lame using the syntax .format(variable name = value or string).
#Another way of assigning the variable by applying indexing to place things according to the index.
print("These are my new indexes {0}.Here you go {1}".format("the First one","The Last one"))