import os
import hashlib
from datetime import datetime

# File paths
ACCOUNTS_FILE = 'accounts.txt'
TRANSACTIONS_FILE = 'transactions.txt'

# Function to create a hashed password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to read accounts
def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as file:
            for line in file:
                acc_num, name, password, balance = line.strip().split(',')
                accounts[acc_num] = {'name': name, 'password': password, 'balance': int(balance)}
    return accounts

# Function to save accounts
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        for acc_num, details in accounts.items():
            file.write(f"{acc_num},{details['name']},{details['password']},{details['balance']}\n")

# Function to log transactions
def log_transaction(acc_num, transaction_type, amount):
    with open(TRANSACTIONS_FILE, 'a') as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{acc_num},{transaction_type},{amount},{date_time}\n")

# Function to create a new account
def create_account(accounts):
    acc_num = str(len(accounts) + 1).zfill(6)  # Generate unique account number
    name = input("Enter your name: ")
    password = hash_password(input("Set a password: "))
    
    while True:
        try:
            initial_balance = int(input("Enter initial deposit: "))
            if initial_balance < 0:
                print("Initial deposit cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
    
    accounts[acc_num] = {'name': name, 'password': password, 'balance': initial_balance}
    print(f"Account created successfully! Your account number is {acc_num}")
    
    save_accounts(accounts)
    log_transaction(acc_num, "Deposit", initial_balance)

# Function to login
def login(accounts):
    acc_num = input("Enter your account number: ")
    password = hash_password(input("Enter your password: "))
    
    if acc_num in accounts and accounts[acc_num]['password'] == password:
        print(f"Welcome, {accounts[acc_num]['name']}!")
        return acc_num
    else:
        print("Invalid account number or password.")
        return None

# Banking operations
def deposit(accounts, acc_num):
    while True:
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount < 0:
                print("Deposit amount cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
    
    accounts[acc_num]['balance'] += amount
    print(f"Deposit successful! New balance: {accounts[acc_num]['balance']}")
    save_accounts(accounts)
    log_transaction(acc_num, "Deposit", amount)

def withdraw(accounts, acc_num):
    while True:
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount < 0:
                print("Withdrawal amount cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
    
    if accounts[acc_num]['balance'] >= amount:
        accounts[acc_num]['balance'] -= amount
        print(f"Withdrawal successful! New balance: {accounts[acc_num]['balance']}")
        save_accounts(accounts)
        log_transaction(acc_num, "Withdrawal", amount)
    else:
        print("Insufficient balance!")

def check_balance(accounts, acc_num):
    print(f"Your current balance is: {accounts[acc_num]['balance']}")

# Main program loop
def main():
    accounts = load_accounts()
    
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            acc_num = login(accounts)
            if acc_num:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    operation = input("Choose an option: ")
                    if operation == '1':
                        deposit(accounts, acc_num)
                    elif operation == '2':
                        withdraw(accounts, acc_num)
                    elif operation == '3':
                        check_balance(accounts, acc_num)
                    elif operation == '4':
                        break
                    else:
                        print("Invalid option!")
        elif choice == '3':
            break
        else:
            print("Invalid option!")

main()
