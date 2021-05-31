import random
import time
import copy

class Chest:
    """
    Class which defines chests.
    Takes the number of weapons and number of armour as inputs.
    Randomly chooses which item to give and assigns a value to it.
    Has a method which allows the player to open a chest.

    Class Variables:
        Response = Stores the response of the player. Tells the code 
                   if the player wants to open a chest or not.
                   Set to None by default.
        
        Numbers = Stores a list of numbers, which is used to give the 
                  armour and weapons their health and attack values 
                  respectively.
        
        WeaponsList = Stores a string list of random weapons.

        ArmourList = Stores a string list of random bits of armour.

    Attributes:
        NumWeapons = Defines how many weapons can be found in a chest.

        NumArmour = Defines how many pieces of armour can be found in a chest.

    Methods:
        __init__ = Defines the initial variables using the attributes.

        open = Runs the code for when the player wants to open the chest.
    """
    Response = None
    Numbers = list(range(2, 22, 2))
    WeaponsList = ['Sword', 'Hammer', 'Knife', 'Dagger', 'Axe', 'Trident']
    ArmourList = ['Helmet', 'Vest', 'Chest Plate', 'Shield', 'pair of Boots', 'bit of mesh']


    
    def __init__(self, NumWeapons, NumArmour):
        """
        Defines the initial variables using the attributes passed into the 
        class.

        Variables:
            self.numweapons = Defines how many weapons can be found in the chest.

            self.numarmour = Defines how many pieces of armour can be found 
                             in the chest.
        """
        self.numweapons = NumWeapons
        self.numarmour = NumArmour

        # If the chest has either a weapon or armour, then a random 
        # number from the Numbers list is assigned to it.
        if self.numweapons == 1:
            self.weapon = copy.deepcopy(random.choice(Chest.Numbers))
        if self.numarmour == 1:
            self.armour = copy.deepcopy(random.choice(Chest.Numbers))


    
    def open(self, Character):
        """
        Tells the code what to do when a player encounters a chest.
        Player can either open the chest or choose to ignore it.
        """
        Chest.Response = input('There is a chest here, would you like to open it? \n(yes/no) \n')
        if Chest.Response == 'yes':
            if self.numweapons == 1:
                print('You have found a', random.choice(Chest.WeaponsList))
                time.sleep(3)
                print('Adding', self.weapon, 'to your attack points.')
                Character.hattack += self.weapon
                time.sleep(3)
                print(Character)
                time.sleep(3)
            if self.numarmour == 1:
                print('You have found a', random.choice(Chest.ArmourList))
                time.sleep(3)
                print('Adding', self.armour, 'to your health points.')
                Character.hhealth += self.armour
                time.sleep(3)
                print(Character)
                time.sleep(3)
            if self.numarmour == 0 and self.numweapons == 0:
                print('This chest is empty.')
                time.sleep(3)