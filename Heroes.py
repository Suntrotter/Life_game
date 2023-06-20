from random import randint

from utils.name_generator import name_generator

from Constants import *


class Human:
    years_old = 0

    def __init__(self, name=name_generator(NAMES_BY_DEFAULT, 0, 2), capital=CAPITAL_BY_DEFAULT["poor"], endpoint=END_POINT_BY_DEFAULT["poor"], social_status=SOCIAL_STATUS_BY_DEFAULT["poor"], iq=IQ_BY_DEFAULT["poor"], bag=BAG_BY_DEFAULT["poor"], marital_status = MARITAL_STATUS_BY_DEFAULT, drinking_status = DRINKING_STATUS_BY_DEFAULT, job = JOB_BY_DEFAULT, history = HISTORY_BY_DEFAULT):
        self.name = name
        self.age = self.years_old
        self.capital = capital
        self.endpoint = endpoint
        self.social_status = social_status
        self.iq = iq
        self.bag = bag
        self.marital_status = marital_status
        self.drinking_status = drinking_status
        self.job = job
        self.history = history


class PoorHuman(Human):
    def __init__(self, name):
        super().__init__(name=name)


class AvarageHuman(Human):
    def __init__(
            self,
            name,
            capital=CAPITAL_BY_DEFAULT["avarage"],
            endpoint=END_POINT_BY_DEFAULT["avarage"],
            social_status=SOCIAL_STATUS_BY_DEFAULT["avarage"],
            iq=IQ_BY_DEFAULT["avarage"],
            bag=BAG_BY_DEFAULT["avarage"],
    ):
        super().__init__(
            name,
            capital,
            endpoint,
            social_status,
            iq,
            bag
        )


class RichHuman(Human):
    def __init__(self,
                 name="",
                 capital=CAPITAL_BY_DEFAULT["rich"],
                 endpoint=END_POINT_BY_DEFAULT["rich"],
                 social_status=SOCIAL_STATUS_BY_DEFAULT["rich"],
                 iq=IQ_BY_DEFAULT["rich"],
                 bag=BAG_BY_DEFAULT["rich"],

                 ):
        super().__init__(
            name,
            capital,
            endpoint,
            social_status,
            iq,
            bag,
        )
