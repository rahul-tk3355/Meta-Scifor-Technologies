
#Q1 calculate the no of desks in a classroom if the desks are arranged in rows and columns.
no_of_rows = int(input("enter the number of rows: "))
no_of_cols = int(input("enter the number of columns: "))
no_of_desks = no_of_rows*no_of_cols
print(no_of_desks)

#Q2. Check whether a number is a prime or not.
number = int(input("enter the number: "))
if number%2==0:
  print("not prime")
else:
  print("prime")

#Q3. print all the even and odd numbers from 11 to 20.
for i in range(11, 21):
  if i%2==0:
    print(f"even number:{i}")
  else:
    print(f"odd number: {i}")

#Q4. Add names of your friends to a dictionary and also print the all the keys.
dict = {}
dict.update({10 : "Arjun"})
dict.update({11 : "Rajesh"})
dict.update({12 :"Rajesh"})
dict.update({13: "sathish"})
empid = dict.keys()
for empid in dict:
  print(f'message sent to: {empid} ')

dict.update({14: "John"})
dict.update({15: "Thomas"})
print(dict)

#Q5.
no_of_guests = 0
codes_list = ['0', '1', '2', '3']
for auth_code in codes_list:
  if auth_code =="0":
    print("Access Granted")
    print("Door opened")
  elif auth_code == "1":
    no_of_guests+=1
    print("Door opened")
    print("Welcome to the party, we hope you have fun.")
  else:
    print("Invalid Authorization code.")
print(f"total number of guests: {no_of_guests}")