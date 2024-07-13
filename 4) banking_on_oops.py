class Banking:
    def __init__(self,bal,accno):
        self.balance=bal
        self.account_number=accno
    def debit(self,amount):
        self.balance-=amount
        print(self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print(self.get_balance())
    def get_balance(self):
        return self.balance
acc=Banking(10000,12345)
acc.debit(1000)
acc.credit(500)
