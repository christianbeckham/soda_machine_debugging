class Coin:
    def __init__(self, name, value):
        self.value = value
        self.name = name


class Dime(Coin):
    def __init__(self):
        super().__init__("Dime", 0.10)


class Nickel(Coin):
    def __init__(self):
        super().__init__("Nickel", 0.05)


class Penny(Coin):
    def __init__(self):
        super().__init__("Penny", 0.01)


class Quarter(Coin):
    def __init__(self):
        super().__init__("Quarter", 0.25)
