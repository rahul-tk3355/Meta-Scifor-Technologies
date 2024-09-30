# #Q1.5 friends decided to go for a picnic and they start discussing the items which they have to take with
# them. They wanted to create a list where they can add items one by one. To help them, write a
# program in python to create an empty list. Then use for loop and append() method to add items one by
# one. ( Note: Range of loop depends on the number of items that have to be included in the list.) After
# adding all the items ask whether the user whether wants to remove any items or not and then print the
# whole list on the screen.
from os import remove
items_to_be_added = ["Picnic basket", "Picnic blanket", "Food and drinks", "Utensils", "First Aid"]
items_to_carry = []
for i in items_to_be_added:
  items_to_carry.append(i)
remove_items = input("Do you want to remove any item from list?(yes/no): ").lower()
if remove_items == 'yes':
  item_to_remove = input("enter the item you want to remove: ")
  if item_to_remove in items_to_carry:
    items_to_carry.remove(item_to_remove)
  else:
    print("Item not found. Please try again!")
print(items_to_carry)

# #Q2. A teacher created a list of names of the students. Now teachers want to get the name of all those
# students whose name starts with the letter “A”. To help the teacher write a python program and create
# a list of names of students. Then print the names which start with the letter “A”. (Hint: Use for loop and
# give condition I [0] == “A” )
names = ["Varun", "John", "Thomas", "Aakash", "Aditya", "Vikash"]
for i in names:
  if i[0]=="A":
    print(i)

# #Q3. In a class, the teacher decides to assign roll numbers to the students in alphabetical order of their
# names. The class consists of more than 60 students. So the class monitor decides to create a list in
# python to take the name of the students in any order and then will print the list in sorted order with roll
# numbers. ( Hint: use append() method to add the names in the list and then use sort() function on the
# list ) . After sorting the list, the Index number of the list can be used to assign the roll numbers to the
# students. ( Hint : roll no = index + 1 )
students = []
students.append("Rahul")
students.append("Sumit")
students.append("Varun")
students.append("Aditya")
students.append("John")
students.append("Navnit")
students.append("Carey")
students.append("Thomas")
students.append("Mike")
students.append("Bheeem")
print(sorted(students))
for index, name in enumerate(students):
  print(f'roll no = {index + 1}: {name}')

# #Q4.Nidhi is trying to solve a few questions in mathematics. She is actually finding out the central tendency(
# mean, median, and mode ) of some numbers. It is taking a lot of time for her to complete the
# questions. Help Nidhi in solving the following questions. Write the program for each of them.
# ● .
# ● She wants to find the mean of numbers. Write a program to find the mean of numbers.
# ● Hint: find the sum of all the numbers in the list then divide it with the number of elements present in the
# list.
# ● .
# ● Shen wants to find the median as well. Write a program to find the median of numbers in the given list.
# ● Hint: Sort the entire list the print the middle value of the list. If the list contains n numbers where n is
# even, then find the mean of the middle values.
# ● .
# ● Lastly, she wants to find the mode of numbers. To help Nidhi in this problem, write a program in python
# where users can enter n numbers as input, and then the program will print the mode of numbers.
# ● Hint: Print the number having maximum count in the list.
#mean calculation
numbers = [1,2,3,4,5]
sum = 0
for i in numbers:
  sum+=i
print('The mean of numbers is: ', (sum/i))

# median calculation
n = len(numbers)
middle = n//2
if n%2==0:
  median=(numbers[middle-1]+numbers[middle]/2)
else:
  median = numbers[middle]
print(f"the median is: {median}")

#mode
from statistics import mode
nums = [1,2,3,4,2,1,4,2]
result = mode(nums)
print(f"the mode is: {result}")

# #Q5. In a school, a football competition is going to be held. The sports captain needs to create a list of the
# players with their heights. According to the rule, only those students can participate in the competition
# who have a height greater than 167cm. To make things easier write a python program. Create a list of
# tuples with the name of the player and their height in cm. Note: while taking the input from the users,
# don’t include the players whose height is less than 167cm. ( Use continue statement )
# ● Sample list: [ (“Chris” , 170) , (“Aditya” , 182) , (“Chirag” , 176 ) ]

players = []
total_players = int(input("Enter the number of players: "))
for _ in range(total_players):
  name = input("Enter the player's name: ")
  height = int(input("Enter the player's height in cm: "))
  if height > 167:
    players.append((name, height))
  else:
    continue

print("Eligible players for the competition:", players)

