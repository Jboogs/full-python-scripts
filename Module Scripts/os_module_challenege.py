#
#   Python Version: 3.8
#
#   Author: Justin Perry
#
#   The purpose of this script is to use the OS module to 
#   iterate through a directory, check for the .txt file extension
#   then print to the screen the files that return true with the 
#   time stamp they were modified

# import modules needed
import os
import datetime

# iterate through the desired directory using listdir() method


directory = os.listdir('C:\\test_folder\\')


def txt_finder():
    txt_files = []
    for file in directory:
        if file.endswith('.txt'):
            txt_files.append(file)
    return txt_files


        
# use the os.path.join(path, *path) method to concat the file name
# to the path

    # find the absolute path of said files
def abs_path():
    txt_file_name = txt_finder()
    absolute_path = []
    for file in txt_file_name:
        x = os.path.join('C:\\test_folder\\', file)
        absolute_path.append(x)
    return absolute_path
    

# use the getmtime() method to get the modify time stamp and append to the string
def mod_time():
    path_list = abs_path()
    list_mod_time = []
    for file in path_list:
        x = os.path.getmtime(file)
        
        list_mod_time.append(x)
    return list_mod_time

#this function will seperate the data of each list and add them together

def list_together():
    time_list = mod_time()
    file_list = abs_path()
    file_date_mod = zip(file_list, time_list)
    return list(file_date_mod)
    
    

# print each file with a .txt extension with date mod time stamp

def final_output():
    list1 = list_together()
    final_list = []
    for i in list1:
        print('Text file name and date modified: {}'.format(i))
      












if __name__ == '__main__':
    # this will begin the program
    final_output()
