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
image_path = os.path.join(images_dir,'dugtrio.png')
photo = PhotoImage(file=image_path)

lbl_image = ttk.Label(frm, image=photo)
lbl_image.grid(row=0, padx=(10,20), pady=(10,20), sticky=NS)

poke_list = poke_api.get_pokemon_names
cbox_poke = ttk.Combobox(frm, values=poke_list, state='readonly')
cbox_poke.set("Select a Pokemon")
cbox_poke.grid(row=1, padx=10, pady=10)

def handle_poke_sel(event):
    global photo
    pokemon_name = cbox_poke.get()
    image_path = poke_api.download_pokemon_artwork(pokemon_name, images_dir)
    if image_path:
        photo = PhotoImage(file=image_path)
        lbl_image.config(image=photo, text="")
    else:
        lbl_image.config(text="Failed to load image.", image="")

cbox_poke.bind('<<ComboboxSelected>>', handle_poke_sel)

'''def handle_set_desktop():# needs to be fix.
  button_set = ttk.Button(text="Set Desktop Image", state="disabled")
  button_set.grid(row=2, padx=10, pady=10)'''
def handle_set_desktop():
    global photo
    if photo:
        image_path = os.path.join(images_dir, f"{cbox_poke.get()}.png")
        image_lib.set_desktop_background(image_path)

btn_set_desktop = ttk.Button(frm, text="Set as Desktop Background", command=handle_set_desktop)
btn_set_desktop.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky=NS)
'''def handle_os_sel(event):
  selected_pokemon = cbox_poke.get()
  photo['file'] = os.path.join(images_dir, f'{selected_pokemon}.png')
  lbl_image['image'] = photo
  button_set['state'] = "enabled"

cbox_poke.bind('<<ComboboxSelected>>', handle_os_sel)'''


root.mainloop()