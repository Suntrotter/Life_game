from utils.get_dict_info import get_dict_info
from utils.is_game_over import is_game_over
from utils.is_first_appearance import is_first_appearance
from functions_for_life import *

def game(hero: dict, current_age: int, end_point: int):

    is_alive = True

    while current_age < end_point and is_alive:

        is_living_year = input("Live this year [y/n] : \n")

        if is_living_year != "y":
            continue

        current_age = current_age + 1
        hero['age'] += 1

        if current_age == 1:
            is_first_appearance(hero, get_dict_info)
            hero["history"].append("was born")

        elif current_age == 2:
            print(hero["name"], "you are", current_age, "years old now")
            print(hero, get_dict_info)

        elif current_age == 3:
            print(hero["name"], "you are", current_age, "years old now. You can go to a kindergarten")
            hero["history"].append("went to a kindergarten")
            print(hero, get_dict_info)

        elif current_age == 4:
            print(hero["name"], "you are", current_age, "years old now. You can do lots of things now!")
            print(hero, get_dict_info)

        elif current_age == 5:
            print(hero["name"], "you are", current_age, "years old now. You are becoming smarter and smarter!")
            print(hero, get_dict_info)

        elif current_age == 6:
            print(hero["name"], "you are", current_age, "years old now. You can start getting ready for school!")

        elif current_age == 7:
            print(hero["name"], "you are", current_age, "years old now. It's time to go to school!")
            hero["history"].append("went to school")
            print(hero, get_dict_info)

        elif current_age == 8:
            print(hero["name"], "you are", current_age, "years old now. You are doing well at school, buddy!")

        elif current_age == 9:
            print(hero["name"], "you are", current_age, "years old now. How are you doing in the matrix?")

        elif current_age == 10:
            print(hero["name"], "you are", current_age, "years old now. You are growing so fast!")

        elif current_age == 11:
            print(hero["name"], "you are", current_age, "years old now. It's time to go to a secondary school!")

        elif current_age == 12:
            print(hero["name"], "you are", current_age, "years old now. You have lots of friends!")

        elif current_age == 13:
            print(hero["name"], "you are", current_age, "years old now. The awkward age starts!")
            sudden_death(hero)

        elif current_age == 14:
            print(hero["name"], "you are", current_age, "years old now. How is your first love?")

        elif current_age == 15:
            print(hero["name"], "you are", current_age, "years old now. You are almost grown-up!")

        elif current_age == 16:
            print(hero["name"], "you are", current_age, "years old now. The first grown-up stage!")
            choice = input("Do you want to leave school? y/n: ")
            if choice == "y":
                hero["iq"] = hero["iq"] - 13
                hero["capital"] = hero["capital"] + 1000
                hero["job"] = "waiter"
                hero["history"].append("got a job as a waiter")
                employment(hero)
                money_check(hero)
                print(hero, get_dict_info)

        elif current_age == 17:
            print(hero["name"], "you are", current_age, "years old now. That's when everybody leaves school.")
            hero['job'] = "builder"
            hero["history"].append("got a job as a builder")
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 18:
            print(hero["name"], "you are", current_age, "years old now. Wow, you've grown up!")
            choice = input("Do you want to begin smoking? y/n: ")
            if choice == "y":
                hero["endpoint"] = hero["endpoint"] - 15
                hero["capital"] = hero["capital"] + 300
                hero["history"].append("started smoking")
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 19:
            print(hero["name"], "you are", current_age, "years old now. Any plans for the future?")
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 20:
            print(hero["name"], "you are", current_age, "years old now. Isn't it good to be young?")
            choice = input("Do you want to buy a phone? y/n: ")
            if choice == "y":
                hero["bag"].append("phone")
                hero["social_status"] = hero["social_status"] + 5
                hero["history"].append("bought a phone")
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 21:
            print(hero["name"], "you are", current_age, "years old now. A good age to start something great!")
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 22:
            print(hero["name"], "you are", current_age, "years old now. Don't let anyone knock you down!")
            choice = input("Do you want to buy a laptop? y/n: ")
            if choice == "y":
                hero["bag"].append("laptop")
                hero["social_status"] = hero["social_status"] + 10
                hero["history"].append("bought a laptop")
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 23:
            print(hero["name"], "you are", current_age, "years old now. It was a good year, right?")
            sudden_death(hero)
            if hero["capital"] > 10000:
                choice = input("Do you want to get a degree? y/n: ")
                if choice == "y":
                    hero["iq"] = hero["iq"] + 35
                    hero["capital"] = hero["capital"] - 1500
                    hero["social_status"] = hero["social_status"] - 10
                    hero["history"].append("went to university")
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)


        elif current_age == 24:
            print(hero["name"], "you are", current_age, "years old now. What do you really want in life, buddy?")
            marriage(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 25:
            print(hero["name"], "you are", current_age, "years old now. The life is yours!")
            choice = input("Do you want to buy a car? y/n: ")
            if choice == "y":
                hero["bag"].append("car")
                hero["social_status"] = hero["social_status"] + 15
                hero["history"].append("bought a car")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 26:
            print(hero["name"], "you are", current_age, "years old now. Just don't stop!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            if hero['capital'] > 10000:
                hero["job"] = "software engineer"
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 27:
            print(hero["name"], "you are", current_age, "years old now. Great achievements, buddy!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 28:
            print(hero["name"], "you are", current_age, "years old now. Shit happens. Take it easy.")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 29:
            print(hero["name"], "you are", current_age, "years old now. Don't worry, be happy!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 30:
            print(hero["name"], "you are", current_age, "years old now. Are you OK with that?")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 31:
            print(hero["name"], "you are", current_age, "years old now. Life goes on!")
            choice = input("Do you want to buy a house? y/n: ")
            if choice == "y":
                hero["bag"].append("house")
                hero["social_status"] = hero["social_status"] + 30
                hero["history"].append("bought a house")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 32:
            print(hero["name"], "you are", current_age, "years old now. Love your life, and it will love you, too!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 33:
            print(hero["name"], "you are", current_age, "years old now. The age of Jesus Christ!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 34:
            print(hero["name"], "you are", current_age, "years old now. You are still strong!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 35:
            print(hero["name"], "you are", current_age, "years old now. Are you happy with your life?")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 36:
            print(hero["name"], "you are", current_age, "years old now. Time for changes.")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 37:
            print(hero["name"], "you are", current_age, "years old now. There is still plenty to do!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 38:
            print(hero["name"], "you are", current_age, "years old now. Mind your health, buddy!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 39:
            print(hero["name"], "you are", current_age, "years old now. You are an experienced guy!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 40:
            print(hero["name"], "you are", current_age, "years old now. A good point to evaluate your life.")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 41:
            print(hero["name"], "you are", current_age, "years old now. There's life after forty, eh?")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 42:
            print(hero["name"], "you are", current_age, "years old now. Strange things happen")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 43:
            print(hero["name"], "you are", current_age, "years old now. Let's try meditation, eh?")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 44:
            print(hero["name"], "you are", current_age, "years old now. A nice-looking figure.")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 45:
            print(hero["name"], "you are", current_age, "years old now. You are a mature man!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 46:
            print(hero["name"], "you are", current_age, "years old now. Fire to live.")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 47:
            print(hero["name"], "you are", current_age, "years old now. Life is beautiful!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 48:
            print(hero["name"], "you are", current_age, "years old now. You are getting wiser!")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 49:
            print(hero["name"], "you are", current_age, "years old now. Time for changes, eh?")
            check_marital_status(hero)
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 50:
            print(hero["name"], "you are", current_age, "years old now. Don't worry, there is life after 50!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 51:
            print(hero["name"], "you are", current_age, "years old now. You still have a lot to experience!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 52:
            print(hero["name"], "you are", current_age, "years old now. You've changed a lot")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 53:
            print(hero["name"], "you are", current_age, "years old now. Happiness exists!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 54:
            print(hero["name"], "you are", current_age, "years old now. A good age for thinking!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 55:
            print(hero["name"], "you are", current_age, "years old now. Your body needs more attention.")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 56:
            print(hero["name"], "you are", current_age, "years old now. Life brings surprises.")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 57:
            print(hero["name"], "you are", current_age, "years old now. Is your life interesting enough?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 58:
            print(hero["name"], "you are", current_age, "years old now. Wanna add some color to life?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 59:
            print(hero["name"], "you are", current_age, "years old now. don't worry, you are still young!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 60:
            print(hero["name"], "you are", current_age, "years old now. A new level of wisdom!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 61:
            print(hero["name"], "you are", current_age, "years old now. Things are getting better, aren't they?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 62:
            print(hero["name"], "you are", current_age, "years old now. Think positive!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 63:
            print(hero["name"], "you are", current_age, "years old now. Walk every day - it helps!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 64:
            print(hero["name"], "you are", current_age, "years old now. No panic, life is long!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 65:
            print(hero["name"], "you are", current_age, "years old now. A great age to start a new hobby!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 66:
            print(hero["name"], "you are", current_age, "years old now. Keep on learning new things!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 67:
            print(hero["name"], "you are", current_age, "years old now. Share your wisdom with others!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 68:
            print(hero["name"], "you are", current_age, "years old now. Take good care of yourself!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 69:
            print(hero["name"], "you are", current_age, "years old now. Time to reap the fruits of your life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 70:
            print(hero["name"], "you are", current_age, "years old now. You look good for your age!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 71:
            print(hero["name"], "you are", current_age, "years old now. Never mind, live to the full!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 72:
            print(hero["name"], "you are", current_age, "years old now. Enjoy every day of your life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 73:
            print(hero["name"], "you are", current_age, "years old now. Life seems more and more interesting!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 74:
            print(hero["name"], "you are", current_age, "years old now. Be open to changes!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 75:
            print(hero["name"], "you are", current_age, "years old now. You've seen a lot in life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 76:
            print(hero["name"], "you are", current_age, "years old now. How are your grandchildren doing?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age == 77:
            print(hero["name"], "you are", current_age, "years old now. Life seems different, doesn't it?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 78:
            print(hero["name"], "you are", current_age, "years old now. If you are alive, your mission is not over!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 79:
            print(hero["name"], "you are", current_age, "years old now. You have something to tell other people!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 80:
            print(hero["name"], "you are", current_age, "years old now. A noble age to live to!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 81:
            print(hero["name"], "you are", current_age, "years old now. You are terrific!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 82:
            print(hero["name"], "you are", current_age, "years old now. You are as lively as ever!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 83:
            print(hero["name"], "you are", current_age, "years old now. Show them all how to live!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 84:
            print(hero["name"], "you are", current_age, "years old now. Your eyes are still cheerful!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 85:
            print(hero["name"], "you are", current_age, "years old now. You seem happy with your life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 86:
            print(hero["name"], "you are", current_age, "years old now. Which was your favorite age?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 87:
            print(hero["name"], "you are", current_age, "years old now. Time to write memoirs!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 88:
            print(hero["name"], "you are", current_age, "years old now. Don't even think of falling ill!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 89:
            print(hero["name"], "you are", current_age, "years old now. You've got so much energy!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 90:
            print(hero["name"], "you are", current_age, "years old now. You love every sunset of your life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 91:
            print(hero["name"], "you are", current_age, "years old now. You live by the sea and you like it!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 92:
            print(hero["name"], "you are", current_age, "years old now. Sounds great!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 93:
            print(hero["name"], "you are", current_age, "years old now. Life has changed a lot since you were a kid, eh?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 94:
            print(hero["name"], "you are", current_age, "years old now. And your mood is still good!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 95:
            print(hero["name"], "you are", current_age, "years old now. Talk to others, they'll appreciate your wisdom!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 96:
            print(hero["name"], "you are", current_age, "years old now. How are your great-grandchildren doing?")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 97:
            print(hero["name"], "you are", current_age, "years old now. You have all the freedom in the world.")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 98:
            print(hero["name"], "you are", current_age, "years old now. Smile every day!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 99:
            print(hero["name"], "you are", current_age, "years old now. A nice age to be loved by all your relatives!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)

        elif current_age == 100:
            print(hero["name"], "you are", current_age, "years old now. This is the crown of your life!")
            check_drinking_status(hero)
            food_plan(hero)
            employment(hero)
            money_check(hero)
            print(hero, get_dict_info)

        elif current_age > 100 and current_age != end_point:
            print("One more golden year of your long life!")

        if current_age == end_point:
            print("Sadly, the hero died")
            print("In the course of his life, he:", hero["history"])
        break

