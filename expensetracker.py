import json                                         #Imports Python Built-In JSON module to handle, read, and write JSON files.

def load_expenses():                                #Loads expenses from a JSON file into the program.
    try:                                            #Error Handling, if file doesn't exist, return an empty list.
        with open("expenses.json", "r") as f:       #Opens the expenses.json file and read("r") its content.
            return json.load(f)                     #After reading the whole JSON file, bring it to the program as a list.
    except FileNotFoundError:                       #In cases the file doesn't exist, it will catch the error 
        return []                                   #And return an empty list on the program.
    
def save_expenses():                                #Saves the current expenses list in the program to a JSON file.
    with open("expenses.json", "w") as f:           #Opens the expenses.json file and write("w") the added expenses list to it. 
        json.dump(expenses, f)                      #Takes the expenses list from the program and writes it to the file in JSON.

expenses = load_expenses()                          #Instead of [], we will load previously saved expenses from the JSON file.
next_id = 1                                         #Initialize next_id to 1, which will be used to assign unique IDs to expenses. 

def show_menu():                                    #Creates a function that shows the menu options the user can choose.

    print('Hello, Please select a number')      
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Remove Expenses')
    print('4. View Total Expenses')
    print('5. View Expenses by Category')
    print('6. Exit')

def add_expense():                                  #Creates a function that allows the user to add an expense.            
    global next_id                                  #When modifying, we declare it as global to ensure we change not create a new local variable.
   
    while True:                                     #Repeats asking the user for an amount until they provide a valid one.
        amount = input("Enter amount: ")            #Ask the user to ask the amount for their expense.
        if amount.replace('.', '', 1).isdigit():        #If we enter a decimal, it would still be valid because of the replace, and it temporarily removes the decimal from the number, and is.digit checks it as a valid number
            break                                       #Once input is valid, it breaks the loop and proceeds to ask for category and description.
        print("Invalid input, please enter a real amount.") 

    category = input("Enter category: ")            #Ask the user for the category of their expense. No Validation Loop because there are no wrong answer.
    description = input("Enter description: ")      #Ask the user for a description of their expense. No Validation Loop because there are no wrong answer.

    expense = {
        "id": next_id,                              #The ID is assigned from the next_id which starts at 1 to ensure unique identifier.
        "amount": float(amount),                    #Float converts the amount from a string to a number with decimals for accurate math operations or procedures later.
        "category": category,                       #Category of the expense provided by the user.
        "description": description                  #Description of the expense provided by the user.
    }   

    expenses.append(expense)                        #Append means adding the new "expense" to the end of the expenses list.
    next_id += 1                                    #When the number of expenses increase, the id number assigned to them also increases.
    print("Expense added successfully!")

def view_expenses():                                #Creates a function that allows the user to view all the expenses.
    if not expenses:                                #If there are no expense, it will print "No expenses to show."
        print("No expenses to show.")
    else:                                           #If there are expenses, display them all
        for expense in expenses:                    #Loop through each expense in the expenses list.
            print(f"ID: {expense['id']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}") #Display each expense's details, :.2f formats amount to 2 decimal places

def remove_expense():                               #Creates a function that allows the user to remove an expense by its ID.
    if not expenses:                                #If there are no expenses, it will print "No expenses to show."
        print("No expenses to show.")
        return                                      #Exits the function if there are no expenses to remove.

    view_expenses()                                 #So that the user could see all the list and their respective ID's.
    
    while True:                                     #Loop that keeps asking for an ID until a valid one is inputted.
        choice = input("Which expense would you like to remove? (Enter ID): ")
        if choice.isdigit():                        #Checks if the input is a valid number, which is necessary for an ID.
            break                                   #Exits the loop if the input is valid.
        print("Invalid input, please enter a valid ID.")
    
    expense_id = int(choice)                        #Converts the string "1" to a integer to compare it with the ID in the dictionary.
    
    for expense in expenses:                        #Loop through every expense in the expenses list.
        if expense["id"] == expense_id:             #If the ID of the current expense matches the ID inputted by the user.
            expenses.remove(expense)                #Remove the expense from the expenses list.
            print("Expense removed successfully!")
            return                                  #Exit the function.
    
    print("Expense not found, please enter a valid existing ID") #If there are no matching ID.

def view_total_expenses():                          #Creates a function that calculates and displays total expenses.
    if not expenses:                                #If there are no expenses, it will print "No expenses to show."
        print("No expenses to show.")
        return                                      #Exits the function if there are no expenses to calculate.
    total = 0                                       #Starting point for total
    for expense in expenses:                        #Loop through each expense in the expenses list.
        total += expense["amount"]                  #Add the amount of each expense to the total variable, which accumulates the total expenses.
    print(f"Total Expenses: ${(total):.2f}")        #:.2f adds 2 decimal places for the whole number.

def view_expenses_by_category():                    #It defines a function where the user can view expenses by their chosen category.
    if not expenses:                                #If there are no expenses, it will print "No expenses to show."
        print("No categories to show.")
        return                                      #Exits the function if there are no expenses to categorize.
    
    categories = set()                              #Creates an empty set to store unique category name which means no duplicates.
    for expense in expenses:                        #Loops through every expense in the expenses list.
        categories.add(expense['category'])         #Adds the category of each expense to the categories set, ensuring that only unique categories are stored.
    print("Available categories:", ", ".join(categories)) #Display all unique categories in one line separated by commas.

    choice = input("Enter category: ")              #Let's the user enter their chosen category as their choice.
    if choice not in categories:                    #If choice is not in the categories, it will print "Invalid category, please enter a valid category."
        print("Invalid category, please enter a valid category.")
    else:                                           #If the choice is valid, it will print all the expenses that belong to that category and calculate the total for that category.
        print(f"Expenses in category '{choice}':")
        for expense in expenses:                    #Loops through every expense in the expense list.
            if expense["category"] == choice:       #Shows the category that matches the choice of the user.
                print(f"ID: {expense['id']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
        
        total = 0                                   #Starting point for total of the category.
        for expense in expenses:                    #Loops through every expense in the expense list.
            if expense["category"] == choice:       #Only count expenses in the chosen category.
                total += expense["amount"]          #Add the amount of each expense in the chosen category to the total variable, which accumulates the total expenses for that category.
        print(f"Total for {choice}: ${total:.2f}")  #:.2f adds 2 decimal places for the whole number.

while True:                                         #Main loop that keeps the program running until the user chooses to exit. It displays the menu and processes user input.
    show_menu()                                     #Shows the menu options to the user by calling the show_menu function.
    choice = input("Choose: ")                      #Captures the user's menu selection as a string.

    if choice == "1":                               #If the user enters 1, call the add_expense function.
        add_expense()
    elif choice == "2":                             #If the user enters 2, call the view_expenses function.
        view_expenses()
    elif choice == "3":                             #If the user enters 3, call the remove_expense function.
        remove_expense()
    elif choice == "4":                             #If the user enters 4, call the view_total_expenses function.
        view_total_expenses()
    elif choice == "5":                             #If the user enters 5, call the view_expenses_by_category function.
        view_expenses_by_category()
    elif choice == "6":                             #If the user enters 6, call the save_expenses function to save the current expenses to the JSON file and then exit the program. 
        save_expenses() 
        print("Goodbye!")
        break                                       #Exits the loop. Ending the program.
    else:                                           #If the input doesn't match any valid option, notify the user.
        print("Invalid choice, please enter a number from 1 to 6.")