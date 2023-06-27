"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Class for rendering the main interface for the app
"""
import tkinter as tk
from view.length import length
from view.mass import mass
from view.temperature import temperature
from view.power import power
from view.speed import speed
from view.area import area

class main():

    fontLarge = ('default',14)
    fontMedium = ('default',12)

    def __init__(self,master):
        self.menubar = tk.Menu(master)
        self.menubar.add_command(label="Exit",command=master.destroy)
        self.navFrame = tk.Frame(master)
        self.navFrame.grid(row=0,column=0,sticky="nsew",padx=5,pady=20)
        self.contentFrame = tk.Frame(master)
        self.contentFrame.grid(row=0,column=1,sticky="nsew",padx=5,pady=20)
        btnLength = tk.Button(self.navFrame,text="Length",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(length(self.contentFrame))])
        btnLength.grid(row=0,pady=5)
        btnMass = tk.Button(self.navFrame,text="Mass",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(mass(self.contentFrame))])
        btnMass.grid(row=1,pady=5)
        btnTemperature = tk.Button(self.navFrame,text="Temperature",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(temperature(self.contentFrame))])
        btnTemperature.grid(row=2,pady=5)
        btnPower = tk.Button(self.navFrame,text="Power",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(power(self.contentFrame))])
        btnPower.grid(row=3,pady=5)
        btnSpeed = tk.Button(self.navFrame,text="Speed",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(speed(self.contentFrame))])
        btnSpeed.grid(row=4,pady=5)
        btnArea = tk.Button(self.navFrame,text="Area",font=self.fontMedium,bg="#2e708c",command= lambda: [self.clearFrame(self.contentFrame),self.show_frame(area(self.contentFrame))])
        btnArea.grid(row=5,pady=5)
        labelWelcome = tk.Label(self.contentFrame,text="Welcome. Choose a category on the left menu to start converting!",font=self.fontLarge)
        labelWelcome.grid(sticky="nsew")
        self.make_dynamic(self.navFrame)
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