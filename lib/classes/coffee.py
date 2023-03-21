from classes.order import Order

class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
      
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        pass

    name = property(get_name, set_name)

    def add_order(self, order):
        self._orders.append(order)
    
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(map(lambda order: order.customer, self.orders())))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total_price = 0
        for order in self.orders():
            total_price += order.price
        return total_price/len(self.orders())
