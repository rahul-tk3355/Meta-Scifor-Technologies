# Q1.create a program of finding total number of upper letters,lower letters ,digits and the symbols using for loop,strings and a if elif and else

str = "Hello-World! 123"
upper_count = 0
lower_count = 0
digit_count = 0
symbol_count = 0
for char in str:
  if char.isupper():
    upper_count += 1
  elif char.islower():
    lower_count+=1
  elif char.isdigit():
    digit_count+=1
  else:
    symbol_count +=1

print(f"total uppercase letters: {upper_count}")
print(f"total lowercase letters: {lower_count}")
print(f"total digits: {digit_count}")
print(f"total symbols: {symbol_count}")

# Q2.Manav wants to know all the possible dates of February 2024. To help Manav write a prgram that can
# take month and year as input and can print all the possible dates of that month in given format :
# dd/mm/yyyy
# ● Hint: Use loops to print all possible dates of the given month and year.
# ● Note: For february month check whether the given year is leap year or not.
# ● Sample run
# ● >>Enter month : 2
# ● >>Enter year : 2024
# ● >>Possible dates are :
# ● >>1/2/2024
# ● >>2/2/2024
# ● >>3/2/2024
# ● >>4/2/2024
# ● >>. # include all possible dates.
# ● >>.
# ● >>.
# ● >>28/2/2024
# ● >>29/2/2024
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
month_list1 = [1,3,5,7,8,10,12]
month_list2 = [4,6,9,11]
if month in month_list1:
  month_days = 31
elif month in month_list2:
  month_days = 30
elif month == 2:
  if(year%4==0 and year%100!=0) or (year%400==0):
    month_days = 29
  else:
    month_days = 28
else:
  print("Invalid month")
if month_days >0:
  print("Possible dates are: ")
  for day in range(1, month_days +1):
      print(f"{day}/{month}/{year}")

# Q3.Arvind came to know about the Fibonacci series.
# ● Note:
# ● The Fibonacci sequence is a series of numbers in which each number is the sum of the two that
# precede it. Starting at 0 and 1, the sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on
# forever. The Fibonacci sequence can be described using a mathematical equation: Xn+2= Xn+1 + Xn.
# ● Arvind is very interested to know the 100th term of the Fibonacci series. He was adding the values
# manually in a calculator but it was taking so much time for him to find any term of the Fibonacci series.
# To help Arvind write a program that can print nth term of the Fibonacci series where n is the given term
# by the user. Also, write the entire program inside a loop so that the user can use the program multiple
# times without running the program again and again.
while True:
  n = int(input("Enter term number: "))
  if n<1:
    print("Enter a positive integer. ")
    continue
  a,b = 0,1
  for _ in range(n-1):
    a,b = b, a+b
  print(f"The nth term is: {a}")
  repeat = input("Do you want for any other term?: " )
  if repeat!="yes":
      break
print("Program ended.")