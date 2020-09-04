username = input()  #Taking the username as input
password = input()  #Also taking the password as input

pLength = "*" * len(password) #Storing the password using asterisk inside the variable pLength.   

print('Your Username is {0} and your password is {1} of length {2} characters.'.format(username,pLength,len(password)))

#Printing the result using Formatted Strings.