class Job:
    def __init__(self, prof, anual_income):
        self.prof = prof
        self.anual_income = anual_income


class Waiter(Job):
    def __init__(self, prof, anual_income, isPoor=True):
        super().__init__(prof, anual_income)
        self.isPoor = isPoor


class Builder(Job):
    def __init__(self, prof, anual_income, isPoor=False):
        super().__init__(prof, anual_income)
        self.isPoor = isPoor


class SoftwareEngineer(Job):
    def __init__(self, prof, anual_income, isPoor=False):
        super().__init__(prof, anual_income)
        self.isPoor = isPoor


class Teacher(Job):
    def __init__(self, prof, anual_income, isPoor=False):
        super().__init__(prof, anual_income)
        self.isPoor = isPoor