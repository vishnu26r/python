def show_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")


def deposit():
    amount = float(input("Enter a amount to Deposit: "))
    if amount < 0:
        print("Enter valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter  amount to be Withdraw:  "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0.0
    is_running= True

    while is_running:
        print("Banking Program")
        print("1:show Balance")
        print("2:Deposit")
        print("3:Withdraw")
        print("4:Exit")

        choice= input("enter your choice (1-4):  ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("enter valid choice")

    print("thank You have a nice day!")
if __name__ == '__main__':
    main()