#
#   python: 3.8.3
#   Author: Justin Perry
#   Recreate a GUI with the tkinter module
#
#

# import modules
import tkinter as tk
from tkinter import *

class ParentWindow(Frame): # parent class
    # initialize the frame with the dunder, referencing the class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # set title of the GUI frame
        self.master.title('Check Files')
        # set size of the gui window
        self.master.geometry('500x130')
        
        
        # set empty row above first entry box and browse button
        self.empty_space = tk.Frame(self.master)
        self.empty_space.grid(row=0, column=0, columnspan=4, pady=10)

        

        

        
        
        # create the buttons
        # browse button 1
        self.btn_browse_1 = tk.Button(self.master, text='Browse...', width=15)
        self.btn_browse_1.grid(row=1, column=0, pady=4, padx=6)

        # browse button 2
        self.btn_browse_2 = tk.Button(self.master, text='Browse...', width=15)
        self.btn_browse_2.grid(row=2, column=0, pady=4, padx=6)

        # check for files button

        self.btn_check_files = tk.Button(self.master, text='Check for files...', width=15)
        self.btn_check_files.grid(row=3, column=0, pady=4, padx=6)

        

        # close program button
        self.btn_close_program = tk.Button(self.master, text='Close Program', width=15)
        self.btn_close_program.grid(row=3, column=4)

        # entry boxes

        # entry box one
        self.ent_box_1 = tk.Entry(self.master)
        self.ent_box_1.grid(row=1, column=1, padx=6, columnspan=4, sticky='EW')

        # entry box two
        self.ent_box_2 = tk.Entry(self.master)
        self.ent_box_2.grid(row=2, column=1, padx=6, columnspan=3, sticky='EW')
        













if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    # create a loop so the window can stay open while using
    # once loop is canceled, window will go away
    root.mainloop()
