class room:
    def __init__(self, difficulty, enemyCount):
        self.difficulty = difficulty
        self.enemyCount = enemyCount
        self.exits = {}

class player:
    def __init__(self, name):
        self.hp = 100
        self.armor = 100
        self.weapons = {}
        self.name = name
        self.wealth = 0

    def hpChange(self, difference):
        self.hp += difference


class armor:
    def __init__(self, armorPoints):
        self.defense = armorPoints

class helmet(armor):
    def __init__(self, armorPoints):
        super().__init__(armorPoints)

class chestplate(armor):
    def __init__(self, armorPoints):
        super().__init__(armorPoints)

class leggings(armor):
    def __init__(self, armorPoints):
        super().__init__(armorPoints)

class boots(armor):
    def __init__(self, armorPoints):
        super().__init__(armorPoints)
