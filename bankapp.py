def create_account{}:
    account_number=str(random.randint(10000,99999))
    if account_number in account:
        print("Account number collision.Try again.")
        return


    name=input("Enter account holder name:").strip()
    try:
        initial-balance=float(input("Enter initial balance"))
        if initial_balance<0:
            print("initial balance must be non-negative.")
            return

    except valueerror;
        print("invalid input for balance.")
        return

        accounts[account-number]={
            'name':name,
            'balance':initial-balance,
            'transactions':[f"account created with balance:{intial-balance}"]
        }
        print(f"Account created successfully!Your account number is {account_number}")


def deposite money():
    account_number=input('Enter your Account no:')