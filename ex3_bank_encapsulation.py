class BankAccount:
    
    def __init__(self, owner,balance):
        self.owner = owner
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amont):
        if amont <= 0:
            print("Montant invalide")
        else:
            self.__balance += amont
            # return self.__balance
    
    def withdraw(self,amont):
        if amont > 0 and amont <= self.__balance:
            self.__balance -= amont
        else:
            print("Retrait impossible")
        
    
account = BankAccount("Alice", 1000)

print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)

account.withdraw(5000)
print(account.balance)