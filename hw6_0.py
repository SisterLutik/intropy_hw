from itertools import cycle
import tkinter as tk


colors = cycle(['red', 'green', 'blue'])

def change_color():
    root['bg'] = next(colors)
    root.after(2000, change_color)


root = tk.Tk()
root.title("Test")
root.geometry("800x800+0+0")

change_color()

root.mainloop()