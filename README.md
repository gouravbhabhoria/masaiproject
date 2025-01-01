# masaiproject
# Banking System

## Overview
This is a simple banking system implemented in Python. It allows users to create accounts, log in, and perform basic banking operations such as deposits, withdrawals, and balance checks. Additionally, all transactions are logged in a separate file for tracking purposes.

---

## Features

1. **Account Creation**
   - Users can create a new account with a unique account number.
   - Passwords are securely stored using SHA-256 hashing.
   - Initial deposit amount is required (non-negative).

2. **User Login**
   - Users can log in using their account number and password.

3. **Banking Operations**
   - **Deposit**: Add money to the account balance.
   - **Withdraw**: Withdraw money from the account balance.
   - **Check Balance**: View the current account balance.

4. **Transaction Logging**
   - All deposits and withdrawals are recorded in `transactions.txt` with the following format:
     ```
     Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date
     ```

5. **Persistent Storage**
   - Account information is stored in `accounts.txt` for persistence.
   - Account details include:
     ```
     Account Number, Name, Password (hashed), Balance
     ```

---

## File Structure

### `accounts.txt`
- Stores account details in the format:
  ```
  Account Number,Name,Password,Balance
  ```

### `transactions.txt`
- Logs transactions in the format:
  ```
  Account Number,Transaction Type,Amount,Date
  ```

---

## Requirements

- Python 3.x

---

## How to Run the Program

1. Clone the repository or download the script.
2. Ensure `accounts.txt` and `transactions.txt` are in the same directory as the script (they will be created automatically if not present).
3. Run the program using:
   ```bash
   python <script_name>.py
   ```

---

## Usage

### Main Menu
1. **Create Account**: Create a new user account.
2. **Login**: Access your account and perform operations.
3. **Exit**: Exit the program.

### Banking Operations (After Login)
1. **Deposit**: Add funds to your account.
2. **Withdraw**: Remove funds from your account (if sufficient balance).
3. **Check Balance**: View your account balance.
4. **Logout**: Exit to the main menu.

---

## Security Features

- **Password Hashing**: Passwords are stored as SHA-256 hashes to ensure security.
- **Input Validation**: Prevents invalid or negative amounts during deposits and withdrawals.

---

## Example Usage

### Create an Account
```
--- Banking System ---
1. Create Account
2. Login
3. Exit
Choose an option: 1
Enter your name: John Doe
Set a password: ******
Enter initial deposit: 500
Account created successfully! Your account number is 000001
```

### Deposit Money
```
1. Deposit
2. Withdraw
3. Check Balance
4. Logout
Choose an option: 1
Enter amount to deposit: 200
Deposit successful! New balance: 700
```

### Withdraw Money
```
1. Deposit
2. Withdraw
3. Check Balance
4. Logout
Choose an option: 2
Enter amount to withdraw: 300
Withdrawal successful! New balance: 400
```

---

## Limitations

- Does not support concurrent access or multi-user sessions.
- Assumes local file-based storage; no database integration.

---

## Future Enhancements

- Add support for multi-threading for concurrent user access.
- Introduce database storage for scalability.
- Implement additional features like account deletion, password reset, and transaction history display within the program.

---

## License
This project is open-source and available under the [MIT License](LICENSE).
