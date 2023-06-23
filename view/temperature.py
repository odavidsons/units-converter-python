"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Class for rendering the temperature coversion frame
"""
import tkinter as tk

class temperature(tk.Frame):

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        label = tk.Label(master,text="Temperature page")
        label.grid()