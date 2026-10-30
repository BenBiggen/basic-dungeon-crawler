import random
from random import randint

globalDifficulty = 1

def opprettKarakter():
    name = input("Skriv inn navnet på karakteren din:")
    player = player(name)  

class room:
    def __init__(self, difficulty, enemyCount):
        self.difficulty = difficulty
        self.enemyCount = enemyCount

class player:
    def __init__(self, name):
        self.hp = 100
        self.armor = 1
        self.armorPieces = {}
        self.heldWeapon = {}
        self.name = name
        self.wealth = 0

    def hpChange(self, difference):
        self.hp += difference

    def attack(weaponType, weaponId):
        rng = randint(1, 100)

        if WeaponTable[weaponType][weaponId].critChance >= rng:
            return WeaponTable[weaponType][weaponId].damage * 2
        else:
            return WeaponTable[weaponType][weaponId].damage
        


class armor:
    def __init__(self, name, armorPoints, armorType, rarity):
        self.name = name
        self.defense = armorPoints
        self.armorType = armorType
        self.rarity = rarity


class weapon:
    def __init__(self, name, damage, critChance, weaponType, rarity):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.weaponType = weaponType
        self.rarity = rarity

ArmorTable = {
    "helmet": [armor("Rusty helmet", 1.05, "h", "common"), armor("Good helmet", 1.15, "h", "uncommon"), armor("Helmet of no headshots", 1.3, "h", "rare")],
    "chestplate": [armor("Rusty chestplate", 1.1, "c", "common"), armor("Worthy chestplate", 1.3, "c", "uncommon"), armor("Very great chestplate", 1.6, "c", "rare")],
    "leggings": [armor("Rusty leggings", 1.08, "l", "common"), armor("Great leggings", 1.26, "l", "uncommon"), armor("Jewel protector leggings", 1.5, "l", "rare")],
    "boots": [armor("Rusty boots", 1.04, "b", "common"), armor("Marvelous boots", 1.12, "b", "uncommon"), armor("No more trench foot boots", 1.24, "b", "rare")]
}

WeaponTable = {
    "sword": [weapon("Rusty sword", 30, 10, "s", "common"), weapon("Sharp sword", 60, 20, "s", "uncommon"), weapon("Stab machine", 100, 40, "s", "rare")]
}

