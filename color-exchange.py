import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Color GUI")
root.geometry("600x500")


def red_color():
    frame.config(bg="red")


def green_color():
    frame.config(bg="green")


def blue_color():
    frame.config(bg="blue")


def yellow_color():
    frame.config(bg="yellow")


def purple_color():
    frame.config(bg="purple")


def change_color():
    frame.config(bg=combo.get().lower())


frame = tk.Frame(root, bg="white", width=500, height=400)
frame.pack(pady=30)
frame.pack_propagate(False)



color = tk.StringVar()
color.set("Red")

radio1 = tk.Radiobutton(frame, text="Red", variable=color, value="Red")
radio1.place(x=80, y=40)

radio2 = tk.Radiobutton(frame, text="Green", variable=color, value="Green")
radio2.place(x=80, y=80)

radio3 = tk.Radiobutton(frame, text="Blue", variable=color, value="Blue")
radio3.place(x=80, y=120)

radio4 = tk.Radiobutton(frame, text="Yellow", variable=color, value="Yellow")
radio4.place(x=80, y=160)

radio5 = tk.Radiobutton(frame, text="Purple", variable=color, value="Purple")
radio5.place(x=80, y=200)


# Buttons
btn1 = tk.Button(frame, text="Red", command=red_color)
btn1.place(x=300, y=35)

btn2 = tk.Button(frame, text="Green", command=green_color)
btn2.place(x=300, y=75)

btn3 = tk.Button(frame, text="Blue", command=blue_color)
btn3.place(x=300, y=115)

btn4 = tk.Button(frame, text="Yellow", command=yellow_color)
btn4.place(x=300, y=155)

btn5 = tk.Button(frame, text="Purple", command=purple_color)
btn5.place(x=300, y=195)


# ComboBox
combo = ttk.Combobox(frame)
combo["values"] = ("Red", "Green", "Blue", "Yellow", "Purple")
combo.set("Select Color")
combo.place(x=180, y=260)


# ComboBox Button
combo_btn = tk.Button(frame, text="Change Color", command=change_color)
combo_btn.place(x=220, y=300)


root.mainloop()
