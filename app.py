import tkinter as tk
import os
from tkinter import filedialog, Text

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp_apps = f.read().split(',')
        apps = [x for x in temp_apps if x.strip()]
        
def add_app():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File",
                                      filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    if filename in apps:
        return

    for widget in frame.winfo_children():
        widget.destroy()

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg = "gray")
        label.pack()

def run_app():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

open_file = tk.Button(root, text='Open File', padx = 10,
                      pady = 5, fg = "white", bg = "#263D42",
                      command = add_app)
open_file.pack()

run_apps = tk.Button(root, text='Run Apps', padx = 10,
                      pady = 5, fg = "white", bg = "#263D42",
                      command = run_app)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')