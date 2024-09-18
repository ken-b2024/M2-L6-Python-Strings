#Task 1
first_name = input("Please type your first name: ")
last_name = input("Please type your last name: ")

if len(first_name) < 2:
    print("First name cannot be under two characters. Please try again...")
if len(last_name) < 2:
    print("Last name cannot be under two characters. Please try again...")