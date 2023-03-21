from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if type(name) == str and (len(name) >= 1 and len(name) <=15):
            self.name = name
        else:
            print("Name must be a string and between 1 and 15 characters")
    name = property(get_name, set_name)