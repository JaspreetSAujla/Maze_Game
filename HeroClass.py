import random
import time
import sys

class Hero:
    """
    Defines Hero's Attributes.
    Name, Health and Attack are the inputs of the class.
    Str outputs the stats of the hero.
    """


    #Defines initial variables.
    def __init__(self, HName, HHealth, HAttack):
        self.hname = HName
        self.hhealth = HHealth
        self.hattack = HAttack
        

    #Outputs the hero's stats.
    def str(self):
        print('Name:', self.hname, 'Health:', self.hhealth, 'Attack:', self.hattack)