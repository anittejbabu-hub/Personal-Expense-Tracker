print("Welcome to Personal Expense Tracker")

while True:
    print("\n1. Add Expense")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        print("Expense Added:", amount, category)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
