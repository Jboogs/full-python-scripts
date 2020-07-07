#
#   Python: 3.8.4rc1
#
#   Justin Perry
#
#   To demonstrate the Shutil module by copying all files
#   from folder A to folder B that have been edited during that day

# import shutil/os modules
import shutil
import os
from os import path
import datetime as dt
import time


seconds_day = 24*60*60

# set the source of the files
file_src = "C:\\Users\\jadam\\Desktop\\daily_files_folder\\"

# this is the destination of the files

file_dst = "C:\\Users\\jadam\\Desktop\\home_office_transfer\\"

now = time.time()
with_in_24 = now - seconds_day


def move_files():
    files = os.listdir(file_src)
    for fname in files:
        if path.getmtime(fname) < with_in_24:
            shutil.copy(file_src+fname, file_dst)
  
    
        
            
        
        
        
    





if __name__ == '__main__':
    move_files()
    

