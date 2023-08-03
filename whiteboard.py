from tkinter import *
import tkinter as tk
import os

root = Tk()
root.title("White Board")
root.geometry("1050x700+200+200")
root.config(bg="#f2f3f5")
root.resizable(False, False)

# icon
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")
image_icon = PhotoImage(file=image_path)
root.iconphoto(False, image_icon)

# sidebar
sidebar_path = os.path.join(current_dir, "sidebar.png")
color_box = PhotoImage(file=sidebar_path)
sidebar_label = Label(root, image=color_box, bg="#f2f3f5")
sidebar_label.grid(row=0, column=0, padx=10, pady=20)

# colors palette
colors = Canvas(sidebar_label, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def set_pen_color(event):
    color = colors.gettags(CURRENT)
    if color:
        global pen_color
        pen_color = color[0]

colors.create_rectangle(10, 10, 30, 30, fill="black", tags=("black", "palette"))
colors.create_rectangle(10, 40, 30, 60, fill="red", tags=("red", "palette"))
colors.create_rectangle(10, 70, 30, 90, fill="green", tags=("green", "palette"))
# Add more color rectangles as needed

colors.tag_bind("palette", '<Button-1>', set_pen_color)

# Slider
current_value = tk.DoubleVar()
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.config(text=get_current_value())

slider = tk.Scale(root, from_=1, to=10, orient="horizontal", length=200, variable=current_value)
slider.grid(row=4, column=0, padx=10, pady=5)
value_label = Label(root, text=get_current_value(), bg="#f2f3f5")
value_label.grid(row=4, column=1, padx=10, pady=5)

# eraser button
eraser_path = os.path.join(current_dir, "eraser.png")
eraser = PhotoImage(file=eraser_path)
Button(root, image=eraser, bg="white", command=lambda: canvas.delete("all")).grid(row=2, column=0, padx=10, pady=5)

# import button
import_path = os.path.join(current_dir, "import.png")
import_image = PhotoImage(file=import_path)
Button(root, image=import_image, bg="white", command=lambda: print("Import button clicked")).grid(row=3, column=0, padx=10, pady=5)

# main screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="pencil")
canvas.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

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
