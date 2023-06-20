from random import randint


def random_pick(collection: tuple, since: int, to: int):
    try:
        return collection[randint(since, to)]
    except:
        return "Error !"