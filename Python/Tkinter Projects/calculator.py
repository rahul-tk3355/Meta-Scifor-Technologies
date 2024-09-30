from tkinter import *
import math
root = Tk()
root.geometry("405x440")
root.title("Calculator")
#root.wm_iconbitmap("cal.ico")

def click(event):
    global screen_var
    text = event.widget.cget('text')
    if text == "=":
        if screen_var.get().isdigit():
            value = int(screen_var.get())
        else:
            value = eval(screen_var.get())
            screen_var.set(value)
            screen.update()

    elif text == "AC":
        screen_var.set("")
        screen.update()

    elif text == "sin":
        value = math.sin(math.radians(eval(screen_var.get())))
        screen_var.set(value)
    elif text == "cos":
        value = math.cos(math.radians(eval(screen_var.get())))
        screen_var.set(value)
    elif text == "tan":
        value = math.tan(math.radians(eval(screen_var.get())))
        screen_var.set(value)
    elif text == "log":
        value = math.log(eval(screen_var.get()))
        screen_var.set(value)
    elif text == "x2":
        value = eval(screen_var.get())**2
        screen_var.set(value)
    elif text == "x3":
        value = eval(screen_var.get())**3
        screen_var.set(value)
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

screen_var = StringVar()
screen_var.set("")

screen = Entry(root, textvariable=screen_var,font="Arial 14 bold",border=10,relief=SUNKEN).pack(pady=30, ipady=10, fill=X, ipadx=50)

# buttons

f = Frame(root, bg="green")
btn1 = Button(f, text="AC", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW, pady=10)
btn1.bind("<Button-1>", click)
btn2 = Button(f, text="+", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW, pady=10)
btn2.bind("<Button-1>", click)
btn3 = Button(f, text="-", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="*", font="Arial 12 bold", width=8,bg="red")
btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
btn1 = Button(f, text="cos", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn1.bind("<Button-1>", click)
btn2 = Button(f, text="sin", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn2.bind("<Button-1>", click)
btn3 = Button(f, text="tan", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="log", font="Arial 12 bold", width=8,bg="red")

btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
btn1 = Button(f, text="7", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn1.bind("<Button-1>", click)
btn2 = Button(f, text="8", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn2.bind("<Button-1>", click)
btn3 = Button(f, text="9", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="/", font="Arial 12 bold", width=8,bg="red")
btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
btn1 = Button(f, text="4", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn1.bind("<Button-1>", click)
btn2 = Button(f, text="5", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn2.bind("<Button-1>", click)

btn3 = Button(f, text="6", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="x2", font="Arial 12 bold", width=8,bg="red")
btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
btn1 = Button(f, text="1", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn1.bind("<Button-1>", click)
btn2 = Button(f, text="2", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn2.bind("<Button-1>", click)
btn3 = Button(f, text="3", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="x3", font="Arial 12 bold", width=8,bg="red")
btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="green")
btn1 = Button(f, text="%", font="Arial 12 bold",width=8,bg="red")
btn1.pack(side=LEFT,padx=7,anchor=NW,pady=10)

btn1.bind("<Button-1>", click)
btn2 = Button(f, text="0", font="Arial 12 bold", width=8,bg="red")
btn2.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn2.bind("<Button-1>", click)
btn3 = Button(f, text=".", font="Arial 12 bold", width=8,bg="red")
btn3.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn3.bind("<Button-1>", click)
btn4 = Button(f, text="=", font="Arial 12 bold", width=8,bg="red")
btn4.pack(side=LEFT,padx=7,anchor=NW,pady=10)
btn4.bind("<Button-1>", click)
f.pack()

root.mainloop()