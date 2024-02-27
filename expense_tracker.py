import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}  # Dictionary to store expenses with categories
        self.categories = set()  # Set to store unique expense categories

    def add_expense(self, amount, category, description):
        if category not in self.expenses:
            self.expenses[category] = []
            self.categories.add(category)
        self.expenses[category].append((amount, description, datetime.datetime.now()))

    def view_monthly_summary(self, month, year):
        total_expenses = 0
        print(f"Monthly Summary for {month}-{year}:")
        for category in self.expenses:
            category_total = sum(amount for amount, _, date in self.expenses[category]
                                 if date.month == month and date.year == year)
            total_expenses += category_total
            print(f"{category}: ${category_total}")
        print(f"Total Expenses: ${total_expenses}")

    def view_category_summary(self, category):
        if category in self.categories:
            total_category_expense = sum(amount for amount, _, _ in self.expenses[category])
            print(f"Category: {category}")
            print(f"Total Expense: ${total_category_expense}")
            print("Expenses:")
            for amount, description, date in self.expenses[category]:
                print(f"${amount} - {description} ({date.date()})")
        else:
            print("Category not found.")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount spent: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added successfully.")

        elif choice == '2':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            tracker.view_monthly_summary(month, year)

        elif choice == '3':
            category = input("Enter category: ")
            tracker.view_category_summary(category)

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
