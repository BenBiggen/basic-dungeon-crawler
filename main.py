import random
from random import randint, uniform

globalDifficulty = 1
gameActive = False


def ask(quest):
    active = True
    while active:
        var = input(quest)
    
    return var




def generateRoom():
    global globalDifficulty
    difficulty = max(1, globalDifficulty + uniform(-0.5, 0.5))
    enemyCount = randint(2, 4*int(difficulty))

    newRoom = room(difficulty, enemyCount)

    for i in range(enemyCount):
        newRoom.enemies.append(generateEnemy(difficulty))

    globalDifficulty =+ 0.1

    return newRoom

def generateEnemy(difficulty):
    hp = int(40*difficulty*uniform(0.8, 1.2))
    damage = int(20*difficulty*uniform(0.8, 1.2))

    names = ["Goblin", "Skeleton", "Zombie", "Swede"]
    name = random.choice(names)

    return enemy(hp, damage, name)

def lootChance(): # 2 er rare, 1 er uncommon og 0 er common
    rng = max(1, randint(1, 100)-(globalDifficulty-1))
    if rng <= 10:
        return 2
    elif rng <= 40:
        return 1
    else:
        return 0


def armorPull():
    typer = ["helmet", "boots", "leggings", "chestplate"]
    return armorTable[random.choice(typer)][lootChance()]


def choice(choice1, choice2):
    while True:
        choice = input(f"1. {choice1}, 2. {choice2}:").strip()
        if choice != "1" and choice != "2":
            continue
        else:
            return int(choice)
        



def fight(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        print(f"{player.name}: {player.hp}")
        print(f"{enemy.name} (fiende): {enemy.hp}")

        choice1 = choice("Angrip", "Flykt") #1 for angrip og 2 for beskytt

        if choice1 == 1:
            damage = 30 #midlertiding (skal bytte ut med player.heldweapon.damage eller no sånt)
            #Husk at enemy skal ha egen damage
            enemy.hpChange(-damage)

            print(f"Du gjorde {damage} skade på {enemy.name}")

            if enemy.hp > 0:
                player.hp -= enemy.damage
                print(f"Du blir angrepet av {enemy.name}")

        elif choice1 == 2:
            return False




class room:
    def __init__(self, difficulty, enemyCount):
        self.difficulty = difficulty
        self.enemyCount = enemyCount
        self.enemies = []
        self.loot = []

class player:
    def __init__(self):
        self.hp = 100
        self.armor = 1
        self.armorPieces = {}
        self.heldWeapon = {}
        self.wealth = 0

    def hpChange(self, difference):
            self.hp += difference

    def createPlayer(self):
        name = input("Skriv inn navnet på karakteren din:")
        self.name = name

class enemy:
    def __init__(self, hp, damage, name):
        self.hp = hp
        self.damage = damage
        self.name = name

    def hpChange(self, difference):
        self.hp += difference

    def attack(weaponType, weaponId):
        rng = randint(1, 100)

        if weaponTable[weaponType][weaponId].critChance >= rng:
            return weaponTable[weaponType][weaponId].damage * 2
        else:
            return weaponTable[weaponType][weaponId].damage
        


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

armorTable = {
    "helmet": [armor("Rusty helmet", 1.05, "h", "common"), armor("Good helmet", 1.15, "h", "uncommon"), armor("Helmet of no headshots", 1.3, "h", "rare")],
    "chestplate": [armor("Rusty chestplate", 1.1, "c", "common"), armor("Worthy chestplate", 1.3, "c", "uncommon"), armor("Very great chestplate", 1.6, "c", "rare")],
    "leggings": [armor("Rusty leggings", 1.08, "l", "common"), armor("Great leggings", 1.26, "l", "uncommon"), armor("Jewel protector leggings", 1.5, "l", "rare")],
    "boots": [armor("Rusty boots", 1.04, "b", "common"), armor("Marvelous boots", 1.12, "b", "uncommon"), armor("No more trench foot boots", 1.24, "b", "rare")]
}

weaponTable = {
    "sword": [weapon("Rusty sword", 30, 10, "s", "common"), weapon("Sharp sword", 60, 20, "s", "uncommon"), weapon("Stab machine", 100, 40, "s", "rare")]
}



#Bare tester systemet her
globalDifficulty = 3

##while gameActive == True:

player1 = player()
player1.createPlayer()
gameActive = True
while gameActive:

    print("---NYTT ROM---")
    currentRoom = generateRoom()
    print(f"Du har kommet til et rom med {currentRoom.enemyCount} fiender")

    for enemies in currentRoom.enemies:
        print("Du havner i en episk kamp")
        fight(player1, enemies)

