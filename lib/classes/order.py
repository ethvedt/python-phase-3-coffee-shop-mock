class Order:
    all = []

    def __init__(self, customer, coffee, price: int):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        customer.add_order(self)
        coffee.add_order(self)
        Order.all.append(self)
        

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price >= 1 and price <= 10:
            self._price = price

    price = property(get_price, set_price)