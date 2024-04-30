class BankAccount:
    def __init__(self, first_name: str, last_name: str, account_id: int, account_type: str, pin: int, balance: float):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(self.balance)
    
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= amount
        print(self.balance)

    def display_balance(self): 
        print("You currently have " + str(self.balance))


cesare = BankAccount("Cesare", "Bianca", 32132439, "OK", 1234, 0)

cesare.deposit(96)
cesare.withdraw(25)
cesare.display_balance()