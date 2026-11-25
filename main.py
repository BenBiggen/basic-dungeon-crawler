import random
from random import randint, uniform

def generateRoom(): # Genererer et rom og setter en vanskelighetsgrad for rommet basert på globaldifficulty
    global globalDifficulty
    difficulty = max(1, globalDifficulty + uniform(-0.5, 0.5)) # Genererer difficulty
    enemyCount = randint(2, 2*int(difficulty)) 

    newRoom = room(difficulty, enemyCount) # Lager det nye rommet fra room klassen

    for i in range(enemyCount):
        newRoom.enemies.append(generateEnemy(difficulty)) # Genererer fiender for antall fiender i rommet

    globalDifficulty += 0.1 

    return newRoom

def generateEnemy(difficulty):
    hp = int(20*difficulty*uniform(0.8, 1.2)) # Setter hp og damage for fiender basert på difficulty
    damage = int(5*difficulty*uniform(0.8, 1.2))

    enemyType = random.choice(["Goblin", "Skeleton", "Zombie", "Swede"])

    if enemyType == "Goblin": #Genererer fiende av en tilfeldig klasse med hp og damage bestemt ovenfor, gir fienden et navn
        return goblin(hp, damage, "Goblin", random.choice(["Grimnak", "Skarn", "Igdut"]))
    elif enemyType == "Skeleton":
        return skeleton(hp, damage, "Skeleton", random.choice(["Bein", "Skelly"]))
    elif enemyType == "Zombie":
        return zombie(hp, damage, "Zombie", random.choice(["Steve", "Flesh"]))
    elif enemyType == "Swede":
        return swede(hp, damage, "Swede", random.choice(["Björn", "Göran", "Johansson"]))


def lootChance(): # 2 er rare, 1 er uncommon og 0 er common, en funksjon for å velge hva loot som blir generert i en loot encounter, 10% for rare, 30% for uncommon og 60% for common
    rng = max(1, randint(1, 100)-(globalDifficulty-1))
    if rng <= 10:
        return 2
    elif rng <= 40:
        return 1
    else:
        return 0


def findLoot(player): # Basically bare genererer enten en armor piece eller et våpen og gir deg mulighet om å beholde eller ikke
    randomNum = randint(1, 2)
    if randomNum == 1:
        typer = ["helmet", "boots", "leggings", "chestplate"]
        foundLoot = armorTable[random.choice(typer)][lootChance()]
    elif randomNum == 2:
        typer = ["sword"]
        foundLoot = weaponTable[random.choice(typer)][lootChance()]

    print("--------")
    print(f"Du fant {foundLoot.name}")

    keepChoice = choice("Bytt ut", "Kast bort") # Valg om å beholde eller ikke

    if keepChoice == 1:
        if randomNum == 1:
            player.armorPiece = foundLoot
        if randomNum == 2:
            player.heldWeapon = foundLoot
        print(f"Du har nå {foundLoot.name}")
    elif keepChoice == 2:
        print(f"Du kastet bort {foundLoot.name}")

        
def choice(choice1, choice2): # Funksjon brukt for valg
    while True:
        choice = input(f"1. {choice1}, 2. {choice2}:").strip()
        if choice != "1" and choice != "2":
            continue
        else:
            return int(choice)

        
def fight(player, enemy): # Hoved funksjonen rundt kamp systemet
    global gameActive
    while player.hp > 0 and enemy.hp > 0: #Sjekker om fienden eller spilleren er død før kampen startes
        print(f"{player.name}: {player.hp}") #printer hp til spiller og fiende
        print(f"{enemy.name} the {enemy.race} (fiende): {enemy.hp}")

        choice1 = choice("Angrip", "Flykt") #1 for angrip og 2 for flykt, velger man angrip så starter man angrips fasen

        if choice1 == 1: #Fortsetter kampen rundt at spilleren angriper
            damage = player.attack() #setter damage med metoden attack()
            enemy.hpChange(-damage) #Gjør at fiende tar skade basert på attack

            print("--------")
            print(f"Du gjorde {damage} skade på {enemy.name}")
            
            if enemy.hp > 0: #sjekker om fiende er død
                if player.armorPiece is not None: #Sjekker om spilleren har noe rustning sånn at programmet ikke crasher av at den prøver å sjekke en ikke eksisterende variabel
                    player.hp -= enemy.damage * (2-player.armorPiece.defense) #Manipulerer skade tatt basert på hvor god rustning man har
                else:
                    player.hp -= enemy.damage #Spiller tar skade
                print(f"Du blir angrepet av {enemy.name}")
            print("--------")

        elif choice1 == 2:
            print(f"Du flyktet fra leiren etter å ha beseiret {player.kills} fiende(r)")
            exit() #Avslutter programmet og forteller antall kills man har om man flykter
    if player.hp <= 0: #Sjekker om spiller døde i angrips fasen
        gameActive = False 
        print(f"Du døde etter å ha beseiret {player.kills} fiende(r)")
        exit() #Terminerer programmet om man dør
    if enemy.hp <= 0: #Om fiende dør så får man beseiret den
        print(f"Du Beseiret {enemy.name}")
        player.kills += 1

