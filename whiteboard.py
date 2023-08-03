from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title("White Board")
root.geometry("1200x650")
root.config(bg="#f2f3f5")
root.resizable(False, False)

# icon
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")
image_icon = PhotoImage(file=image_path)
root.iconphoto(False, image_icon)

# colors palette
colors = Canvas(root, bg="#fff", width=37, height=400, bd=0)
colors.grid(row=0, column=0, padx=10, pady=10)

def set_pen_color(event):
    color = colors.gettags(CURRENT)
    if color:
        global pen_color
        pen_color = color[0]

colors.create_rectangle(10, 10, 30, 30, fill="black", tags=("black", "palette"))
colors.create_rectangle(10, 40, 30, 60, fill="red", tags=("red", "palette"))
colors.create_rectangle(10, 70, 30, 90, fill="green", tags=("green", "palette"))
colors.create_rectangle(10, 100, 30, 120, fill="blue", tags=("blue", "palette"))
colors.create_rectangle(10, 130, 30, 150, fill="yellow", tags=("yellow", "palette"))
colors.create_rectangle(10, 160, 30, 180, fill="orange", tags=("orange", "palette"))
colors.create_rectangle(10, 190, 30, 210, fill="purple", tags=("purple", "palette"))
colors.create_rectangle(10, 220, 30, 240, fill="pink", tags=("pink", "palette"))
colors.create_rectangle(10, 250, 30, 270, fill="brown", tags=("brown", "palette"))
colors.create_rectangle(10, 280, 30, 300, fill="gray", tags=("gray", "palette"))
colors.create_rectangle(10, 310, 30, 330, fill="cyan", tags=("cyan", "palette"))
colors.create_rectangle(10, 340, 30, 360, fill="magenta", tags=("magenta", "palette"))
colors.create_rectangle(10, 370, 30, 390, fill="indigo", tags=("indigo", "palette"))
colors.create_rectangle(10, 430, 30, 450, fill="teal", tags=("teal", "palette"))

colors.tag_bind("palette", '<Button-1>', set_pen_color)

# eraser button
eraser_path = os.path.join(current_dir, "eraser.png")
eraser = PhotoImage(file=eraser_path)
Button(root, image=eraser, bg="white", command=lambda: canvas.delete("all")).grid(row=1, column=0, padx=10, pady=5)

# import button
def import_image_func():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global imported_image
        imported_image = Image.open(file_path)
        imported_image = imported_image.resize((500, 500))  # You can adjust the size of the pasted image here
        photo = ImageTk.PhotoImage(imported_image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.image = photo  # Keep a reference to the image to avoid garbage collection

import_path = os.path.join(current_dir, "import.png")
import_image = PhotoImage(file=import_path)
Button(root, image=import_image, bg="white", command=import_image_func).grid(row=2, column=0, padx=10, pady=5)

# main screen
canvas = Canvas(root, width=1100, height=600, background="white", cursor="pencil")
canvas.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

# Slider
current_value = tk.DoubleVar()
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.config(text=get_current_value())

slider = tk.Scale(root, from_=1, to=10, orient="horizontal", length=150, variable=current_value)
slider.grid(row=3, column=0, padx=10, pady=5)
value_label = Label(root, text=get_current_value(), bg="#f2f3f5")
value_label.grid(row=3, column=1, padx=10, pady=5)

# Drawing functionality
pen_color = "black"

def start_drawing(event):
    canvas.x = event.x
    canvas.y = event.y

def draw(event):
    x = event.x
    y = event.y
    canvas.create_line(canvas.x, canvas.y, x, y, width=current_value.get(), fill=pen_color)
    canvas.x = x
    canvas.y = y

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

root.mainloop()