#
#   python: 3.8.4
#   Author: Justin Perry
#   Create an app that allows a user to insert text into the
#   body tag of a simple webpage
#
#



# import modules
import tkinter as tk
from tkinter import *
import webbrowser as wb
import os.path
from os import path

class ParentWindow(Frame): # parent class
    # initialize the frame with the dunder, referencing the class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # set title of the GUI frame
        self.master.title('Update the body tag')
        # set size of the gui window
        self.master.geometry('500x130')

        # declare variable that will be from the entry box
        self.body_text = StringVar()

        # set labels for button
        self.lbl_update = tk.Label(self.master, text='Enter new body text here:')
        self.lbl_update.grid(row=0, column=0, padx=10)

        #create entry box for body text
        self.ent_body_text = tk.Entry(self.master, textvariable=self.body_text)
        self.ent_body_text.grid(row=1, column=0, columnspan=3, sticky='NSEW', padx=10)

        # buttons

        # update button
        self.btn_update = tk.Button(self.master, text='Update Body')
        self.btn_update.grid(row=2, column=0, padx=10, pady=20, sticky='w')
        self.btn_update.configure(command=self.update_file)

        #open file button
        self.btn_open_page = tk.Button(self.master, text='Open File')
        self.btn_open_page.grid(row=2, column=1, pady=20, padx=20, sticky='ew')
        self.btn_open_page.configure(command=self.open_file)

        #close application button/ with cancel command
        self.btn_close = tk.Button(self.master, text='Close')
        self.btn_close.grid(row=2, column=2, pady=20)
        self.btn_close.configure(command=self.cancel)

        
        

    def cancel(self):
        self.master.destroy()

    def open_file(self):
        if path.exists('sale_coming_soon.html'):
            open_in_wb = True
            while open_in_wb == True: 
                wb.open('sale_coming_soon.html')
                open_in_wb = False

    def update_file(self):
        insert_body = self.body_text.get()
        if path.exists('sale_coming_soon.html'):
            os.remove('sale_coming_soon.html')
        create = open('sale_coming_soon.html', 'x')
        write_file = open('sale_coming_soon.html', 'w')
        write_file.write("""<!DOCTYPE html>
                            <html>
                            <body>"""
                            + insert_body +
                            """</body> 
                            </html>""")
        create.close()
    
        

        

        









if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    # create a loop so the window can stay open while using
    # once loop is canceled, window will go away
    root.mainloop()
