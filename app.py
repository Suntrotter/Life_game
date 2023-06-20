from Heroes import *
from utils.is_first_appearance import is_first_appearance
from utils.get_dict_info import get_dict_info
# functions
from utils.random_pick import random_pick
from utils.get_dict import get_dict

from game import *


def main():

    is_running = True
    humans = (PoorHuman("John"), RichHuman(
        "John"), AvarageHuman("John"))

    picked_hero = random_pick(humans, 0, len(humans) - 1)

    hero = get_dict(picked_hero)

    while is_running:
        user_pick = input("Do you wanna play now ? y/n : \n")

        if user_pick != "y":
            break



        if hero:

            current_age = hero['age']
            end_point = hero['endpoint']
            game(hero, current_age, end_point)




if __name__ == "__main__":
    main()