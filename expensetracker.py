import json                                     #Imports Python Built-In JSON module to handle, read, and write JSON files.

def load_expenses():                            #Loads expenses from a JSON file into the program.
    try:                                        #Error Handling, if file doesn't exist, return an empty list.
        with open("expenses.json", "r") as f:   #Opens the expenses.json file and read("r") its content.
            return json.load(f)                 #After reading the whole JSON file, bring it to the program as a list.
    except FileNotFoundError:                   #In cases the file doesn't exist, it will catch the error 
        return []                               #And return an empty list on the program.
    
def save_expenses():                            #Saves the current expenses list in the program to a JSON file.
    with open("expenses.json", "w") as f:       #Opens the expenses.json file and write("w") the added expenses list to it. 
        json.dump(expenses, f)                  #Takes the expenses list from the program and writes it to the file in JSON.

expenses = load_expenses()                      #Instead of [], we will load previously saved expenses from the JSON file.
next_id = 1                                     #Initialize next_id to 1, which will be used to assign unique IDs to expenses. 

def show_menu():                                #Creates a function that shows the menu options the user can choose.

    print('Hello, Please select a number')      
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Remove Expenses')
    print('4. View Total Expenses')
    print('5. View Expenses by Category')
    print('6. Exit')

def add_expense():                              #Creates a function that allows the user to add an expense.            
    global next_id                              #When modifying, we declare it as global to ensure we change not create a new local variable.
   
    while True:                                 #Repeats asking the user for an amount until they provide a valid one.
        amount = input("Enter amount: ")        #Ask the user to ask the amount for their expense.
        if amount.replace('.', '', 1).isdigit():    #If we enter a decimal, it would still be valid because of the replace, and it temporarily removes the decimal from the number, and is.digit checks it as a valid number
            break                                   #Once input is valid, it breaks the loop and proceeds to ask for category and description.
        print("Invalid input, please enter a real amount.") 

    category = input("Enter category: ")        #Ask the user for the category of their expense. No Validation Loop because there are no wrong answer.
    description = input("Enter description: ")  #Ask the user for a description of their expense. No Validation Loop because there are no wrong answer.

    expense = {
        "id": next_id,                          #The ID is assigned from the next_id which starts at 1 to ensure unique identifier.
        "amount": float(amount),                #Float converts the amount from a string to a number with decimals for accurate math operations or procedures later.
        "category": category,                   #Category of the expense provided by the user.
        "description": description              #Description of the expense provided by the user.
    }   

    expenses.append(expense)                    #Append means adding the new "expense" to the end of the expenses list.
    next_id += 1                                #When the number of expenses increase, the id number assigned to them also increases.
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses to show.")
    else:
        for expense in expenses:
            print(f"ID: {expense['id']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

def remove_expense():
    if not expenses:
        print("No expenses to show.")
        return
    
    view_expenses()
    
    while True:
        choice = input("Which expense would you like to remove? (Enter ID): ")
        if choice.isdigit():
            break
        print("Invalid input, please enter a valid ID.")
    
    expense_id = int(choice)
    
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print("Expense removed successfully!")
            return
    
    print("Expense not found, please enter a valid existing ID")

def view_total_expenses():
    if not expenses:
        print("No expenses to show.")
        return
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total Expenses: ${(total):.2f}")

def view_expenses_by_category():
    if not expenses:
        print("No categories to show.")
        return
    
    categories = set()
    for expense in expenses:
        categories.add(expense['category'])
    print("Available categories:", ", ".join(categories))

    choice = input("Enter category: ")
    if choice not in categories:
        print("Invalid category, please enter a valid category.")
    else:
        print(f"Expenses in category '{choice}':")
        for expense in expenses:
            if expense["category"] == choice:
                print(f"ID: {expense['id']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
        
        total = 0
        for expense in expenses:
            if expense["category"] == choice:
                total += expense["amount"]
        print(f"Total for {choice}: ${total:.2f}")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        remove_expense()
    elif choice == "4":
        view_total_expenses()
    elif choice == "5":
        view_expenses_by_category()
    elif choice == "6":
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 6.")