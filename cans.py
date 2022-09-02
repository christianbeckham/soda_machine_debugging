class Can:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cola(Can):
    def __init__(self):
        super().__init__("Cola", 0.60)


class OrangeSoda(Can):
    def __init__(self):
        super().__init__("Orange Soda", 0.40)


class RootBeer(Can):
    def __init__(self):
        super().__init__("Root Beer", 0.50)
