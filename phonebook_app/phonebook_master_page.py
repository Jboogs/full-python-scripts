#
#   Python Version: 3.8.3
#
#   Author: Justin Perry
#
#
#   Purpose: To design and create a phonebook applications
#       that connects and uses sqlite3 and tkinter to make 
#       a fully functional phone database that can be updated,
#       and queried as needed
#       
#   OS: This code was written and created in Windows 10

from tkinter import *
import tkinter as tk

# import created modules for use in app, user created
# this is the GUI module
import phonebook_gui
#  this is the functional module
import phonebook_func

# create the tkinter frame that all classes will inherit from
class ParentWindow(Frame): # parent class
    # initialize the frame with the dunder, referencing the class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # this is the master frame configuration
        self.master = master
        self.master.minsize(500, 300) # (height X width)
        self.master.maxsize(500, 300)

        # center the master frame on the users screen when opened
        # function called from the function module, always pass in self
        phonebook_func.center_window(self, 500, 300)
        # title of the application
        self.master.title('PhoneBook Application')
        #set background color
        self.master.configure(bg='#f0f0f0')
        # built in method to catch if the user clicks the 'X' in the upper
        # corner, in the windows OS, asks if user wants to quit
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # This will load the GUI from seperate module in order
        # to keep the code neet and tidy (compartimentalized)
        # module name, phonebook_gui.py
        phonebook_gui.load_gui(self)
        
        
        



if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    # create a loop so the window can stay open while using
    # once loop is canceled, window will go away
    root.mainloop()

    
    
