class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self,amount):
        self.points+= int(amount*0.10)


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

customer1 = Customer("정시원", "vip")
customer2 = Customer("정찬영", "basic")

order1 = Order(1, customer1)
order1.add_item("아메리카노", 3000)
order1.add_item("초코무스", 7000)

order2 = Order(2, customer2)
order2.add_item("바닐라라떼", 4000)
order2.add_item("샌드위치", 6000)

order3 = Order(3, customer1)
order3.add_item("자몽에이드", 5000)

print("주문 1 금액:", order1.total_price())
print("주문 2 금액:", order2.total_price())
print("주문 3 금액:", order3.total_price())

order1.pay()
order2.pay()
order3.pay()

print(customer1.summary())
print(customer2.summary())
   