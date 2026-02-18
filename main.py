import json

print("Welcome to Personal Expense Tracker")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except:
            data = []

        data.append(expense)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Expense Saved Successfully!")

    elif choice == "2":
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            print("\nAll Expenses:")
            for expense in data:
                print(expense)

        except:
            print("No expenses found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