def newRoom(player): #Bare det som printes og vises for hvert nytt rom ramset opp i en funksjon i stedet for å inkludere det i while løkken, litt mer oversiktlig og lettere å lese
    print("---NYTT ROM---")
    currentRoom = generateRoom()
    print(f"Du har kommet til et rom med {currentRoom.enemyCount} fiender")
    
    for enemies in currentRoom.enemies: #Lager lik antall encounters som det er fiender
        print("---Du havner i en episk kamp---")
        fight(player, enemies)
    
        if not gameActive:
            break


class room: 
    def __init__(self, difficulty, enemyCount):
        self.difficulty = difficulty
        self.enemyCount = enemyCount
        self.enemies = []
        self.loot = []


class player:
    def __init__(self):
        self.hp = 200
        self.armor = 1
        self.armorPiece = None
        self.heldWeapon = weaponTable["sword"][0]
        self.wealth = 0
        self.kills = 0

    def hpChange(self, difference): #Metode for å lettere endre hp
            self.hp += difference

    def createPlayer(self): #Lar spiller opprette navn til karakteren
        name = input("Skriv inn navnet på karakteren din:")
        self.name = name

    def attack(self): #Genererer en damage basert på våpenet spilleren holder
        rng = randint(1, 100)
    
        if self.heldWeapon.critChance >= rng:
            return self.heldWeapon.damage * 2
        else:
            return self.heldWeapon.damage


class enemy:
    def __init__(self, hp, damage, race):
        self.hp = hp
        self.damage = damage
        self.race = race

    def hpChange(self, difference): #Samme metode for å endre hp som i player
        self.hp += difference

class goblin(enemy):
    def __init__(self, hp, damage, race, name):
        super().__init__(hp, damage, race)
        self.name = name

class zombie(enemy):
    def __init__(self, hp, damage, race, name):
        super().__init__(hp, damage, race)
        self.name = name

class skeleton(enemy):
    def __init__(self, hp, damage, race, name):
        super().__init__(hp, damage, race)
        self.name = name

class swede(enemy):
    def __init__(self, hp, damage, race, name):
        super().__init__(hp, damage, race)
        self.name = name


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

#Under her har jeg bare laget noen dictionaries for å lagre loot tables til armor og våpen, lager de forskjellige våpenene / rustningene med å kalle på klassen
armorTable = {
    "helmet": [armor("Rusty helmet", 1.05, "h", "common"), armor("Good helmet", 1.15, "h", "uncommon"), armor("Helmet of no headshots", 1.3, "h", "rare")],
    "chestplate": [armor("Rusty chestplate", 1.1, "c", "common"), armor("Worthy chestplate", 1.3, "c", "uncommon"), armor("Very great chestplate", 1.6, "c", "rare")],
    "leggings": [armor("Rusty leggings", 1.08, "l", "common"), armor("Great leggings", 1.26, "l", "uncommon"), armor("Jewel protector leggings", 1.5, "l", "rare")],
    "boots": [armor("Rusty boots", 1.04, "b", "common"), armor("Marvelous boots", 1.12, "b", "uncommon"), armor("No more trench foot boots", 1.24, "b", "rare")]
}

weaponTable = {
    "sword": [weapon("Rusty sword", 30, 10, "s", "common"), weapon("Sharp sword", 60, 20, "s", "uncommon"), weapon("Stab machine", 100, 40, "s", "rare")]
}


globalDifficulty = 3

player1 = player() #Lager en karakter med base stats
player1.createPlayer() #Lar deg skrive inn et navn for karakteren
gameActive = True
while gameActive:
    newRoom(player1) 
    findLoot(player1)

