Nstring = 'Normal String' #Normally the string must be in single or double quotes.
print(Nstring)
Astring = 'Another String' 
print(Astring)
Estring = Nstring + ' ' + Astring
print(Estring) 
long_string  = ''' 
WOW
(.-0-.)
WOW
''' #The long_string starts and ends with 3 single quotes. Used to store longer string types.   
print('Concatenated' + ' ' + 'String') #Concatenated String or adding strings together. 
print(long_string)
#We can index the strings to get the assigned character to a distinct index of the string.
print(Nstring[0]) #This points the 0th element of the string and prints it.
#strings can have properties of start, stop and stepover. 
print(Nstring[0:12:2]) # This implies the string will start from 0th index and end at the 12th index point while going through the process it'll step over 2 indexes at a time.
#The string propert in detail. [start(Starts from the 0th index):end(Default will go through from start to (n-1)th index):step-over(Default is 1)]
#Negative in the string will print data from backward.
print(Astring[-1])#This will print g(The last index element).
print(Astring[::-1]) #Prints the entire string in reverse.
#Strings are immutable object.
#Nstring[3] = 'Hi'   #This new assignment will cause an error because of the immutable property of string.
Nstring = "Hello I'm a New string" #Will assign the string to Nstring.
print(Nstring)
