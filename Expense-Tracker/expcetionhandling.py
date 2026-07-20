# Task 10: Expense Tracker (Mini Project)
# Menu
# Add Expense
# View Expenses
# Calculate Total
# Delete Expense
# Exit
# Handle
# Invalid amount.
# Negative amount.
# Invalid index while deleting.
# Empty expense list.
# Invalid menu option.
# Hint:
# Use try-except for numeric input.
# Use if-else to validate amounts and indexes.
# Use finally to display a "Thank you" or cleanup message after each operation if appropriate.
expenses = []
while True:
    try:
        menu =input( """
            1.Add Expense
            2.view Expense
            3.calculate total
            4.Delete Expense
            5.Exit     """)
        if menu not in ("1","2","3","4","5"):
            raise ValueError("only Enter 1 to 5")
        if menu == "1":
            add_expense = int(input("Enter a Expense "))
            if add_expense <= 0:
                raise ValueError("don't enter add expense negative or empty")
            expenses.append(add_expense)
        elif menu == "2":
            if len(expenses) == 0:
              raise  ValueError("list is empty")
            print(expenses)
        elif menu == "3":
            total = 0
            for i in expenses:
                total+=i
                print(total)
        elif menu == "4":
            print(expenses)
            del_expense=int(input("Delete expenses give a correct index"))
            if del_expense < 0 or del_expense>=len(expenses):
                raise ValueError("invalid index")
            expenses.pop(del_expense)
        elif menu == "5":
            break
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Thank you")

    