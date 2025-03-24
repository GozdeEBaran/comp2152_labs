
import random
import os


def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def inception_dream(num_dream_lvls):
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + inception_dream(num_dream_lvls - 1)


def save_game(hero_wins, hero_name="", num_stars=0):
    total_kills = load_total_kills()
    total_kills += 1

    with open("save.txt", "a") as file:
        if hero_wins:
            file.write(f"Hero {hero_name} won the fight  with {num_stars} stars.\n")
        else:
            file.write("Monster won the fight.\n")
        file.write(f"Total monsters killed: {total_kills}\n")


def load_game():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(f"Last saved game: {last_line}")
                if "Hero" in last_line:
                    return int(last_line.split()[-2])
            return 0
    except FileNotFoundError:
        print("No previous game found.")
        return 0


def load_total_kills():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Total monsters killed" in line:
                    return int(line.split(": ")[1])
            return 0
    except FileNotFoundError:
        return 0


def adjust_combat_strength(hero, monster):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                monster.combat_strength += 1
        elif "Monster won the fight" in last_game:
            hero.combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)

    choice = input("Do you want to roll manually? (y/n): ").strip().lower()
    if choice == "y":
        while True:
            try:
                loot_roll = int(input(f"Enter a number between 1 and {len(loot_options)}: "))
                if 1 <= loot_roll <= len(loot_options):
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Enter a valid number.")
    else:
        loot_roll = random.choice(range(1, len(loot_options) + 1))
    
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points

