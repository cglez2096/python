
class ShoppingCart:

    def __init__(self):
        self.items =  {}

    def add_item(self,item,qty):
        if item in self.items:
            self.items[item]+=qty
        else:
            self.items[item] = qty

    def remove_item(self,item,qty):
        if qty >= self.items[item]:
            del self. items[item]
        else:
            self.items[item] -= qty

    def get_count (self,item):
        if item in self.items:
            return self.items[item]

        else:
            return 0

    def get_total_items (self):
        return sum(self.items.values())

    def get_names (self):
        return list(self.items.keys())

    def clear_cart (self):
        self.items={}

    

