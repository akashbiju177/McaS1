class Bank:
<<<<<<< HEAD
    def __init__(self, acc_no,name,acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def show(self):
        print("\n Account details:")
        print("Account no:", self.acc_no)
        print("Name:", self.name)
        print("Type:", self.acc_type)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawal amount must be positive")
        elif self.balance < amount:
            print("Insuficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}")
            print("balance:", self.balance)
=======
    def __init__(self, acc_no, name, acc_type, balance):
        self.account_no = acc_no
        self.name = name
        self.account_type = acc_type
        self.balance = balance

    def show(self):
        print("\nAccount Details:")
        print("Account Number : ", self.account_no)
        print("Account Name : ", self.name)
        print("Account Type : ", self.account_type)
        print("Balance : ", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif self.balance < amount:
            print("Insufficent Balance")
        else:

            self.balance -= amount
            print(f"withdraw : {amount}")
            print("Balance : ", self.balance)
>>>>>>> 1d31b8c5c62b79c8f97760311a9f1bedc0a3dc0e

    def deposit(self, amount):
        if amount <= 0:
            print("enter a positive integer")
        else:
            self.balance += amount
<<<<<<< HEAD
            print(f"Deposit: {amount}")
=======
            print(f"deposited amount : {amount}")
            print("Updated amount : ", self.balance)


acc_no = int(input("enter account no: "))
name = input("enter the name : ")
acc_type = input("account type : ")
balance = float(input("initial balance : "))
account = Bank(acc_no,name,acc_type,balance)
account.show()

deposit=float(input("enter the amount to be deposited : "))
account.deposit(deposit)
withdraw=float(input("enter the amount to be withdraw : "))
account.withdraw(withdraw)


>>>>>>> 1d31b8c5c62b79c8f97760311a9f1bedc0a3dc0e

