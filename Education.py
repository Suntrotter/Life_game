class Education:
    def __init__(self, cost, duration, document, institution):
        self.cost = cost
        self.duration = duration
        self.document = document
        self.institution = institution


class Primary_Education(Education):
    def __init__(self, cost, duration, document, institution):
        super().__init__(cost, duration, document, institution)

class Secondary_Education(Education):
    def __init__(self, cost, duration, document, institution):
        super().__init__(cost, duration, document, institution)

class Higher_Education(Education):
    def __init__(self, cost, duration, document, institution):
        super().__init__(cost, duration, document, institution)

class Further_Education(Education):
    def __init__(self, cost, duration, document, institution):
        super().__init__(cost, duration, document, institution)