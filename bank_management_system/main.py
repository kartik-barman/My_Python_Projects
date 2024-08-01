balance = 0

def show_balance():
    print(f"Your total balance is {balance:.2f}")

def deposit():
        deposit_amount = int(input("Enter deposit Amount : "))
        if deposit_amount < 0:
            print("This is not a valid amount")
        else:
            print(f"Your amount {deposit_amount} is successfully deposit")
            return deposit_amount
    

def withdraw():
    withdraw_amount = int(input("Enter withdraw Amount : "))
    if withdraw_amount > balance:
        print("insufficient Balance")
    
    elif withdraw_amount < 0:
        print("Amount must be greater than 0")
    else:
        print(f"Your amount {withdraw_amount} is successfully withdraw")
        return withdraw_amount
        



while True:
    print("************************************")
    print("       Bank Management System       ")
    print("************************************")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Witdraw")
    print("4. Exit")
    print("***********************************")
    choice = input("Enter your Choice (1-4): ")
    
    if choice == '1':
        show_balance()
    
    elif choice == '2':
        balance += deposit()
        show_balance()
    
    elif choice == '3':
        balance -= withdraw()
    
    elif choice == '4':
        print("Closing this Program.......")
        break
    else:
        print("Invalid Choice please enter valid choice")