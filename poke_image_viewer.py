"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500,500)
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))

# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticky= NSEW)

# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir,'poke_ball.png')
photo = PhotoImage(file=image_path)

lbl_image = ttk.Label(#fill in 1 and 2)
lbl_image.grid(#fill in a,b,c,d)

#Create button to set desktop background
def handle_set_desktop():
  ##finish this

def handle_poke_sel(event):
  ##Finish this

cbox_poke_sel.bind('<<ComboboxSelected>>', handle_poke_sel)

root.mainloop()