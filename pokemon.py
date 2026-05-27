import random
import time

class Pokemon:
    def __init__(self, name, health, stamina, element, moves):
        self.name = name
        self.health= health
        self.stamina = stamina
        self.element = element
        self.moves = moves


charmander = Pokemon("Charmander", 100, 60, "fire", {
                "Scratch":20,
                "Ember":25,
                "Growl":0
                        })

squirtle = Pokemon("Squirtle", 100, 60, "water", {
                "Tackle":20,
                "Water Gun":25,
                "Tail Whip":0
                        })

bulbasaur = Pokemon("Bulbasaur", 100, 60, "grass", {
                "Scratch":20,
                "Vine Whip":25,
                "Growl":0
                        })

potions = 3


def starter_pokemon():
    starter_pokemon = input("Choose your starter pokemon:\n" \
    "1. Bulbasaur\n2. Squirtle\n3. Charmander\n")

    if starter_pokemon == "1":
        player_pokemon = bulbasaur

    elif starter_pokemon == "2":
        player_pokemon = squirtle

    elif starter_pokemon == "3":
        player_pokemon = charmander

    else:
        print("Invalid Command")
        return
    
    print(f"You have choosen {player_pokemon.name}")
    return player_pokemon


def rival_pokemon():
    rival_pokemon = random.choice([charmander, bulbasaur, squirtle])
    print(f"The rival has {rival_pokemon.name}")
    time.sleep(0.7)
    return rival_pokemon


def battle_menu(player_pokemon, rival_pokemon):
    print(f"Your {player_pokemon.name} have {player_pokemon.health} health and {player_pokemon.stamina} stamina.")
    print()
    print(f"Rival's {rival_pokemon.name} have {rival_pokemon.health} health and {rival_pokemon.stamina} stamina.")

    print(f"What will {player_pokemon.name} do?")
    menu = input("1. Attack\n2. Bag\n3. Run\n4. Rest\n")

    if menu == "3":
        print("You decided to run")
        exit()

    elif menu == "2":
        bag(player_pokemon, rival_pokemon)

    elif menu == "1":
        player_attack(player_pokemon, rival_pokemon)

    elif menu == "4":
        rest(player_pokemon, rival_pokemon)

    else:
        print("Invalid Choice")
        battle_menu(player_pokemon, rival_pokemon)

    
def bag(player_pokemon, rival_pokemon):
    print("You opened the bag...")
    time.sleep(0.5)

    global potions

    print(f"You have {potions} potions")
    
    use_potion = input("Would you like to use potion?\n1. Yes\n2. No\n")

    if use_potion == "2":
        battle_menu(player_pokemon, rival_pokemon)

    elif use_potion == "1":

        if potions == 0:
            print("Not enough potions")
            return battle_menu(player_pokemon, rival_pokemon) 

        player_pokemon.health += 20
        potions -= 1
        print(f"You used the potion on {player_pokemon.name}")
        time.sleep(0.7)
        print(f"{player_pokemon.name} is recovered by 20 points")

        rival_attack(player_pokemon, rival_pokemon)

        if player_pokemon.health > 100:
            player_pokemon.health = 100

    else:
        print("Invalid command")
        bag(player_pokemon, rival_pokemon)


def rest(player_pokemon, rival_pokemon):
    print(f"Your {player_pokemon.name} decided to rest")
    time.sleep(1)
    print(f"Your {player_pokemon.name} recovered 20 stamina")

    player_pokemon.stamina += 20
    if player_pokemon.stamina > 60:
        player_pokemon.stamina = 60

    rival_attack(player_pokemon, rival_pokemon)


def player_attack(player_pokemon, rival_pokemon):
    print(f"What move will {player_pokemon.name} use?")

    moves = list(player_pokemon.moves.keys())

    print(f"1. {moves[0]}\n2. {moves[1]}\n3. {moves[2]}")
    move_choose = input()

    if move_choose == "1":
        if player_pokemon.stamina < 10:
            print("Not enough stamina")
            return battle_menu(player_pokemon, rival_pokemon)

        player_pokemon.stamina -= 10

    elif move_choose == "2":
        if player_pokemon.stamina < 15:
            print("Not enough stamina")
            return battle_menu(player_pokemon, rival_pokemon)

        player_pokemon.stamina -= 15

    elif move_choose == "3":
        if player_pokemon.stamina < 10:
            print("Not enough stamina")
            return battle_menu(player_pokemon, rival_pokemon)

        player_pokemon.stamina -= 10
            

    else:
        print("Invalid Choice")
        return player_attack(player_pokemon, rival_pokemon)

    move = moves[int(move_choose) - 1]

    damage = player_pokemon.moves[move]

    rival_pokemon.health -= damage

    print(f"{player_pokemon.name} used {move} on rival's {rival_pokemon.name}")
    time.sleep(1)
    print(f"It did {damage} damage on rival's {rival_pokemon.name}")
    print(f"{player_pokemon.name} used some of stamina.")

    if rival_pokemon.health <= 0:
        print("You defeated the Rival!")

    else:
        rival_attack(player_pokemon, rival_pokemon)



def rival_attack(player_pokemon, rival_pokemon):
    rival_attack = random.choice(list(rival_pokemon.moves.keys()) + ["rest"])

    if rival_attack == "rest":
        rival_pokemon.stamina += 20
        if  rival_pokemon.stamina > 60:
            rival_pokemon.stamina = 60
        battle_menu(player_pokemon, rival_pokemon)

    else:
        damage = rival_pokemon.moves[rival_attack]
        
        player_pokemon.health -= damage

        print(f"Rival's {rival_pokemon.name} used {rival_attack}")
        time.sleep(1)
        print(f"It did {damage} on your {player_pokemon.name}")

    if player_pokemon.health <= 0:
        print(f"{player_pokemon.name} fainted!")
        exit()

    else:
        battle_menu(player_pokemon, rival_pokemon)


def main():
    player = starter_pokemon()
    time.sleep(0.7)

    print("Searching for rival...")
    time.sleep(1)
    print("Found a rival!")
    rival = rival_pokemon()

    battle_menu(player, rival)

main()