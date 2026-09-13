class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self,amount):
        self.points+= int(amount*0.05)

    def get_discount_rate(self):
        if self.grade=="vip":
            return 0.1
        else:
            return 0.03

    def summary(self):
        return f"[{self.grade}]{self.name}(포인트: {self.points:,})"

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer   
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total_price(self):
        total = sum(price for name, price in self.items)
        discount_rate = self.customer.get_discount_rate()
        return int(total * (1 - discount_rate))
        
    def pay(self):
        amount = self.total_price()
        self.customer.add_points(amount)
        return amount

   