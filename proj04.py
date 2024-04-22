import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg,*png,*gif")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

root = tk.Tk()
root.title("Image Viewer")

button = tk.Button(root, text="Open Image" ,command=open_image)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
