from tkinter import * 
root = Tk() 
root.geometry("900x600") 
root.title("COVID VACCINE REGISTRATION FORM ") 
name_var = StringVar() 
age_var= StringVar() 
gender_var = StringVar() 
email_id_var = StringVar() 
contact_no_var = StringVar() 
country_var = StringVar() 
state_var = StringVar() 
disease_var1 = StringVar() 
disease_var2 = StringVar() 
disease_var3 = StringVar() 
disease_var4 = StringVar() 
def submit(): 
    print("Form submitted successfully!") 
#Name 
name = Label(root, text="Name of the visitor : ", font="Helvetica 10 bold").grid(row=0,column=0,sticky=W,padx=10, pady=8) 
name_entry = Entry(root, 
textvariable=name_var).grid(row=0, column=1) 
#Age  
age = Label(root, text="Age of the visitor : ", font="Helvetica 10 bold").grid(row=1,column=0,sticky=W,padx=10, pady=8) 
visitor_age = Entry(root, 
textvariable=age_var).grid(row=1,column=1,padx=5,pady=8) 
#Gender 
gender = Label(root, text="Gender : ", font="Helvetica 10 bold").grid(row=2,column=0,sticky=W,padx=10, pady=8) 
visitor_gender = Radiobutton(root, text="Male", variable= 
gender_var, value="Male").grid(row=2,column=1, sticky=W) 
visitor_gender = Radiobutton(root, text="Female", variable= 
gender_var, value="Female").grid(row=2,column=2, 
sticky=W) 
# Address 
address  = Label(root, text="Address : ", font="Helvetica 10 bold").grid(row=3,column=0, sticky=W,padx=10, pady=8) 
visitor_address = Text(root, height=4, 
width=30).grid(row=3,column=1,padx=5,pady=8) 
#Email Id 
email_id = Label(root, text="Email Id : ", font="Helvetica 10 bold").grid(row=4, column=0,sticky=W,padx=10, pady=8) 
visitor_email = Entry(root, 
textvariable=email_id_var).grid(row=4,column=1,padx=5,pady=8) 
#Contact No 
contact_no = Label(root, text="Contact No : ", font="Helvetica 10 bold").grid(row=5,column=0,sticky=W,padx=10, pady=8) 
visitor_contact = Entry(root, 
textvariable=contact_no_var).grid(row=5,column=1,padx=5,pady=8) 
#Country 
country = Label(root, text="Country : ", font="Helvetica 10 bold").grid(row=6,column=0,sticky=W,padx=10, pady=8) 
visitor_country = Entry(root, 
textvariable=country_var).grid(row=6,column=1,padx=5,pady
 =8) 
#State 
state = Label(root, text="State : ", font="Helvetica 10 bold").grid(row=7,column=0,sticky=W, pady=8,padx=10) 
visitor_state = Entry(root, textvariable=state_var).grid(row=7, 
column=1,padx=5,pady=8) 
#Select diseases 
choice = Label(root, text="If you are having any following disease : ", font="Helvetica 10 bold").grid(row=8,column=0,sticky=W, padx=8) 
visitor_choice1 = Checkbutton(root, text="Cold", 
variable=disease_var1, font="Helvetica 10 bold").grid(row=8,column=1,sticky=W,padx=5,pady=8) 
visitor_choice2 = Checkbutton(root, text="Cough", variable=disease_var2, font="Helvetica 10 bold").grid(row=9,column=1,sticky=W,padx=5,pady=8) 
visitor_choice3 = Checkbutton(root, text="Fever", variable=disease_var3, font="Helvetica 10 bold").grid(row=10,column=1,sticky=W,padx=5,pady=8) 
visitor_choice4 = Checkbutton(root, text="Headache", variable=disease_var4, font="Helvetica 10 bold").grid(row=11,column=1,sticky=W,padx=5,pady=8) 
#Submit button 
btn = Button(root, text="Submit", relief=SUNKEN, font="Helvetica 10 bold", command=submit).grid(row=12,column=1, pady=10) 
root.mainloop()