from classes.order import Order

class Coffee:
    def __init__(self, name):
        self._name = name
      
    def get_name(self):
        return self._name
    
    name = property(get_name)