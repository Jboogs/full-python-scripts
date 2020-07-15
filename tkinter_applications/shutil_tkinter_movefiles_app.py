#
#   python: 3.8.4
#   Author: Justin Perry
#   Create an app that allows a user to choose a directory
#   that will be copied to another directory based off
#   the mod time (last 24 hours) of the files in the directory
#
#   The move button moves files from one folder to another



# import modules
import tkinter as tk
from tkinter import *
import os
from os import *
from tkinter import filedialog as fd
import time
import shutil

class ParentWindow(Frame): # parent class
    # initialize the frame with the dunder, referencing the class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # set title of the GUI frame
        self.master.title('Copy Files')
        # set size of the gui window
        self.master.geometry('500x200')

        # variables
        self.copy_from_directory = StringVar()
        self.copy_to_directory = StringVar()
        
        

        # labels for the list boxes
        self.lbl_copy_from = tk.Label(self.master, text='Directory path to copy from:')
        self.lbl_copy_from.grid(row=0, column=0, padx=10, sticky='we')

        self.lbl_copy_to = tk.Label(self.master, text='Directory to copy to:')
        self.lbl_copy_to.grid(row=2, column=0, padx=10, sticky='we')

        # label to update if successful or not
        self.lbl_update_blank = tk.Label(self.master, text='')
        self.lbl_update_blank.grid(row=5, column=0)

        #choose directory buttons
        self.btn_choose_copy_from = tk.Button(self.master, text='Choose Directory')
        self.btn_choose_copy_from.grid(row=1, column=0, padx=10, sticky='we')
        self.btn_choose_copy_from.configure(command=self.choose_copy_from_direct)

        self.btn_choose_copy_to = tk.Button(self.master, text='Choose Directory')
        self.btn_choose_copy_to.grid(row=3, column=0, padx=10, sticky='we')
        self.btn_choose_copy_to.configure(command=self.choose_copy_to_direct)

        # copy files button
        self.btn_copy_files = tk.Button(self.master, text='Copy Files')
        self.btn_copy_files.grid(row=4, column=0, padx=10, sticky='we')
        self.btn_copy_files.configure(command=self.copy_files)

        #move files
        self.btn_move_files = tk.Button(self.master, text='Move Files')
        self.btn_move_files.grid(row=4, column=1, padx=10, sticky='ew')
        self.btn_move_files.configure(command=self.move_files)

        # clear list boxes button
        self.btn_clear = tk.Button(self.master, text='Clear selection')
        self.btn_clear.grid(row=4, column=2, padx=10, sticky='ew')
        self.btn_clear.configure(command=self.clear_list_boxes)
        

        #list boxes to display chosen directory paths
        self.lst_copy_from = tk.Listbox(self.master, height=1, width=40)
        self.lst_copy_from.grid(row=1, column=1, columnspan=3)

        self.lst_copy_to = tk.Listbox(self.master, height=1, width=40)
        self.lst_copy_to.grid(row=3, column=1, columnspan=3)

        #close application button/ with cancel command
        self.btn_close = tk.Button(self.master, text='Close')
        self.btn_close.grid(row=4, column=3, pady=20, sticky='ew')
        self.btn_close.configure(command=self.cancel)

    # define function for choosing directory 1
    def choose_copy_from_direct(self): 
        direc_name_copy_from = fd.askdirectory(initialdir = "/")
        self.lst_copy_from.insert(END, direc_name_copy_from)
        self.copy_from_directory.set(direc_name_copy_from+'/')
        self.lbl_update_blank.config(text='Copy from Directory Chosen')
        print(self.copy_from_directory.get())
    # define function to choose directory 2
    def choose_copy_to_direct(self): 
        direc_name_copy_to = fd.askdirectory(initialdir = "/")
        self.lst_copy_to.insert(END, direc_name_copy_to)
        self.copy_to_directory.set(direc_name_copy_to+'/')
        self.lbl_update_blank.config(text='Copy to Directory Chosen')
        print(self.copy_to_directory.get())
    # define the function to clear lst boxes
    def clear_list_boxes(self):
        self.lst_copy_from.delete(0)
        self.lst_copy_to.delete(0)
        self.copy_to_directory.set('')
        self.copy_from_directory.set('')
        self.lbl_update_blank.config(text='Selection Cleared')

    # this will move files from one folder to another
    def move_files(self):
        if self.copy_to_directory.get() == '' or self.copy_from_directory.get() == '':
            self.lbl_update_blank.config(text='Please select both options')
        else:
            files = os.listdir(self.copy_from_directory.get())
            for i in files:
                shutil.move(self.copy_from_directory.get()+i, self.copy_to_directory.get())
            self.lbl_update_blank.config(text='This will move files, delete folder')
    # this will copy all files with in a folder that have been altered or created with in the
    # last 24 hours
    def copy_files(self):
        if self.copy_to_directory.get() == '' or self.copy_from_directory.get() == '':
            self.lbl_update_blank.config(text='Please select both options')
        else:
            seconds_day = 24*60*60
            now = time.time()
            with_in_24 = now - seconds_day
            files = os.listdir(self.copy_from_directory.get())
            for i in files:
                if path.getmtime(self.copy_from_directory.get()+i) > with_in_24:
                    shutil.copy(self.copy_from_directory.get()+i, self.copy_to_directory.get())
            self.lbl_update_blank.config(text='Files Copied Succesfully')
        

    def cancel(self):
        self.master.destroy()




if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    # create a loop so the window can stay open while using
    # once loop is canceled, window will go away
    root.mainloop()
    
