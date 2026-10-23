# HEWWO :>

expenses = []

def add_expense():
    print("\n--- Add Expense ---")

    description = input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    category = input("Enter category (Food, Transport, School, Other): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in PHP: "))
        if not 0 < amount < float("inf"):
            print("Please enter a valid positive amount.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expenses.append({
        "description": description,
        "category": category.title(),
        "amount": round(amount, 2)
    })

    print("Expense added successfully!")

def view_expenses():
    print("\n--- Expense Records ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} | "
            f"{expense['category']} | "
            f"PHP {expense['amount']:.2f}"
        )

def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter the expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(f"Deleted expense: {removed['description']}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid whole number.")

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: PHP {total:.2f}")

def show_category_summary():
    print("\n--- Spending by Category ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    for category, amount in sorted(totals.items()):
        print(f"{category}: PHP {amount:.2f}")

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Show Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_category_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()