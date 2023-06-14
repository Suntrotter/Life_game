class Property:
    def __init__(self, cost, age):
        self.cost = cost
        self.age = age


class Car(Property):
    def __init__(self, cost, age, color, model):
        self.color = color
        self.model = model
        super().__init__(cost, age)


class House(Property):
    def __init__(self, cost, age, area):
        self.area = area
        super().__init__(cost, age)


class Phone(Property):
    def __init__(self, cost, age, model):
        self.model = model
        super().__init__(cost, age)


class Laptop(Property):
    def __init__(self, cost, age, performance):
        self.performance = performance
        super().__init__(cost, age)

