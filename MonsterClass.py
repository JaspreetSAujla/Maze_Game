import random
import time
import sys
from HeroClass import Hero
import copy

class Monster:
    """
    Defines the monsters.
    Takes the Name, Health and Attack of the monster as inputs.
    Str outputs the monsters stats.
    The fight method runs the code for the fight scene.
    """
    #These variables are used in the fight scene.
    Response = 0
    Number = [0, 1, 0, 0, 1, 1]
    Number2 = [0, 1, 1]
    Chance = 0


    #Defines the initial variables
    def __init__(self, MName, MHealth, MAttack):
        self.mname = MName
        self.mhealth = MHealth
        self.mattack = MAttack


    #Outputs the monster's stats.
    def str(self):
        print(self.mname, 'Health:', self.mhealth, 'Attack:', self.mattack)
        time.sleep(3)


    #Code for the fight scene.
    def fight(self, Character):
        print('You must fight the', self.mname)
        time.sleep(3)
        print('You attack first.')
        time.sleep(3)
        #Loops over as long as the monster is alive.
        while self.mhealth > 0:
            print('You inflicted', Character.hattack, 'damage to the monster.')
            time.sleep(3)
            self.mhealth -= Character.hattack
            if self.mhealth < 1:
                continue
            print(self.mname, 'health:', self.mhealth)
            time.sleep(3)
            #Player can pick whether to block or dodge.
            #Both have different outcomes.
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
            #Checks hero health after each attack.
            #Ends game if hero health is zero.
            if Character.hhealth < 0:
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