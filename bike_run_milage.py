import os
# this function will write the data from the data variable to the next line
# on the test.txt file that is being openened
def write_data():
    # this is the data to be appeneded to the end of the file
    data = input('Please enter date and how many miles you biked today!\n>>>')
    # with statement opens the file and gives permission to append
    # the data variable to the and of the file
    with open('miles.txt', 'a') as f:
        # f.write() writes the data to the end of the string
        f.write(data)
        # f.close() closes the file when complete
        f.close()


# with this file open, perform the following commands
# the with statement is sort of like the while statement
# but for files
# this function calls the file and prints the data to the screen
def open_file():
    # with test.txt open, in read only mode (content cannot be changed in the file
    # saved as an instance of f
    with open('miles.txt', 'r') as f:
        #store the data inside the text in a variable, the read() method reads
        # the string values in the txt file
        data = f.read()
        # print that variable onto the screen (the text in the file)
        print(data)
        # close the file/sesion with the close() method so that nothing
        # happens to the file
        f.close()

if __name__ == '__main__':
    write_data()
    open_file()
    
    
