class Bad_Habit:
    def __init__(self, cost, harm_for_health, harm_for_family):
        self.cost = cost
        self.harm_for_health = harm_for_health
        self.harm_for_family = harm_for_family


class Smoking(Bad_Habit):
    def __init__(self, cost, harm_for_health, harm_for_family, cigs_a_day):
        self.cigs_a_day = cigs_a_day
        super().__init__(cost, harm_for_health, harm_for_family)

class Drinking(Bad_Habit):
    def __init__(self, cost, harm_for_health, harm_for_family, frequency):
        self.frequency = frequency
        super().__init__(cost, harm_for_health, harm_for_family)

class Gambling(Bad_Habit):
    def __init__(self, cost, harm_for_health, harm_for_family):
        super().__init__(cost, harm_for_health, harm_for_family)

class Drugs(Bad_Habit):
    def __init__(self, cost, harm_for_health, harm_for_family):
        super().__init__(cost, harm_for_health, harm_for_family)

class Risky_Driving(Bad_Habit):
    def __init__(self, cost, harm_for_health, harm_for_family, accident):
        self.accident = accident
        super().__init__(cost, harm_for_health, harm_for_family)