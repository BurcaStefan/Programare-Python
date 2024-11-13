class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Ai depozitat: {amount}. Bani in cont: {self.balance}.")
        else:
            print("Nu poti depune o suma negativa!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Ai extras {amount}. Bani in cont: {self.balance}.")
        else:
            print("Suma nu e valida!")

    def get_balance(self):
        print(f"Soldul contului: {self.balance}.")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Dobanda: {interest}.")
        return interest

class CheckingAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)


savings = SavingsAccount("Ion", 1000)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()

checking = CheckingAccount("Mihai", 500)
checking.deposit(300)
checking.get_balance()