import tkinter as tk
import random

students = ["Rahul", "John", "Charlie", "Thomas", "Varun", "Rohan", "Sachin", "Kurban Ali"]

def pick_random_name():
    if students:
        selected_name = random.choice(students)
        students.remove(selected_name)
        name_label.config(text=selected_name)
        completed_listbox.insert(tk.END, selected_name)
    else:
        name_label.config(text="No more names!")

root = tk.Tk()
root.title("Random Name Picker")
root.geometry("545x454")

name_frame = tk.Frame(root)
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="Click the button to pick a name", font=("Helvetica", 16))
name_label.pack()

pick_button = tk.Button(root, text="Pick a Name", command=pick_random_name, font=("Helvetica", 14))
pick_button.pack(pady=20)

completed_frame = tk.Frame(root)
completed_frame.pack(pady=10)

completed_label = tk.Label(completed_frame, text="Completed Names:", font=("Helvetica", 14))
completed_label.pack()

completed_listbox = tk.Listbox(completed_frame, width=30, height=10, font=("Helvetica", 12))
completed_listbox.pack()

root.mainloop()
