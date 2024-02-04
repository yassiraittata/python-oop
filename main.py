class Item:
    pay_rate = 0.8

    def __init__(self, title: str, price: float, quantity=0):
        # validation
        assert price >= 0, f"price must be positif number"
        assert quantity >= 0, f"quantity must be positif number"

        # assign to theself object
        self.title = title
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


phone = Item('phone', 5, 4)

print(phone.title)
