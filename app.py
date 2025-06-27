import tkinter as tk
from tkinter import filedialog
import os

folder_a = ""
folder_b = ""

def choose_folder_a():
    global folder_a
    folder_a = filedialog.askdirectory()
    if folder_a:
        button_b.pack(pady=5)

def choose_folder_b():
    global folder_b
    folder_b = filedialog.askdirectory()
    if folder_b and folder_a:
        folder_names = [name for name in os.listdir(folder_a) if os.path.isdir(os.path.join(folder_a, name))]
        label.pack(pady=5)
        for name in folder_names:
            new_folder_path = os.path.join(folder_b, name)
            os.makedirs(new_folder_path, exist_ok=True)

        label.config(text=f"Done, copied {len(folder_names)} folders.")

root = tk.Tk()
root.geometry("250x110")
root.title("Copy Folders")

button_a = tk.Button(root, text="Choose Folder", command=choose_folder_a)
button_a.pack(pady=5)

button_b = tk.Button(root, text="Choose Destination", command=choose_folder_b)

label = tk.Label(root, text="")

root.mainloop()