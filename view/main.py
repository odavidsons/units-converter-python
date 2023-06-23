"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Class for rendering the main interface for the app
"""
import tkinter as tk
from view.length import length
from view.mass import mass


class main():

    fontLarge = ('default',14)
    fontMedium = ('default',12)

    def __init__(self,master):
        self.menubar = tk.Menu(master)
        self.menubar.add_command(label="Exit",command=master.destroy)
        self.navTextFrame = tk.Text(master)
        self.navTextFrame.grid(row=0,column=0,padx=5,pady=20)
        self.navFrame = tk.Frame(self.navTextFrame)
        self.navFrame.grid(row=0,column=0,sticky="nsew")
        self.contentFrame = tk.Frame(master)
        self.contentFrame.grid(row=0,column=1,sticky="nsew",padx=5,pady=20)
        nav_scrollbar_y = tk.Scrollbar(self.navTextFrame,orient="vertical")
        nav_scrollbar_y.grid(row=0,column=1,sticky="ns")
        self.navTextFrame.config(yscrollcommand=nav_scrollbar_y.set)
        btnLength = tk.Button(self.navFrame,text="Length",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(length(self.contentFrame))])
        btnLength.grid(row=0,pady=5)
        btnMass = tk.Button(self.navFrame,text="Mass",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(mass(self.contentFrame))])
        btnMass.grid(row=1,pady=5)
        btnTemperature = tk.Button(self.navFrame,text="Temperature",font=self.fontMedium)
        btnTemperature.grid(row=2,pady=5)
        btnPower = tk.Button(self.navFrame,text="Power",font=self.fontMedium)
        btnPower.grid(row=3,pady=5)
        btnCategory = tk.Button(self.navFrame,text="Category",font=self.fontMedium)
        btnCategory.grid(row=4,pady=5)
        btnCategory = tk.Button(self.navFrame,text="Category",font=self.fontMedium)
        btnCategory.grid(row=5,padx=10,pady=5)
        btnCategory = tk.Button(self.navFrame,text="Category",font=self.fontMedium)
        btnCategory.grid(row=6,padx=10,pady=5)
        btnCategory = tk.Button(self.navFrame,text="Category",font=self.fontMedium)
        btnCategory.grid(row=7,padx=10,pady=5)
        btnCategory = tk.Button(self.navFrame,text="Category",font=self.fontMedium)
        btnCategory.grid(row=8,padx=10,pady=5)
        labelWelcome = tk.Label(self.contentFrame,text="Welcome. Choose a category on the left menu to start converting!",font=self.fontLarge)
        labelWelcome.grid(sticky="nsew")
        self.make_dynamic(self.navTextFrame)
        self.make_dynamic(self.contentFrame)
        
    #Make a window's widgets dynamic when resizing
    def make_dynamic(self,window):
        col_count,row_count = window.grid_size()
        
        for i in range(row_count):
            window.grid_rowconfigure(i, weight=1)

        for i in range(col_count):
            window.grid_columnconfigure(i, weight=1)

        for child in window.children.values():
            try:
                child.grid_configure(sticky="nsew")
                self.make_dynamic(child)
            except: pass

    #Show a frame
    def show_frame(self,frame):
        frame.tkraise()
        self.make_dynamic(frame)

    #Clear a frame out of all it's widgets
    def clearFrame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()