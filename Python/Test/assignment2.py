# Q1.Its childrens day and the class teacher wanted to share chocolates with the entire class the details are as follows,The number of chocolates with the teacher are = 327 Number of kids in the class are = 78. Write a program to perform modulus division using (%) modulus operator and find out how many chocolates are remaining with the teacher after equally distributing 327 chocolates to 78 students.

#calculating the remaining chocolates after distributing them equally among the students:
total_chocolates = 327
number_of_kids = 78
remaining_chocolates = total_chocolates %  number_of_kids
print(remaining_chocolates)

# Q2.It's Domino's 25th Anniversary and is planning for a big give away and in order to choose the lucky draw winner Domino's first needs to collect all of its customer details. On collecting the customer details Domino's even wants to thank each and every customer for visiting as soon as they entered their details.Write a program to accept customer details like customer name, customer mobile number, customer age, customer email Id.On successfully receiving all the customer information write a print() to thank the customer by using his name for example"Hi", customerName,"!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.""Once the lucky draw results are announced you will receive a message on your mobile number :",customerMobileNumber"An detailed description of your gift on your email Id :",customerEmailId"Thank you for being a valued customer",customerName,"!!""Dominos"

# Accepting customer details
cust_name = input("Enter your name: ")
cust_mobile_number = input("Enter your mobile number: ")
cust_age = input("Enter your age: ")
cust_email_id = input("Enter your email ID: ")

# Printing thank you message using the collected details
print(f"Hi, {cust_name}!!\nThanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary. Once the lucky draw results are announced you will receive a message on your mobile number: {cust_mobile_number}\nAn detailed description of your gift on your email Id : {cust_email_id}\nThank you for being a valued customer, {cust_name}!!\nDominos")

# Q3.Teacher wants to conduct a quiz activity in her class. For that she is planning to group 4 students for each team among 60 students. She wants to know how many teams she can create among 60 students.Write a program to find the total number of teams that can be created among students by dividing total number of students to the number of students per team.Total number of student = 60 Number of students per team =4

#Calculating the total number of teams that can be created among 60 students
total_students = 60
no_of_students_per_team = 4
total_teams = total_students / no_of_students_per_team
print(total_teams)

# Q4.Nidhi loves to travel to different countries. She is now in a country where the temperature is measured in Fahrenheit and she is not able to understand it in a better way. To help her in this situation, write program to convert temperature from Fahrenheit to celsius. ● Hint: (0°C × 9/5) + 32 = 32°F

#Convert temperature from Fahrenheit to celsius.
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
celsius_temperature = (fahrenheit_temperature - 32) * 5/9
print(celsius_temperature)


