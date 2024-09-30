# Q1.Arvind just started learning python and he is very interested to know how he can print his name on the screen using python. Write a program to print Arvind on the screen. Print your name and age as well using a python print statement. 

#Printing Arvind's name
print("Arvind")

#Printing my name and age
print("Rahul Thakur, Age:27")

#Q2. Himanshi is confused with different shapes. Write a program in python to print different shapes using these symbols: “|”, “-”, “/”, “\”.

#Printing rectangle
print("Rectangle shape")
print("-------------")
print("|           |")
print("|           |")
print("-------------")

#Printing triangle
print("Triangle shape")
print("  /\  ")
print(" /  \ ")
print(" ----")

#Printing Parallelogram
print("Parallelogram shape")
print("    --------")
print("   /       /")
print("  /       /")
print(" /       /")
print("/       /")
print("--------")

#Printing Trapezoid
print("Trapezoid shape")
print("   ------  ")
print("  /      \\")
print(" /        \\")
print("/          \\")
print("------------")

#Printing Right-Angle Triangle
print("Right-Angle Triangle shape")
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/     |")
print("-------")

#Q3.Sahil challenged Chirag to print the names of his friend in different lines using a single print statement. Sahil thought that this would be impossible to do. To help Chirag write a python program to print the names of your five friends in five different lines using a single print statem

print("John Rao\nKurban Ali\nAmit Tripathi\nAnkit Kumar\nVishal Singh")

# Q4.A teacher told students to write an essay on themselves. Nidhi created a python program that can generate an essay just by taking inputs. She shared the program with her friends to help them. Write a python program that can take inputs like name, age, address, etc, and convert it into an essay. ● Rakshita wants to create a simple chatbot using python language. Write a program in python to help Rakshita in creating the chatbot. ● Hint: with the help of variables store the answers of the user and use it for further conversation by the chatbot. ● Example : ● >> ● Hi, I am a chatbot. What is your name? ● >>Nidhi ● Oh, Nidhi in which grade you are right now? ● >>8 ● Nidhi you are in 8th grade. Can I ask you one question? yes or no? ● >>yes ● Tell me 1024+98=? ● >>1122 ● Good! Your answer is correct. Bye ● >>bye

#Taking inputs from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
grade = int(input("Enter your grade: "))
address = input("Enter your address: ")
fav_sport = input("Enter your favourite sport: ")

essay = ("Hi, I am a chatbot. What is your name?\nMy name is " + name + ".\n"+"Oh, " + name + " what is your age?\n"+str(age) + ".\n"+"Ok " + name + ", " "in which grade are you at present?\n"+str(grade) + ".\n"+"Ok " + name + " you are in " + str(grade) + "th " + "grade. What is your address?\n"+address + ".\n"+"What is your favourite sport?\n"+fav_sport + ".\n"+"Nice! Thank you.")
print(essay)

#Q5.Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to calculate the total amount to charge from the customer. To help Himanshu create a program that asks the user to enter the number of books to buy and then print the amount to be paid. ● Hint: Assume the cost of one notebook - $2

cost_per_notebook_in_dollars = 2
num_notebooks = int(input("Enter the number of notebooks you want to buy: "))
total_cost = num_notebooks * cost_per_notebook_in_dollars
print("The total amount to be paid is: $" + str(total_cost))

# Q6.Shubh is excited to do something mathematical in python. He decided to create a program that could add, subtract, multiply and divide two numbers. To help Shubh write a python program to apply addition, subtraction, multiplication, and division between two numbers. ● Rakshita wants to calculate her age. So she subtracted her year of birth from the current year. Her classmates also wanted to find their age in the same way. So she decides to write a python program where students can input their year of birth, then the program will print their age. Write the same program to find your age and help your classmates in finding their age

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Adding two numbers
print("The addition of " + str(num1) + " and " + str(num2) + " is: ",num1 + num2 )
#Subtracting two numbers
print("The subtraction of " + str(num1) + " and " + str(num2) + " is: ",num1 - num2 )
#Multiplying two numbers
print("The multiplication of " + str(num1) + " and " + str(num2) + " is: ",num1 * num2 )
#Dividing two numbers
print("The division of " + str(num1) + " and " + str(num2) + " is: ",num1 / num2 )

#Calculating the age
current_year = 2024
year_of_birth = int(input("Enter the year of birth: "))
age = current_year - year_of_birth
print(age)

