new_file = open('newfile.txt',"w+")
for i in range(1,6):
    new_file.write("Line no = {} \n".format(i))
#new_file.close()   #Always close the files before you save. As it's always running in python if you don't close.
#Reading the content in the file
new_file.read()
#Seek is used to reset the cursor to it's starting position or to the place where you can choose the index.
new_file.seek(0)
#reading lines of a file
new_file.readlines()
with open("new_file.txt", mode = "w") as f:
    f.write("This is me and my friend python")
#opening an existing text file
# open("C:\\THE PATH") '\\' this is used to not confuse the interpreter as after a single '\' it can interpret as a newline or tab or a line feed
# pwd is used for present working directory(it shows your present working directory of the text file).
# with and as are another keywords for file operating to open and close.
# To solve the closing problem of a file before exiting any editor or any IDE the code is show below.
with open("new_file.txt") as new_file2:
    info = new_file2.read()
# pwd is abbreviated as present working directory(Shows the current directory)
# there are different modes for read & write both are combined together     
#Modes are there to set the type of the file
#mode = "r" read only type
#mode = "w" write or create new files
#mode = "a" will add on to new files
#mode = "r+" reading and writing of files
#mode = "w+" writing and reading(overwrites exisiting files or creates a new file!) 
with open("new_file.txt",mode = "a") as f:
    f.write('\nLine no = 6')
with open("new_file.txt",mode = "r") as f:
    files = print(f.read())
