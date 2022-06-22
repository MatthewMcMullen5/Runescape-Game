import random


class monster:
    def __init__(self, name, level, hp, defence, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.defence = defence
        self.attack = attack


goblin = monster('Goblin', 5, 15, 1, 2)
spider = monster('Spider', 2, 10, 0, 1)

monster_list = [goblin, spider]


