import random, time, sys

classes = ["Warrior", "Mage", "Rogue"]

statDict = {"Strength": 0, "Vitality": 0, "Intellect": 0, "Wisdom": 0, "Agility": 0, "Sneak": 0}

steps = ["forward", "left", "right"]

corPath = []
step = random.randint(2,10)
for i in range(1,step):
    corPath.append(steps[random.randint(0,2)])

encounters = [" you spot a goblin.", " you stumble upon a corpse holding a book titled \"The Secret To A Warrior's Strength\".", " you stumble upon a corpse holding a book titled \"The Secret To A Mages' Intellect\".", " you stumble upon a corpse holding a book titled \"The Secret To A Rogue's Sneakiness\"."]

userPath = []

health = 3

gold = 0

pas = 0

def types(x):
    px = list(x)
    for i in px:
        if i == ".":
            print(i, end="")
            time.sleep(0)
        else:
            print(i, end="")
            time.sleep(0)

def encounted(gold, health):
    arse = random.randint(0, 100)
    rand = encounters[random.randint(0,3)]
    
    if arse == 78:
        types("\nYou found a shortcut!")
        types("\nYou successfully traversed this place with a shorcut. Your luck is quite good. Congratulations! You win.")
        sys.exit()
        
    types("\nAs you move towards this direction, " + rand)

    if rand == encounters[0]:
        types("""\nWhat would you like to do?
[1] Attack
[2] Sneak
""")
        while True:
            try:
                act = int(input())
            except ValueError:
                types("Please input a number.")
                continue
            else:
                break

        if arse == 63:
            types("You were unable to sneak or fight the goblin and got killed.\n\nYou lost!")
            sys.exit()
        elif act == 1 and (statDict["Strength"] >= 1 or statDict["Intellect"] >= 1):
            types("You successfully defeated the goblin and gained 20 gold!")
            gold += 20
            status(gold, health)
        elif act == 1 and statDict["Strength"] < 1:
            types("You were unable to defeat the goblin. Fortunately, you managed to run away but you lost 1 health in the process.")
            health -= 1
            status(gold, health)
        elif act == 2 and statDict["Sneak"] == 1:
            types("You successfully sneaked out of the room without the goblin noticing.")
            status(gold, health)
        elif act == 2 and statDict["Sneak"] == 0:
            types("You were unable to sneak away unnoticed. Fortunately, you managed to run away but you lost 1 health in the process.")
            status(gold, health)
        
    elif rand == encounters[1]:
        types("""\nWhat would you like to do?
[1] Read
[2] Leave
""")
        while True:
            try:
                act = int(input())
            except ValueError:
                types("Please input a number.")
                continue
            else:
                break

        if arse == 83:
            types("You were unable to see the hole in floor and fell to your death.\n\nYou lost!")
            sys.exit()
        elif act == 1 and statDict["Intellect"] >= 1:
            types("You were successfully able to read and understand the book, +1 to your strength!")
            statDict["Strength"] += 1
            status(gold, health)
        elif act == 1 and statDict["Intellect"] < 1:
            types("You were unable to understand the book, your stupidity is utterly dissapointing.")
            status(gold, health)
        elif act == 2:
            types("You decide to leave and continue on.")
            status(gold, health)

    elif rand == encounters[2]:
        types("""\nWhat would you like to do?
[1] Read
[2] Leave
""")
        while True:
            try:
                act = int(input())
            except ValueError:
                types("Please input a number.")
                continue
            else:
                break

        if arse == 23:
            types("You were unable to see the hole in floor and fell to your death.\n\nYou lost!")
            sys.exit()
        elif act == 1 and statDict["Intellect"] >= 0:
            types("You were successfully able to read and understand the book, +1 to your intellect!")
            statDict["Intellect"] += 1
            status(gold, health)
        elif act == 2:
            types("You decide to leave and continue on.")
            status(gold, health)

    elif rand == encounters[3]:
        types("""\nWhat would you like to do?
[1] Read
[2] Leave
""")
        while True:
            try:
                act = int(input())
            except ValueError:
                types("Please input a number.")
                continue
            else:
                break

        if arse == 47:
            types("You were unable to see the hole in floor and fell to your death.\n\nYou lost!")
            sys.exit()
        elif act == 1 and statDict["Intellect"] >= 1:
            types("You were successfully able to read and understand the book, +1 to your sneakiness!")
            statDict["Sneak"] += 1
            status(gold, health)
        elif act == 1 and statDict["Intellect"] < 1:
            types("You were unable to understand the book, your stupidity is utterly dissapointing.")
            status(gold, health)
        elif act == 2:
            types("You decide to leave and continue on.")
            status(gold, health)


