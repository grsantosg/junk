# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:42:14 2020

@author: german.santos
"""
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")

etiqueta = tk.Label(window,text="Python Rocks!")
etiqueta.pack()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black" , # Set the background color to black
    width=10,
    height=10
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

#window.destroy()

window.mainloop()

