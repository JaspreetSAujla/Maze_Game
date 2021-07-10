import random
import time
import sys
import copy

class Monster:
    """
    Defines the monsters.
    Takes the Name, Health and Attack of the monster as inputs.
    Str outputs the monsters stats.
    The fight method runs the code for the fight scene.

    Class Variables:
        Response = Stores the response of the player for whether they 
                   want to dodge or block the attack.
        
        Number = Stores a list of numbers which are used to determine 
                 the probability of blocking an attack.
        
        Number2 = Stores a list of numbers which are used to determine 
                  the probability of dodging an attack.
        
        Chance = Stores the value that is picked from the Number and 
                 Number2 list, and executes the corresponding code.
    
    Attributes:
        MName = Stores the name of the monster.

        MHealth = Stores the health of the monster.

        MAttack = Stores the attack of the monster.
    
    Methods:
        __init__ = Initialises the object with input variables.

        str = Prints the stats of the monster.

        fight = Performs the fight scene.
    """
    Response = None
    Number = [0, 1, 0, 0, 1, 1]
    Number2 = [0, 1, 1]
    Chance = None


    
    def __init__(self, MName, MHealth, MAttack):
        """
        Defines the initial variables when an instance of this class 
        is initialised.

        Variables:
            self.mname = Defines the name of the monster.

            self.mhealth = Defines the health of the monster.

            self.mattack = Defines the attack of the monster.
        """
        self.mname = MName
        self.mhealth = MHealth
        self.mattack = MAttack


    
    def str(self):
        """
        Prints the stats of the monster.
        """
        print(f"{self.mname} --- Health: {self.mhealth}, Attack: {self.mattack}")
        time.sleep(3)


    
    def fight(self, Character):
        """
        Performs the code for the fight scene.
        Player can choose to block or dodge attacks from the monster. 
        Random probability of of either decision being successful.

        Parameters:
            Character = Uses the character object to perform the fight 
                        scene.
        """
        print('You must fight the', self.mname)
        time.sleep(3)
        print('You attack first.')
        time.sleep(3)
        # Loops over as long as the monster is alive.
        while self.mhealth > 0:
            print('You inflicted', Character.hattack, 'damage to the monster.')
            time.sleep(3)
            self.mhealth -= Character.hattack
            if self.mhealth < 1:
                continue
            print(self.mname, 'health:', self.mhealth)
            time.sleep(3)
            # Player can pick whether to block or dodge.
            # Both have different outcomes.
            Monster.Response = input('Do you want to block or dodge the next attack? \n(block/dodge) \n')
            if Monster.Response == 'block':
                Monster.Chance = copy.deepcopy(random.choice(Monster.Number))
                if Monster.Chance == 1:
                    print('You have blocked the attack!')
                    time.sleep(3)
                elif Monster.Chance == 0:
                    print('You have failed to block the attack.')
                    time.sleep(3)
                    print(self.mname, 'inflicts', self.mattack, 'damage to you.')
                    time.sleep(3)
                    Character.hhealth -= self.mattack
            elif Monster.Response == 'dodge':
                 Monster.Chance = copy.deepcopy(random.choice(Monster.Number2))
                 if Monster.Chance == 1:
                    print('You have dodged the attack!')
                    time.sleep(3)
                 elif Monster.Chance == 0:
                    print('You have failed to dodge the attack.')
                    print(self.mname, 'inflicts', self.mattack, 'damage to you.')
                    time.sleep(3)
                    Character.hhealth -= self.mattack
            # Checks hero health after each attack.
            # Ends game if hero health is zero.
            if Character.hhealth < 1:
                time.sleep(1)
                print('Your health has been reduced to zero.')
                time.sleep(3)
                print('You have died.')
                input('Press any button to quit.')
                sys.exit()
            print('Your health:', Character.hhealth)
            time.sleep(3)
        print('You have killed the', self.mname)
        time.sleep(3)