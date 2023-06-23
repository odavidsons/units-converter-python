"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Class for rendering the length conversion frame
"""
import tkinter as tk
import dictionaries.lengthDict

class length(tk.Frame):

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        title = tk.Label(master,text="Length Conversion")
        title.grid(row=0,columnspan=2,sticky="ew")
        self.fromUnit = tk.StringVar()
        values = dictionaries.lengthDict.length_values
        label1 = tk.Label(master,text="From:")
        label1.grid(row=1,column=0)
        menu1 = tk.OptionMenu(master,self.fromUnit,*values)
        menu1.grid(row=1,column=1)
        self.textbox = tk.Entry(master)
        self.textbox.grid(row=2,columnspan=2)
        label2 = tk.Label(master,text="To:")
        label2.grid(row=3,column=0)
        self.toUnit = tk.StringVar()
        menu2 = tk.OptionMenu(master,self.toUnit,*values)
        menu2.grid(row=3,column=1)
        convert = tk.Button(master,text="Convert",command=self.convert)
        convert.grid(row=4,column=0)
        label3 = tk.Label(master,text="Result:")
        label3.grid(row=5,column=0)
        self.result = tk.Label(master,text="")
        self.result.grid(row=5,column=1)

    def convert(self):
        from_unit = self.fromUnit.get()
        to_unit = self.toUnit.get()
        try:
            value = float(self.textbox.get())
        except: print("Enter a valid number")
        try:
            conversion = dictionaries.lengthDict.length_conversions[from_unit][to_unit]
            self.result.config(text=(conversion * value))
        except: print("Error in calculation")