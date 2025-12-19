class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Device Name: {self.name}, Price: ₹{self.price}"


class Mobile(Device):
    pass


iphone = Mobile("iPhone", 100000)
print(iphone)
