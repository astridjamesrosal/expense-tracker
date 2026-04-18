expenses = []
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

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 6.")