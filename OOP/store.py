class Store:
    def __init__(name, productList=''):
        self.userID = name
        
    def add_product(self, new_product):
        self.productList += new_product
        return self
    def sell_product(self, id):
        self.productList -= new_product
    def inflation(self, percent_increase):
        self.cost *= percent_increase
    def set_clearance(self, category, percent_discount):   
        self.cost /= percent_discount
class Product:
    def __init__(name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased > self.price:
            self.price *= percent_change
        else:
            self.price /= percent_change
    def print_info(self):
        print(f"This is a {self.name} which is a {self.category} and costs {self.price}")


apple = Product("apple",1,"fruit")

apple.print_info