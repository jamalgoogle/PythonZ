account = 10000

while True:
    option = int(input("Enter your option (1. Deposit, 2. Withdraw, 3. Check Balance): "))
    if option == 3:  
      print(f"Your balance is: {account}")
    else:
      amount = float(input("Enter the amount to deposit/withdraw: "))

    def deposit(account, amount):
        account += amount
        return account

    def withdraw(account, amount):
        if amount <= account:
            account -= amount
            return account
        else:
            return "Insufficient funds"

    if option == 1:
        account = deposit(account, amount)
        print(f"Your updated balance is: {account}")

    elif option == 2:
        account = withdraw(account, amount)
        if isinstance(account, str):
            print(account)
        else:
            print(f"Your updated balance is: {account}")

    continue_option = input("Do you want to continue? (yes/no): ")
    if continue_option.lower() != 'yes':
        break

print("thanks for using our survices ... bye bye")