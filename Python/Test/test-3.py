

# Create a Atm program using while loop major one
total_bal = 50000
correct_pin = 2156
atm_pin = int(input("enter the pin: "))
print("Welcome to the ATM")
if atm_pin != correct_pin:
  print("Incorrect pin. Please enter the correct pin")
else:
  while True:
    print("\nATM menu details")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")
    chosen_option = int(input("choose the option (1-4)"))
    if chosen_option == 1:
        print(f"Your total balance is: {total_bal}")
    elif chosen_option == 2:
        deposit_amount = int(input("Please enter the deposit amount: "))
        if deposit_amount == 0:
          print("enter amount greater than 0")
        else:
          total_bal += deposit_amount
          print(f"New balance: {total_bal}")
    elif chosen_option == 3:
          withdraw_amount = int(input("Please enter the withdrawal amount: "))
          if withdraw_amount == 0:
            print("enter amount greater than 0")
          elif withdraw_amount > total_bal:
            print("Insufficient balance")
          else:
            total_bal -= withdraw_amount
            print(f"withdrawal amount: {total_bal}")
    elif chosen_option == 4:
        print("Thank You for using the ATM")
        break
    else:
        print("Invalid choice. Please try again!")