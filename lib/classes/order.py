class Order:
    def __init__(self, customer, coffee, price: int):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    def get_price(self):
        return self.price
    
    def set_price(self, price):
        if price >= 1 and price <= 10:
            self.price = price

    price = property(get_price, set_price)
