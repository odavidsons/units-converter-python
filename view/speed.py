"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Class for rendering the speed coversion frame
"""
import tkinter as tk
import dictionaries.speedDict

class speed(tk.Frame):

    fontLarge = ('default',14)
    fontMedium = ('default',12)

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        title = tk.Label(master,text="Speed Conversion",font=self.fontLarge)
        title.grid(row=0,columnspan=2,sticky="ew",padx=20,pady=10)
        self.fromUnit = tk.StringVar()
        values = dictionaries.speedDict.speed_values
        label1 = tk.Label(master,text="From:",font=self.fontMedium)
        label1.grid(row=1,column=0,pady=5)
        menu1 = tk.OptionMenu(master,self.fromUnit,*values)
        menu1.grid(row=1,column=1,pady=5,padx=5)
        self.textbox = tk.Entry(master)
        self.textbox.grid(row=2,columnspan=2)
        label2 = tk.Label(master,text="To:",font=self.fontMedium)
        label2.grid(row=3,column=0,pady=5)
        self.toUnit = tk.StringVar()
        menu2 = tk.OptionMenu(master,self.toUnit,*values)
        menu2.grid(row=3,column=1,pady=5,padx=5)
        convert = tk.Button(master,text="Convert",command=self.convert,font=self.fontMedium)
        convert.grid(row=4,column=0,pady=5,columnspan=2)
        label3 = tk.Label(master,text="Result:",font=self.fontMedium)
        label3.grid(row=5,column=0,padx=20,pady=5)
        self.result = tk.Label(master,text="")
        self.result.grid(row=5,column=1)

    def convert(self):
        from_unit = self.fromUnit.get()
        to_unit = self.toUnit.get()
        try:
            value = float(self.textbox.get())
        except: print("Enter a valid number")
        try:
            conversion = dictionaries.speedDict.speed_conversions[from_unit][to_unit]
            result = conversion*value
            self.result.config(text=result)
        except: print("Error in calculation")