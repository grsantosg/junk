# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:42:14 2020

@author: german.santos
"""
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")

label=tk.Label(text="Name")
entry=tk.Entry(window)
label.pack()
entry.pack()

name=entry.get()
print(name)
text_box = tk.Text()
text_box.pack()

aux=text_box.get("1.0",tk.END)
text_box.insert("1.0", "Hello")
window.mainloop()
