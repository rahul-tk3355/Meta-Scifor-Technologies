from tkinter import *
root = Tk()
root.geometry("405x340")
root.title("Paint")
def draw():
    pass
v1 = DoubleVar()
pen = Label(root, text="pen", font="Arial 10 bold").grid(row=0,column=0,padx=10)
btn_pen = Button(root, text="p", command=draw, width=3).grid(row=0,column=1, padx=10)

brush = Label(root, text="brush", font="Arial 10 bold").grid(row=1,column=0,padx=10)
btn_brush = Button(root, text="b", command=draw, width=3).grid(row=1,column=1, padx=10)

color = Label(root, text="color", font="Arial 10 bold").grid(row=2,column=0,padx=10)
btn_color = Button(root, text="c", command=draw, width=3).grid(row=2,column=1, padx=10)

erasor = Label(root, text="erasor", font="Arial 10 bold").grid(row=3,column=0,padx=10)
btn_erasor = Button(root, text="e", command=draw, width=3).grid(row=3,column=1, padx=10)

s1 = Scale(root, variable=v1, from_=10, to= 1, orient= VERTICAL).grid(row=4, column=1, pady=30)
l1 = Label(root, text="Pen Size", font="Arial 10 bold").grid(row=5, column=1)

root.mainloop()
