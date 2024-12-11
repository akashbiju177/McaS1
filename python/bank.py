class Bank:
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

    def deposit(self, amount):
        if amount <= 0:
            print("enter a positive integer")
        else:
            self.balance += amount
            print(f"Deposit: {amount}")

