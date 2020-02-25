from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

import os

import tkinter as tk

from functools import partial

class Window(Frame):

    def callback(self, event, e):
        print('e.get():', e.get())
        # or more universal
        print('event.widget.get():', event.widget.get())

        # select text
        event.widget.select_range(0, 'end')
        # move cursor to the end
        event.widget.icursor('end')

    def commit(self):
        my_input = self.entry.get()
        if my_input[-4:] != ".png":
            my_input += ".png"
        print(self.files[0], "=>", my_input)
        os.rename(self.files.pop(0), my_input)
        current_path = os.path.dirname(os.path.abspath(__file__))
        load = Image.open(os.path.join(current_path, self.files[0]))
        render = ImageTk.PhotoImage(load)
        self.img.config(image = render)
        self.img.image = render
        self.entry.delete(0, 'end')
        self.entry.insert(0, self.files[0])
        self.entry.select_range(0, 'end')

    def __init__(self, master=None):
        frame = Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.files = os.listdir(current_path)
        print(self.files)
        load = Image.open(os.path.join(current_path, self.files[0]))
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.place(x=0, y=0)
        self.entry = tk.Entry(frame, width=30)
        self.entry.insert(0, self.files[0])
        self.entry.pack()
        self.entry.bind('<Control-KeyRelease-a>', partial(self.callback, e=self.entry))
        self.entry.select_range(0, 'end')
        buttonCommit = Button(root, height=1, width=10, text="Commit",
                              command=self.commit)
        buttonCommit.bind("<Return>", lambda x: self.commit())
        buttonCommit.pack()


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("500x300")
# root.bind("<Return", app.commit())
root.mainloop()
