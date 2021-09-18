import random
import time
import sys
import copy

class Monster:
    """
    Defines the monsters.
    Takes the Name, Health and Attack of the monster as inputs.
    __str__ outputs the monsters stats.
    The fight method runs the code for the fight scene.

    Class Variables:
        NumbersForBlocking = Stores a list of numbers which are 
                             used to determine the probability 
                             of blocking an attack.
        
        NumbersForDodging = Stores a list of numbers which are 
                            used to determine the probability 
                            of dodging an attack.
    
    Attributes:
        MonsterName = Stores the name of the monster.

        MonsterHealth = Stores the health of the monster.

        MonsterAttack = Stores the attack of the monster.

        MonsterNamesList = Stores a list of names for the monsters.

        MonsterHealthList = Stores a list of values that the monsters 
                            health could be.
        
        MonsterAttackList = Stores a list of values that the monsters 
                            health could be.
    
    Methods:
        __init__ = Initialises the object with input variables.

        __str__ = Prints the stats of the monster.

        fight = Performs the fight scene.
    """
    MonsterNamesList = ["Troll", "Giant Lizard", "Weeping Angel", 
                        "Bear", "Spider", "Skeleton", "Rat", 
                        "Baby Dragon", "Snake", "Zombie"]
    MonsterHealthList = list(range(20, 100, 5))
    MonsterAttackList = list(range(5, 45, 5))
    NumbersForBlocking = [0, 1, 0, 0, 1, 1]
    NumbersForDodging = [0, 1, 1]


    
    def __init__(self, MonsterName = random.choice(MonsterNamesList), MonsterHealth = random.choice(MonsterHealthList), MonsterAttack = random.choice(MonsterAttackList)):
        """
        Defines the initial variables when an instance of this class 
        is initialised.

        Variables:
            self.monster_name = Defines the name of the monster.

            self.monster_health = Defines the health of the monster.

            self.monster_attack = Defines the attack of the monster.
        """
        self.monster_name = MonsterName
        self.monster_health = MonsterHealth
        self.monster_attack = MonsterAttack


    
    def __str__(self):
        """
        Prints the stats of the monster.
        """
        return f"{self.monster_name} --- Health: {self.monster_health}, Attack: {self.monster_attack}"


    
    def fight(self, Character):
        """
        Performs the code for the fight scene.
        Player can choose to block or dodge attacks from the monster. 
        Random probability of of either decision being successful.

        Parameters:
            Character = Uses the character object to perform the fight 
                        scene.
        
        Variables:
            response = Stores the response of the player for whether they 
                       want to dodge or block the attack.
            
            chance = Stores the value that is picked from the 
                     NumbersForBlocking and NumbersForDodging list, 
                     and executes the corresponding code.
            
            valid_response = Stores whether a valid response was entered.
        """
        print(f"You must fight the {self.monster_name}.")
        time.sleep(1)
        print('You attack first.')
        time.sleep(1)

        # Loops over as long as the monster is alive.
        while self.monster_health > 0:
            print(f"You inflicted {Character.hero_attack} damage to the monster.")
            time.sleep(1)
            self.monster_health -= Character.hero_attack
            if self.monster_health < 1:
                continue
            print(f"{self.monster_name} health: {self.monster_health}.")
            time.sleep(1)

            # Player can pick whether to block or dodge.
            # Both have different outcomes.
            valid_response = False
            while valid_response == False:
                response = input('Do you want to block or dodge the next attack? \n(block/dodge) \n')
                valid_response == True
                if response == 'block':
                    chance = copy.deepcopy(random.choice(Monster.NumbersForBlocking))
                    if chance == 1:
                        print('You have blocked the attack!')
                        time.sleep(1)
                    elif chance == 0:
                        print('You have failed to block the attack.')
                        time.sleep(1)
                        print(f"{self.monster_name} inflicts {self.monster_attack} damage to you.")
                        time.sleep(1)
                        Character.hero_health -= self.monster_attack
                elif response == 'dodge':
                    chance = copy.deepcopy(random.choice(Monster.NumbersForDodging))
                    if chance == 1:
                        print('You have dodged the attack!')
                        time.sleep(1)
                    elif chance == 0:
                        print('You have failed to dodge the attack.')
                        print(f"{self.monster_name} inflicts {self.monster_attack} damage to you.")
                        time.sleep(1)
                        Character.hero_health -= self.monster_attack
                else:
                    print("invalid response, try again.")

            # Checks hero health after each attack.
            # Ends game if hero health is zero.
            if Character.hero_health < 1:
                time.sleep(1)
                print('Your health has been reduced to zero.')
                time.sleep(1)
                print('You have died.')
                input('Press any button to quit.')
                sys.exit()
            print(f"Your health: {Character.hero_health}.")
            time.sleep(1)
        print(f"You have killed the {self.monster_name}.")
        time.sleep(1)