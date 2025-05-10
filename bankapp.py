import random
#Dictionory to hold account data
accounts={};

#Create an Account

def create_account():
    account_number=str(random.randint(10000,99999))
    if account_number in accounts:
        print("Account number collision.Try again.")
        return


    name=input("Enter account holder name:").strip()
    try:
        initial_balance=float(input("Enter initial balance"))
        if initial_balance< 0:
            print("initial balance must be non-negative.")
            return

    except ValueError:
        print("invalid input for balance.")
        return

    accounts[account_number]={
            'name':name,
            'balance': initial_balance,
            'transactions':[f"account created with balance:{ initial_balance}"]
        }
    print(f"Account created successfully!Your account number is {account_number}")

#Deposite money
def deposit_money():
    account_number=input('Enter your Account no:')
    if account_number not in accounts:
        print('Account not found!')
        return
    try:
        amount=float(input('Enter the amount to deposit:'))
        if amount<=0:
            print('Please enter a positive amount.')
            return
    except ValueError:print("Invalid number")    
    accounts[account_number]['balance']+=amount
    accounts[account_number]['transactions'] .append(f'Deposited:{amount}') 
    print('deposit successful!')
#widthdow money
def widthdrow_money():
    account_number=input('Enter your account no:')
    if account_number not in accounts:
        print('Account not found')
        return
    try:
        amount=float(input('Enter amount to widthdrow:')) 
        if amount<=0:
            print('Amount must be positive') 
            return
        if amount>accounts[account_number]['balance']:
            return
    except ValueError:
        print('invalid input')  
        return  

    accounts[account_number]['balance']-=amount
    accounts[account_number]['transactions'].append(f'withdrawn:{amount}') 
    print('Withdral successful') 


def checkbalance():
    account_no=input('Enter account no:') 
    if account_no not in accounts:
        print('account not found')
        return
    balance=accounts[account_no]['balance'] 
    print(f'current balance:{balance}') 


def transactions_history():
    account_no=input('Enter your account no:')
    if account_no not in accounts:
        print('Account not found!')
        return
    print('Transactions history:') 
    for txn in accounts[account_no]['transactions']:
        print(txn)


def main():
    while True:
        print('\n-----Main Banking Application-------')
        print('1.Create Account')
        print('2.Deposite Money')
        print('3.Withdrow money')
        print('4.Check Balance')
        print('5.Transactions History')
        print('6.Exit')

        choice=input('enter your choice:')
        if choice=='1':
            create_account()
        elif choice=='2':
             deposit_money()
        elif choice=='3':
            widthdrow_money()
        elif choice=='4':
            checkbalance()
        elif choice=='5':
            transactions_history()
        elif choice=='6':
            print("Exiting programe. Goodbye!")   
            break
        else:
            print("invalid option. please try again.") 



    
main()

               

       







        