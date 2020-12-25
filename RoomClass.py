import random
import time
import sys
from HeroClass import Hero
from MonsterClass import Monster
from ChestClass import Chest
import copy

class Room:
    """
    Defines the rooms as they get appended to the room list.
    The class will create the correct number of monster and chest objects.
    This depends on the values in the __init__ method.
    The str method outputs what is in the room.
    The run method runs the code for the actions taken within the room.
    """
    # These variables allow random monster and chest objects to be generated.
    monster_name_list = ["Troll", "Giant Lizard", "Weeping Angel", "Bear", "Spider", "Skeleton", "Rat", "Baby Dragon", "Snake", "Zombie"]
    monster_health_list = list(range(20, 100, 5))
    monster_attack_list = list(range(5, 45, 5))
    chest_list = [0, 1]                          # To choose either 0/1 weapon or armour items.


    # Defines initial variables of the class.
    def __init__(self, NumMonsters, NumChests):
        self.nummonsters = NumMonsters
        self.numchests = NumChests

        if self.nummonsters == 2:
            self.monster1 = Monster(random.choice(Room.monster_name_list), random.choice(Room.monster_health_list), random.choice(Room.monster_attack_list))
            self.monster2 = Monster(random.choice(Room.monster_name_list), random.choice(Room.monster_health_list), random.choice(Room.monster_attack_list))
        elif self.nummonsters == 1:
            self.monster1 = Monster(random.choice(Room.monster_name_list), random.choice(Room.monster_health_list), random.choice(Room.monster_attack_list))
        if self.numchests == 2:
            self.chest1 = Chest(random.choice(Room.chest_list), random.choice(Room.chest_list))
            self.chest2 = Chest(random.choice(Room.chest_list), random.choice(Room.chest_list))
        elif self.numchests == 1:
            self.chest1 = Chest(random.choice(Room.chest_list), random.choice(Room.chest_list))


    # Outputs what is in the room.
    def __str__(self):
        if self.nummonsters == 2:
            print('There is a', self.monster1.mname, 'in this room.')
            print('There is a', self.monster2.mname, 'in this room.')
            time.sleep(3)
        elif self.nummonsters == 1:
            print('There is a', self.monster1.mname, 'in this room.')
            time.sleep(3)
        if self.numchests == 2:
            print('There are 2 chests in this room.')
            time.sleep(3)
        elif self.numchests == 1:
            print('There is a chest in this room.')
            time.sleep(3)
        return ""


    # Runs the code for the actions taken in the room.
    def run(self, Character):
        if self.nummonsters == 2:
            self.monster1.str()
            self.monster1.fight(Character)
            self.monster2.str()
            self.monster2.fight(Character)
        elif self.nummonsters == 1:
            self.monster1.str()
            self.monster1.fight(Character)
        else:
            print('There are no monsters in this room.')
            time.sleep(3)
        if self.numchests == 2:
            self.chest1.open(Character)
            self.chest2.open(Character)
        elif self.numchests == 1:
            self.chest1.open(Character)
        else:
            print('There are no chests in this room.')
            time.sleep(3)
    

    def BossBattle(self, Character):
        """
        This function runs the final boss battle.
        Once the player reaches the final room, they must fight the boss.
        Takes the Character as a parameter.
        Two lists have been defined for the monster attack and health.
        A new monster object is defined and the fight function is run.
        """
        dragon_attack_list = list(range(30, 75, 5))
        dragon_health_list = list(range(150, 310, 20))
        # Define new monster object.
        dragon = Monster("Giant Dragon", random.choice(dragon_health_list), random.choice(dragon_attack_list))
        print("You enter a room and see a Giant Dragon!")
        time.sleep(2)
        print("You can see the exit behind the dragon.")
        time.sleep(2)
        print("You must fight the dragon to escape...")
        time.sleep(2)
        dragon.str()
        dragon.fight(Character)

