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
Label(root, image=color_box, bg="#f2f3f5").grid(row=0, column=0, padx=10, pady=20)

# colors palette
colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.grid(row=1, column=0, padx=10, pady=5)

def show_color(color):
    print("Selected color:", color)

def display_palette():
    colors.create_rectangle(10, 10, 30, 30, fill="black")
    colors.create_rectangle(10, 40, 30, 60, fill="red")
    colors.create_rectangle(10, 70, 30, 90, fill="green")
    # Add more color rectangles as needed
    colors.tag_bind("palette", '<Button-1>', lambda x: show_color(colors.gettags(CURRENT)))

display_palette()

# eraser button
eraser_path = os.path.join(current_dir, "eraser.png")
eraser = PhotoImage(file=eraser_path)
Button(root, image=eraser, bg="white", command=lambda: print("Eraser button clicked")).grid(row=2, column=0, padx=10, pady=5)

# import button
import_path = os.path.join(current_dir, "import.png")
import_image = PhotoImage(file=import_path)
Button(root, image=import_image, bg="white", command=lambda: print("Import button clicked")).grid(row=3, column=0, padx=10, pady=5)

# main screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

root.mainloop()
