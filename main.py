from tkinter import *

root = Tk()
root.title("Epic Seven Gear Rate Tool")
root.config(bg="#333333")

left_panel = Frame(root, bg="#444444")
left_panel.grid(row=0, column=0, padx=10, pady=10)

middle_panel = Frame(root, bg="#444444")
middle_panel.grid(row=0, column=1, padx=10, pady=10)

right_panel = Frame(root, bg="#444444")
right_panel.grid(row=0, column=2, padx=10, pady=10)


stat_label = Label(left_panel, bg="#444444", fg="White", text="Choose stats")
stat_label.pack()
stat_listbox = Listbox(left_panel, selectmode=MULTIPLE, bg="#444444", fg="White", width=30)
list = ["Attack flat", "Attack percentage", "Defense flat", "Defense percentage",
        "Health flat", "Health percentage", "Speed", "Critical hit chance", "Critical hit damage",
        "Effectiveness", "Effect Resistance"]
for i in range(11):
    stat_listbox.insert(i, list[i])
stat_listbox.pack()

label1 = Label(middle_panel, text="label1", bg="#444444", fg="White", width=30)
label1.pack()
label2 = Label(middle_panel, text="label2", bg="#444444", fg="White")
label2.pack()
label3 = Label(middle_panel, text="label3", bg="#444444", fg="White")
label3.pack()
label4 = Label(middle_panel, text="label4", bg="#444444", fg="White")
label4.pack()

root.mainloop()