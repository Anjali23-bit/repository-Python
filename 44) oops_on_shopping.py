class Shopping:
    def __init__(self,cost,price,items):
        self.price=price
        self.items=items
        self.cost=cost
    def add(self,items,price):
        self.cost+=(items*price)
        print(self.get_cost())
    def remove(self,items,price):
        self.cost-=(items*price)
        print(self.get_cost())
    def get_cost(self):
        return self.cost
shop=Shopping(0,20,5)
shop.add(7,15)
shop.remove(2,15)
