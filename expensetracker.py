import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_expenses(): 
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

expenses = load_expenses()
next_id = 1

def show_menu():

    print('Hello, Please select a number')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Remove Expenses')
    print('4. View Total Expenses')
    print('5. View Expenses by Category')
    print('6. Exit')

def add_expense():
    global next_id

    while True:
        amount = input("Enter amount: ")
        if amount.replace('.', '', 1).isdigit():
            break
        print("Invalid input, please enter a real amount.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "id": next_id,
        "amount": float(amount),
        "category": category,
        "description": description
    }

    expenses.append(expense)
    next_id += 1
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