import random
import time
import sys
from HeroClass import Hero
from MonsterClass import Monster
import copy

class Chest:
    """
    Class which defines chests.
    Takes the number of weapons and number of armour as inputs.
    #Randomly chooses which item to give and assigns a value to it.
    """
    #Variables used to define the chest objects.
    Response = 0
    Numbers = list(range(2, 22, 2))
    WeaponsList = ['Sword', 'Hammer', 'Knife', 'Dagger', 'Axe', 'Trident']
    ArmourList = ['Helmet', 'Vest', 'Chest Plate', 'Shield', 'pair of Boots', 'bit of mesh']


    #Defines the initial variables.
    def __init__(self, NumWeapons, NumArmour):
        self.numweapons = NumWeapons
        self.numarmour = NumArmour

        if self.numweapons == 1:
            self.weapon = copy.deepcopy(random.choice(Chest.Numbers))
        if self.numarmour == 1:
            self.armour = copy.deepcopy(random.choice(Chest.Numbers))


    #Performs the main code for when the player opens the chest.
    def open(self, Character):
        Chest.Response = input('There is a chest here, would you like to open it? \n(yes/no) \n')
        if Chest.Response == 'yes':
            if self.numweapons == 1:
                print('You have found a', random.choice(Chest.WeaponsList))
                time.sleep(3)
                print('Adding', self.weapon, 'to your attack points.')
                Character.hattack += self.weapon
                time.sleep(3)
                Character.str()
                time.sleep(3)
            if self.numarmour == 1:
                print('You have found a', random.choice(Chest.ArmourList))
                time.sleep(3)
                print('Adding', self.armour, 'to your health points.')
                Character.hhealth += self.armour
                time.sleep(3)
                Character.str()
                time.sleep(3)
            if self.numarmour == 0 and self.numweapons == 0:
                print('This chest is empty.')
                time.sleep(3)