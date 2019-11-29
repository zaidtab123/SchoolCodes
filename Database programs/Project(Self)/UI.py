import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from PIL import Image, ImageTk

'''root = Tk()
root.geometry("600x600")
root.configure(background='black')
root.title("Ticket Booking Agent")'''


class TickEasy(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("600x600")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HomeScreen, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        email = StringVar()
        password = StringVar
        '''Tk.configure(background='black')
        Tk.title("Ticket Booking Agent")'''
        label1 = Label(self, text="Welcome to TickEasy", fg='white', bg='black',
                       font=("Ronduit Capitals Light", 20, 'bold'))
        label1.pack()

        login_icon_location = "C:/Users/Zaid/PycharmProjects/SchoolCodes/Database programs/Project(Self)/Icon/login_image.png"
        login_icon = ImageTk.PhotoImage(Image.open(login_icon_location))
        login_icon_dp = Label(self, image=login_icon, bg='black')
        login_icon_dp.pack()

        email_txt = Label(self, text="E-Mail:", fg='white', bg='black', font=("Ronduit Capitals Light", 14))
        email_txt.place(x=30, y=190)
        email_entry = Entry(self, textvar=email, width=50)
        email_entry.place(x=200, y=195)

        passw_txt = Label(self, text="Password:", fg='white', bg='black', font=("Ronduit Capitals Light", 14))
        passw_txt.place(x=30, y=230)
        passw = Entry(self, textvar=password, width=50)
        passw.place(x=200, y=235)
        submit_bt = Button(self, text='Submit', fg='white', width=9, bg='black', relief='raised',
                           font=("Ronduit Capitals Light", 12), command=lambda:controller.show_frame("HomeScreen"))
        submit_bt.place(x=90, y=300)

        exit_bt = Button(self, text='Exit', fg='white', width=9, bg='black', relief='raised',
                         font=("Ronduit Capitals Light", 12), command=exit)
        exit_bt.place(x=300, y=300)


class HomeScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = TickEasy()
    app.mainloop()




