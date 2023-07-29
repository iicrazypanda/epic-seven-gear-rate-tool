from tkinter import *

root = Tk()
root.title("Epic Seven Gear Rate Tool")
root.config(bg="#333333")

left_frame = Frame(root, bg="#444444", width=200, height=600)
left_frame.grid(row=0, column=0, padx=10, pady=10)

middle_frame = Frame(root, bg="#444444", width=200, height=600)
middle_frame.grid(row=0, column=1, padx=10, pady=10)

right_frame = Frame(root, bg="#444444", width=200, height=600)
right_frame.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()