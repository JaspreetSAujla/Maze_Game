import random
import time
from MonsterClass import Monster
from ChestClass import Chest

class Room:
    """
    Defines the rooms as they get appended to the room list.
    The class will create the correct number of monster and chest objects.
    This depends on the values in the __init__ method.
    The __str__ method outputs what is in the room.
    The run_room method runs the code for the actions taken within the room.

    Methods:
        __init__ = Initialises the variables.

        __str__ = Prints what is in the room.

        run_room = Runs the code for the room.
    """
    


    def __init__(self):
        """
        Defines the variables when the class is initialised.
        Defines the correct number of monsters and chests.
        
        Variables:
            self.number_of_monsters = Stores how many monsters are 
                                      in the room.
            
            self.number_of_chests = Stores how many chests are in 
                                    the room.
            
            self.monster1/2 = Defines a monster.

            self.chest1/2 = Defines a chest.
            """
        self.number_of_monsters = random.randint(0, 2)
        self.number_of_chests = random.randint(0, 2)

        if self.number_of_monsters == 2:
            self.monster1 = Monster()
            self.monster2 = Monster()
        elif self.number_of_monsters == 1:
            self.monster1 = Monster()
        if self.number_of_chests == 2:
            self.chest1 = Chest()
            self.chest2 = Chest()
        elif self.number_of_chests == 1:
            self.chest1 = Chest()



    def __str__(self):
        """
        Prints what is in the room.
        """
        if self.number_of_monsters == 2:
            print(f"There is a {self.monster1.monster_name} in this room.")
            print(f"There is a {self.monster2.monster_name} in this room.")
            time.sleep(1)
        elif self.number_of_monsters == 1:
            print(f"There is a {self.monster1.monster_name} in this room.")
            time.sleep(1)
        if self.number_of_chests == 2:
            print('There are 2 chests in this room.')
            time.sleep(1)
        elif self.number_of_chests == 1:
            print('There is a chest in this room.')
            time.sleep(1)
        return ""



    def run_room(self, Character):
        """
        Runs the code for when the player is in a room.
        Checks to see if there are any monsters and chests, 
        and performs the appropriate code.

        Parameters:
            Character = Passes in the player so the attributes 
                        can be accessed.
        """
        if self.number_of_monsters == 2:
            print(self.monster1)
            self.monster1.fight(Character = Character)
            print(self.monster2)
            self.monster2.fight(Character = Character)
        elif self.number_of_monsters == 1:
            print(self.monster1)
            self.monster1.fight(Character = Character)
        else:
            print('There are no monsters in this room.')
            time.sleep(1)
        if self.number_of_chests == 2:
            self.chest1.open(Character = Character)
            self.chest2.open(Character = Character)
        elif self.number_of_chests == 1:
            self.chest1.open(Character = Character)
        else:
            print('There are no chests in this room.')
            time.sleep(1)
    


    def BossBattle(self, Character):
        """
        This function runs the final boss battle.
        Once the player reaches the final room, they must fight the boss.
        Takes the Character as a parameter.
        Two lists have been defined for the monster attack and health.
        A new monster object is defined and the fight function is run.

        Parameters:
            Character = Passes in the player so the attributes can be 
                        used.
        
        Variables:
            dragon_attack_list = Stores the attack points the dragon 
                                 could have.
            
            dragon_health_list = Stores the health points the dragon 
                                 could have.
            
            dragon = Defines the boss.
        """
        dragon_attack_list = list(range(30, 75, 5))
        dragon_health_list = list(range(150, 310, 20))
        # Define new monster object.
        dragon = Monster(MonsterName = "Giant Dragon", 
                         MonsterHealth = random.choice(dragon_health_list), 
                         MonsterAttack = random.choice(dragon_attack_list))
        print("You enter a room and see a Giant Dragon!")
        time.sleep(2)
        print("You can see the exit behind the dragon.")
        time.sleep(2)
        print("You must fight the dragon to escape...")
        time.sleep(2)
        print(dragon)
        dragon.fight(Character = Character)