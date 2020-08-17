import random
import time
import sys

class Hero:
    """
    Defines Hero's Attributes.
    """

    def __init__(self, HName, HHealth, HAttack):
        self.hname = HName
        self.hhealth = HHealth
        self.hattack = HAttack
        

    def str(self):
        print('Name:', self.hname, 'Health:', self.hhealth, 'Attack:', self.hattack)