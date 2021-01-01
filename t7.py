# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:28:21 2020

@author: german.santos
"""
import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()