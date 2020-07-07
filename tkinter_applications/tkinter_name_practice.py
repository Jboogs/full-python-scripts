# Tkinter practice and overview
import tkinter
# from tkinter, import ALL widgets
from tkinter import *
# this is the parent window, use this to create the window and its
# characteritics
class Parent_window(Frame):
    def __init__ (self, master):
        Frame.__init__(self)
        # the master arg is now saved as self.master 
        self.master = master
        # this states the window that will be opened cannot be resized
        # and stays at the same size
        self.master.resizable(width=False, height=False)
        # this is the exact size of the window, using string format {Wpx}x{Hpx}
        self.master.geometry('{}x{}'.format(700, 400))
        # title for the master frame
        self.master.title('Learning Tkinter')
        # configure the color/graphics of the window, bg is background
        # color is string, passed in similar to CSS
        self.master.configure(bg='darkgray')

        # create variables and call them later to create text boxes
        # you can effect the text that is in the text box with the
        # variables (StringVar())
        self.varfName = StringVar()
        self.varlName = StringVar()
        self.varAge = IntVar()

        #labels for the text boxes for UX, easier to know where to put info in
        self.lblfName = Label(self.master, text='First Name: ', font=('Helvetica', 16), fg='black', bg='darkgray')
        #paint, with some padding using padx and pady
        self.lblfName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))
        # instanciate the label
        self.lbllName = Label(self.master, text='Last Name: ', font=('Helvetica', 16), fg='black', bg='darkgray')
        # paint the label
        self.lbllName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))
        # instantiate the label
        self.lblAge = Label(self.master, text='Age: ', font=('Helvetica', 16), fg='black', bg='darkgray')
        # paint the label
        self.lblAge.grid(row=2, column=0, padx=(30, 0), pady=(30, 0))
        #output display label, where the information will go once submitted
        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='darkgray')
        #paint the display box, this will be below the buttons to display
        self.lblDisplay.grid(row=4, column=1, padx=(30, 0), pady=(30, 0))
        

        # this is where you paint (create) the text box for inputs/reads
        # on the screen with the entry widget from tkinter
        # modify, where it needs to go, attach it to the master (app box)
        
        # entry method args entry(master window, input path variable, font tuple(font name, size)
        # these are instantiations that can be referenced for later
        self.txtfName = Entry(self.master, text=self.varfName, font=('Helvetic', 16), fg='black', bg='red')
        # paint into the grid
        self.txtfName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))
        # instanciate
        self.txtlName = Entry(self.master, text=self.varlName, font=('Helvetic', 16), fg='black', bg='red')
        # paint into the grid
        self.txtlName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))
        # instanciate
        self.txtAge = Entry(self.master, text=self.varAge, font=('Helvetic', 16), fg='black', bg='red')
        # paint into the grid
        self.txtAge.grid(row=2, column=1, padx=(30, 0), pady=(30, 0))

        # buttons on the form code
        #submit button, command=self.submit(this is calling the function for when you hit submit) this is calling hte function, not defining
        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        #Paint the button
        self.btnSubmit.grid(row=3, column=1, padx=(0, 0), pady=(30,0), sticky=NE)

            #close button with the command calling the cancel function.  This is calling, not defining
        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        #paint the button
        self.btnCancel.grid(row=3, column=1, padx=(0, 30), pady=(30, 0), sticky=NW)

    #define the methods for the buttons, same indentation as the __init__ above
    def submit(self):
        #store the innitial first name StringVar() created above in this variable here, using the get method
        fname = self.varfName.get()
        lname = self.varlName.get()
        age = self.varAge.get()
        self.lblDisplay.config(text='Hello {} {}! You are {} years old'.format(fname, lname, age))
    # this closes the window using the destroy() method/tk widget
    def cancel(self):
        self.master.destroy()
        
        




#program flow
if __name__ == '__main__':
    # instantiate tkinter and saving it in the variable root
    root = Tk() # frame is tkinters main class, names it root
    App = Parent_window(root) # attached it to the parent window
    # this line keeps the window alive, mainloop()
    root.mainloop() # keeps the window open until closed

