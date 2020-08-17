import random
import time
import sys
from HeroClass import Hero
import copy

class Monster:
    """
    Defines the monsters.
    """
    Response = 0
    Number = [0, 1, 0, 0, 1, 1]
    Number2 = [0, 1, 1]
    Chance = 0

    def __init__(self, MName, MHealth, MAttack):
        self.mname = MName
        self.mhealth = MHealth
        self.mattack = MAttack

    def str(self):
        print(self.mname, 'Health:', self.mhealth, 'Attack:', self.mattack)
        time.sleep(5)

    def fight(self, Character):
        print('You must fight the', self.mname)
        time.sleep(4)
        print('You attack first.')
        time.sleep(3)
        while self.mhealth > 0:
            print('You inflicted', Character.hattack, 'damage to the monster.')
            time.sleep(4)
            self.mhealth -= Character.hattack
            if self.mhealth < 1:
                continue
            print(self.mname, 'health:', self.mhealth)
            time.sleep(3)
            Monster.Response = input('Do you want to block or dodge the next attack? \n(block/dodge) \n')
            if Monster.Response == 'block':
                Monster.Chance = copy.deepcopy(random.choice(Monster.Number))
                if Monster.Chance == 1:
                    print('You have blocked the attack!')
                    time.sleep(4)
                elif Monster.Chance == 0:
                    print('You have failed to block the attack.')
                    time.sleep(3)
                    print(self.mname, 'inflicts', self.mattack, 'damage to you.')
                    time.sleep(4)
                    Character.hhealth -= self.mattack
            elif Monster.Response == 'dodge':
                 Monster.Chance = copy.deepcopy(random.choice(Monster.Number2))
                 if Monster.Chance == 1:
                    print('You have dodged the attack!')
                    time.sleep(4)
                 elif Monster.Chance == 0:
                    print('You have failed to dodge the attack.')
                    print(self.mname, 'inflicts', self.mattack, 'damage to you.')
                    time.sleep(4)
                    Character.hhealth -= self.mattack
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
        time.sleep(5)