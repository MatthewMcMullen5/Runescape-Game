
class monster:
    def __init__(self, name, level, hp, defence, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.defence = defence
        self.attack = attack


class boss_monster:
    def __init__(self, name, level, hp, defence, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.defence = defence
        self.attack = attack


# monsters
goblin = monster('Goblin', 5, 10, 1, 1)
spider = monster('Spider', 2, 5, 0, 1)

monster_list = [goblin, spider]

# bosses
obor = boss_monster('Obor', 106, 120, 6, 20)
bryophyta = boss_monster('Bryophyta', 128, 115, 5, 25)

boss_list = [obor, bryophyta]
