import tkinter as tk

from libs import Libs

class Main:
    """"Main class for the app"""
    def __init__(self):
        self.myapp = App()
        self.myapp.master.title("Mad Libs game")
        self.myapp.master.minsize(600, 600)
        self.lib = Libs()
        self.run_app()
        
        self.cloese_app()

    def run_app(self):
        """Function which provides text ant the buttons for the application"""

        tk.Label(self.myapp, text="").grid(column=0, row=1)
        tk.Label(self.myapp, text="Mad Libs Game!", font = 'arial 20 bold').grid(column=1, row=2)
        tk.Label(self.myapp, text="").grid(column=0, row=3)
        tk.Button(self.myapp, text="First story", command=self.lib.first_lib).grid(column=1, row=4)
        tk.Label(self.myapp, text="").grid(column=0, row=5)
        tk.Button(self.myapp, text="Second story", command=self.lib.second_lib).grid(column=1, row=6)
        tk.Label(self.myapp, text="").grid(column=0, row=7)
        tk.Button(self.myapp, text="Third story", command=self.lib.third_lib).grid(column=1, row=8)


    def cloese_app(self):
        self.myapp.mainloop()



class App(tk.Frame):
    """Class for manipulating the screen size"""
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

if __name__ == '__main__':
    #Run Main instance.
    ai = Main()