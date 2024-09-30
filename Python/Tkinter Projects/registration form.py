from tkinter import *
root = Tk()
root.geometry("900x700")
root.title("SCHOOL REGISTRATION FORM ")

name_var = StringVar()
class_var= StringVar()
age_var = StringVar()
gender_var = StringVar()
email_id_var = StringVar()
contact_no_var = StringVar()
country_var = StringVar()
category_var1 = StringVar()
category_var2 = StringVar()
category_var3 = StringVar()
category_var4 = StringVar()

def submit():
    print("Form submitted successfully!")
#Name
name = Label(root, text="Student's name : ", font="Helvetica 10 bold").grid(row=0,column=0,sticky=W,padx=10, pady=8)
name_entry = Entry(root, textvariable=name_var).grid(row=0, column=1)

#Age 
age = Label(root, text="Student's DOB : ", font="Helvetica 10 bold").grid(row=1,column=0,sticky=W,padx=10, pady=8)
age = Entry(root, textvariable=age_var).grid(row=1,column=1,padx=5,pady=8)

#class
class1 = Label(root, text="Class/Standard : ", font="Helvetica 10 bold").grid(row=2,column=0,sticky=W,padx=10, pady=8)
class1 = Entry(root, textvariable=class_var).grid(row=2,column=1,padx=5,pady=8)
#Father name
father_name = Label(root, text="Father's name : ", font="Helvetica 10 bold").grid(row=3,column=0,sticky=W,padx=10, pady=8)
father_name = Entry(root, textvariable=class_var).grid(row=3,column=1,padx=5,pady=8)

#Mother name
mother_name = Label(root, text="Mother's name : ", font="Helvetica 10 bold").grid(row=4,column=0,sticky=W,padx=10, pady=8)
mother_name = Entry(root, textvariable=class_var).grid(row=4,column=1,padx=5,pady=8)

#Gender
gender = Label(root, text="Gender : ", font="Helvetica 10 bold").grid(row=5,column=0,sticky=W,padx=10, pady=8)
gender1 = Radiobutton(root, text="Male", variable= gender_var, value="Male").grid(row=5,column=1, sticky=W)
gender2 = Radiobutton(root, text="Female", variable= gender_var, value="Female").grid(row=5,column=2, sticky=W)

#category
category = Label(root, text="Category : ", font="Helvetica 10 bold").grid(row=6,column=0,sticky=W,padx=10, pady=8)
category_choice1 = Checkbutton(root, text="UR", variable=category_var1, font="Helvetica 10 bold").grid(row=6,column=1,sticky=W,padx=5,pady=5)
category_choice2 = Checkbutton(root, text="OBC", variable=category_var2, font="Helvetica 10 bold").grid(row=7,column=1,sticky=W,padx=5,pady=5)
category_choice3 = Checkbutton(root, text="SC", variable=category_var3, font="Helvetica 10 bold").grid(row=8,column=1,sticky=W,padx=5,pady=5)
category_choice4 = Checkbutton(root, text="ST", variable=category_var4, font="Helvetica 10 bold").grid(row=9,column=1,sticky=W,padx=5,pady=5)

# Address
address  = Label(root, text="Correspondence Address : ", font="Helvetica 10 bold").grid(row=10,column=0, sticky=W,padx=10, pady=8)
address = Text(root, height=4, width=30).grid(row=10,column=1,padx=5,pady=8)

#Email Id
email_id = Label(root, text="Email Id : ", font="Helvetica 10 bold").grid(row=11, column=0,sticky=W,padx=10, pady=8)
email = Entry(root, textvariable=email_id_var).grid(row=11,column=1,padx=5,pady=8)

#Contact No
contact_no = Label(root, text="Contact No : ", font="Helvetica 10 bold").grid(row=12,column=0,sticky=W,padx=10, pady=8)
contact = Entry(root, textvariable=contact_no_var).grid(row=12,column=1,padx=5,pady=8)

#Country
country = Label(root, text="Nationality : ", font="Helvetica 10 bold").grid(row=13,column=0,sticky=W,padx=10, pady=8)
country = Entry(root, textvariable=country_var).grid(row=13,column=1,padx=5,pady=8)

#Submit
btn = Button(root, text="Submit", relief=SUNKEN, font="Helvetica 10 bold", command=submit).grid(row=16,column=1, pady=10)

root.mainloop()
