from Heroes import *
from utils.random_pick import random_pick
from utils.get_dict import get_dict
from app import main
import app

def marriage(hero):
    choice = input("Do you want to get married? y/n: ")
    if choice == "y":
        hero["endpoint"] = hero["endpoint"] - 10
        hero["marital_status"] = "married"
        hero["history"].append("got married")

def check_marital_status(hero):
    if hero["marital_status"] == "married":
        choice = input("Do you want to become an alcoholic? y/n: ")
        if choice == "y":
            hero["endpoint"] = hero["endpoint"] - 10
            hero["drinking status"] = "alcoholic"
            hero["history"].append("became an alcoholic")
    if hero["marital_status"] == "single":
        marriage(hero)

def check_drinking_status(hero):
    if hero["drinking_status"] == "non-alcoholic":
        pass
    elif hero["drinking_status"] == "alcoholic":
        hero["capital"] = hero["capital"] + 300

def sudden_death(hero):
    import random
    a = [0, 1]
    if random.choice(a) == 0:
        is_running = False
        print("Game over, the hero suddenly died")
        print(hero["history"])
    else:
        pass

def food_plan(hero):
    choice = input("Do you want to spend 100, 200,or 300 on food a year? Please type: ")
    if choice == 100:
        hero["capital"] = hero["capital"] - 100
        hero["endpoint"] = hero["endpoint"] - 0.5
    if choice == 200:
        hero["capital"] = hero["capital"] - 200
        hero["endpoint"] = hero["endpoint"] - 0.2
    if choice == 300:
        hero["capital"] = hero["capital"] - 300
        hero["endpoint"] = hero["endpoint"] + 0.2

def employment(hero):
    if hero["job"] == "waiter":
        hero["capital"] = hero["capital"] + 100
    if hero["job"] == "builder":
        hero["capital"] = hero["capital"] + 400
    if hero["job"] == "software engineer":
        hero["capital"] = hero["capital"] + 1500

def money_check(hero):
    if hero["capital"] == 0:
        is_running = False
        print("Game over! You've run out of money!")