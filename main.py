class Item:
    pay_rate = 0.8
    all_items = []

    def __init__(self, title: str, price: float, quantity=0):
        # validation
        assert price >= 0, f"price must be positif number"
        assert quantity >= 0, f"quantity must be positif number"

        # assign to theself object
        self.title = title
        self.price = price
        self.quantity = quantity

        # Actions
        Item.all_items.append(self)

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        total = self.price = self.price * Item.pay_rate
        return total

    def __repr__(self):
        return f"Item('{self.title}', '{self.price}', '{self.quantity}')"

    @classmethod
    def instance_from_csv(cls):
        print('hello')


phone = Item('phone', 500, 4)
phone = Item('Laptop', 999, 4)
phone = Item('watch', 349, 4)

phone.instance_from_csv()

# Item.instance_from_csv()

# print(phone.title)
