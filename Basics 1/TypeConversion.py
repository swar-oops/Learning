#converting a data type to a different type is known as type casting.
#Example    
a = '100' #String variable
b = type(int(a)) #Converting the string variable with the method type() to change the string variable to the type "int" 
print(b) #Storing the converted type in variable b and printing b.
#Another way implementing the same as above would look like this:
Type = type(int(str(100)))
print(Type)
#Both the results are going to print the same output but, the 1st method declares different variables to help us understand the process of casting in the structural way.