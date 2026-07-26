try:
    def deposit_cash(balance):
        deposit = int(input("Enter deposit money"))
        balance+=deposit
        return balance
    def withdraw_cash(balance):
        withdraw = int(input("Enter a withdraw money"))
        if withdraw > balance or withdraw < 0:
            raise ValueError("balance kam hai")
        elif withdraw <= balance:
            balance = balance - withdraw
            return balance
    def checked_balance(balance):
             return balance
except Exception as e:
    print(e)
balance = 0
while True:
    try:
        print("    welcome to Bank")
        user = input("""
        1.For deposit monay
        2.For withdraw monay
        3.Check balace
        4.Exit
        Enter a option number = """)
        if user not in ("1","2","3","4") :
            raise ValueError("only Enter 1 to 4 option")
        if user == "1":
            balance = deposit_cash(balance)
        elif user == "2":
            balance = withdraw_cash(balance)
        elif user == "3":
            balance  = checked_balance(balance)
            print(f"The current balance is {balance}2")
        elif user == "4":
            break
    except ValueError as MyError:
        print(MyError)
print(balance)
