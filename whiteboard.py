from tkinter import *
import tkinter as tk
import os

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+150")
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
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

# eraser button
eraser_path = os.path.join(current_dir, "eraser.png")
eraser = PhotoImage(file=eraser_path)
Button(root, image=eraser, bg="white", command=lambda: print("Eraser button clicked")).place(x=10, y=400)

# import button
import_path = os.path.join(current_dir, "import.png")
import_image = PhotoImage(file=import_path)
Button(root, image=import_image, bg="white", command=lambda: print("Import button clicked")).place(x=10, y=400)

# main screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

root.mainloop()
