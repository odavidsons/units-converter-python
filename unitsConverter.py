"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

#UPDATE#
This application is a unit converter that features a user interface for easy usability. It includes multiple modes such as
length, weight, volume... 
"""
import tkinter as tk
from view.main import main

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Unit Converter")
        self.resizable(True,True)
        self.mainView = main(self)
        self.config(menu=self.mainView.menubar,bg="#f2f2f2")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
if __name__ == '__main__':
    app = App()
    app.mainloop()