def status(gold, health):
    global pas
    
    if userPath[0] == corPath[0] and pas == 0:
        types("\nIt appears you gone the right way. For now...")
        pas+=1

    if len(userPath) == len(corPath):
        if userPath == corPath:
            time.sleep(1)
            types("\n\nYou are the one and only escapee of this place. Congratulations! You win.")
            sys.exit()
        else:
            time.sleep(1)
            types("\n\nYou were unable to escape this place. You lost!")
            sys.exit()
    
    if statDict["Vitality"] >= 1:
        health+=1
        
    types("\n\nYou currently have "+str(health)+" health and "+str(gold)+" gold.")
    types("\nYour stats are:\nStrength: "+str(statDict["Strength"])+"      Vitality: "+str(statDict["Vitality"])+"\nIntellect: "+str(statDict["Intellect"])+"     Wisdom: "+str(statDict["Wisdom"])+"\nAgility: "+str(statDict["Agility"])+"       Sneak: "+str(statDict["Sneak"])+"")

    direction()

def direction():    
    while True:
        types("\n\nWhich way would you like to go? (forward, left, right) ")
        direct = input()
        if direct.lower() != "forward" and direct.lower() != "left" and direct.lower() != "right" or direct.lower() == "konami code":
            if direct.lower() == "konami code":
                print('\n'+str(corPath), end="")
                continue
            else:
                types("\nPlease choose between forward, left and right only.")
                continue
        elif direct.lower() == "forward" or direct.lower() == "left" or direct.lower() == "right":
            types("You went " + direct.lower() + ".\n")     
        break

    userPath.append(direct)

    encounted(gold, health)

def gameStart():
    types("\nYou suddenly find yourself in a strange cave, with humid air and lumious moss that gives an ominous glow.")
    types(" As your eyes begin to adjust to the darkness, you realize you're completely alone with no resources and no way to get out.")
    types(" You hear a voice telling you that this place is your doom. No man has ever escaped.")
    types("\nThat is where you come in...")

    types("\nWhich class would you like to be?\n")
    while True:
        try:
            cl = int(input("""
[1] Warrior - (+1 Strength) (+2 Vitality)
[2] Mage - (+2 Intellect) (+1 Wisdom)
[3[ Rogue - (+2 Agility) (+1 Sneak)
"""))
        except ValueError:
            types("Please input a number: ")
            continue
        else:
            break

    clt = cl - 1

    types("What an excellent choice! You chose to be a " + classes[clt] + ".")

    types("\nSince you chose "+ classes[clt] + " your stats are:\n")

    if clt == 0:
        types("\nStrength: 2      Vitality: 1\nIntellect: 0     Wisdom: 0\nAgility: 0       Sneak: 0")
        statDict["Strength"] = 2
        statDict["Vitality"] = 1
    elif clt == 1:
        types("\nStrength: 0      Vitality: 0\nIntellect: 2     Wisdom: 1\nAgility: 0       Sneak: 0")
        statDict["Intellect"] = 2
        statDict["Wisdom"] = 1
    elif clt == 2:
        types("\nStrength: 0      Vitality: 0\nIntellect: 0     Wisdom: 0\nAgility: 2       Sneak: 1")
        statDict["Agility"] = 2
        statDict["Sneak"] = 1

    types("\n\nAs a proud " + classes[clt] + ", you confidently walk inside the dungeon.")

    types("\nYou hear a whisper saying \""+str(len(corPath))+" more rooms...\", how peculiar.")
    
    fell = random.randint(1, 100)
    if fell == random.randint(1,100):
        types("\nAnd you immediately trip and hit your head on a pointy rock.....")
        types("\nHow utterly dissapointing.")
        types("\nYou lose!")
        sys.exit()

    if statDict["Wisdom"] == 1:
        types("\nYour wisdom compels you to think that the first step to escaping is to go " + corPath[0] + ".")

    direction()

def startGame():
    types("This is simple text-based dungeon crawler game.\n")
    types("Would you like to play? (yes/no) ")
    inp = input()
    
    while True:
        # checks if user inputs yes or no, if not continues to ask user to input yes or no
        if inp.lower() == "yes" or inp.lower() == "no":
            break
        else:
            types("Please input yes/no only: ")
            inp = input()
            continue
        
    if inp.lower() == "yes":
        gameStart()
    elif inp.lower() == "no":
        sys.exit()

startGame()
        
