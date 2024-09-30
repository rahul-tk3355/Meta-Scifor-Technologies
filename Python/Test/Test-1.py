#Q1.The RTO (Regional Transport Office) website holds a registration form which is responsible for registering a user for a Driving License. The RTO wants to take the next step if and only if the user's age is greater than or equal to 18.
# Scenario 1 : When Traffic Light is Red
# Jake, a 20 year old teenager has learnt to ride a bike and is a bit confused with the traffic signals. He doesn't know what to do when the signal is red.
# So In this scenario Jake should just know what Jake should do when the signal is red whether he should leave or stop.
# So Write a If-Else condition to guide Jake
age = 20
if age >=18:
  print("Eligible for driving license registration.")
else:
  print("Not Eligible for driving license registration.")

#Scenario 1: Traffic Light Guide
traffic_light = "red"
if traffic_light == "red":
  print("Stop, Jake should not proceed.")
else:
  print("Proceed as per the traffic rules.")

#Q2.Sameer, a resident of India met John, a resident of california on facebook and they became friends, just in a conversation they planned to know each other's height and there was a problem, John would understand only if told in centimeter(cm) format. So write a program to help John to understand Sameer’s height in python to convert Feet & Inches To CM

feet = int(input("Enter the height in feet: "))
inches = int(input("Enter the height in inches: "))
total_inches = feet * 12 + inches
height_cm = total_inches*2.54
print(f"Sameer's height is {height_cm} cm.")

#Q3.Mary, a 15 year old girl, was watching her mom making a budget list every month, either her mom use to forget few things or she use to go out of budget due to no proper grocery list that says quantity of items, prices and stuff.
# So Mary wants to help her mom in managing the monthly groceries by creating an app that takes grocery item name, item price and quantity of item.
# Before all this, the app is suppose to accept the budget amount, if shopping list items price cross over the budget amount then any new items should not be added to the list.
# There should be 2 things in the menu of the app one to add an item and the second option to exit from the menu once the add item is chosen, then the item name, item quantity and item price should be accepted and the price should be checked with the budget amount. If the item amount is crossing the budget amount then the item cannot be added to the list.
# If the exit option is chosen then the total budget amount.


budget = float(input("Enter your budget amount: "))
total_expenses = 0.0
shopping_list = []
# display menu
print("\nMenu:")
print("1. Add item to shopping list")
print("2. Exit and show total budget")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    item_price = float(input("Enter item price per unit: "))

    total_item_cost = item_quantity * item_price

    if total_expenses + total_item_cost > budget:
        print(f"Cannot add {item_name} to the list. Exceeds budget.")
    else:
        shopping_list.append((item_name, item_quantity, item_price))
        total_expenses += total_item_cost
        print(f"{item_name} added to the list.")
elif choice == '2':
    print(f"Total Budget: ${budget:.2f}")
else:
    print("Invalid choice. Please enter 1 or 2.")






