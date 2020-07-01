# import tkinter module and sub modules

from tkinter import*
import tkinter as tk

# import custom made modules

import phonebook_master_page
import phonebook_func

# define the function that loads the GUI and the layout below

def load_gui(self):

    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets over pack.
    """

# define and paint labels for info boxes useing lbl_ as the variable name
    # First name, last name, Phone, email, user
    self.lbl_fname = tk.Label(self.master, text='First Name:')
    # paint first name label
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10, 0), sticky=N+W)
    # last name label
    self.lbl_lname = tk.Label(self.master, text='Last Name:')
    # paint last name label
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10, 0), sticky=N+W)
    # phone label declaration
    self.lbl_phone = tk.Label(self.master, text='Phone Number:')
    # paint phone number label
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10, 0), sticky=N+W)
    # email address label
    self.lbl_email = tk.Label(self.master, text='Email Address:')
    # paint email label
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10, 0), sticky=N+W)
    #information box label
    self.lbl_info = tk.Label(self.master, text='Information:')
    #paint info label
    self.lbl_info.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

#entry boxes for information txt_ label for variables

    #first name entry box declaration
    self.txt_fname = tk.Entry(self.master, text='')
    #paint fname entry
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    #Last name entry box declaration
    self.txt_lname = tk.Entry(self.master, text='')
    #paint lname entry
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    #Phone entry box declaration
    self.txt_phone = tk.Entry(self.master, text='')
    #paint phone entry box
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    #Email entry box declaration
    self.txt_email = tk.Entry(self.master, text='')
    #paint email entry
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

# define and paint the info box with scroll-bar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    # if the user selects an item from the list, it will call the function (event = select)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    #paint the scroll bar
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    #paint list
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

#define and paint the buttons (add, update, delete, close) using btn_ as the label
    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command=lambda: phonebook_func.addToList(self))
    #paint add button
    self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
    #define update button, paint update button
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command=lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
    #define and paint delete button (with call to func)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command=lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)
    # define and paint the Close button
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command=lambda: phonebook_func.askQuit(self))
    self.btn_close.grid(row=8, column=4, padx=(15,0), pady=(45,10), sticky=E)

    # create database function call from phonebook_func
    phonebook_func.create_db(self)
    # refresh the db to add information
    phonebook_func.onRefresh(self)










if __name__ == "__main__":
    pass
                        
                        




                        
    
