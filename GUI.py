from tkinter import *                                                   # import all from tkinter


class WindowLogin:                                                      # build class window_Login

    def __init__(self, master):                                         # initialize
        frame = Frame(master)
        frame.pack()

        self.lblTechName = Label(frame, text="Tech Name")               # create label
        self.lblTechName.grid(row=0, sticky=E)                          # align label to 1st row on right side

        self.entName = Entry(frame)                                     # create text entry
        self.entName.grid(row=0, column=1, sticky=W)                    # align entry
        self.entName.bind("<Return>", self.techname)                    # set enter to run printName

        self.buttonSubmit = Button(frame, text="Login")                 # create button
        self.buttonSubmit.grid(columnspan=2)                            # align button
        self.buttonSubmit.bind("<Button-1>", self.techname)             # bind left click to run printName function

    def techname(self):                                                 # define function printName
        print("Test")                                                   # have function print ent_Name


login = Tk()
b = WindowLogin(login)
login.mainloop()