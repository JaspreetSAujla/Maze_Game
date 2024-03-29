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
        Numbers = Stores a list of numbers, which is used to give the 
                  armour and weapons their health and attack values 
                  respectively.
        
        WeaponsList = Stores a string list of random weapons.

        ArmourList = Stores a string list of random bits of armour.

    Methods:
        __init__ = Defines the initial variables using the attributes.

        open = Runs the code for when the player wants to open the chest.
    """
    Numbers = list(range(2, 22, 2))
    WeaponsList = ['a Sword', 'a Hammer', 'a Knife', 'a Dagger', 'an Axe', 'a Trident']
    ArmourList = ['Helmet', 'Vest', 'Chest Plate', 'Shield', 'pair of Boots', 'bit of mesh']


    
    def __init__(self):
        """
        Defines the initial variables.

        Variables:
            self.number_of_weapons = Defines how many weapons can be 
                                     found in the chest.

            self.number_of_armour = Defines how many pieces of armour 
                                    can be found in the chest.

            self.weapon_points = Stores the attack points of the weapon.

            self.armour_points = Stores the health points of the armour.
        """
        # Picks random number of weapons and armour between 1 and 0.
        self.number_of_weapons = random.randint(0, 1)
        self.number_of_armour = random.randint(0, 1)

        # If the chest has either a weapon or armour, then a random 
        # number from the Numbers list is assigned to it.
        if self.number_of_weapons == 1:
            self.weapon_points = copy.deepcopy(random.choice(Chest.Numbers))
        if self.number_of_armour == 1:
            self.armour_points = copy.deepcopy(random.choice(Chest.Numbers))


    
    def open(self, Character):
        """
        Tells the code what to do when a player encounters a chest.
        Player can either open the chest or choose to ignore it.

        Parameters:
            Character = Passes in the player so that its attributes 
                        can be accessed.

        Variables:
            response = Stores the response of the player. Tells the code 
                       if the player wants to open a chest or not.
            
            valid_response = Stores whether the response was valid.
        """
        valid_response = False
        while valid_response == False:
            response = input('There is a chest here, would you like to open it? \n(yes/no) \n')
            valid_response = True
            if response == 'yes':
                if self.number_of_weapons == 1:
                    print(f"You have found {random.choice(Chest.WeaponsList)}.")
                    time.sleep(1)
                    print(f"Adding {self.weapon_points} to your attack points.")
                    Character.hero_attack += self.weapon_points
                    time.sleep(1)
                    print(Character)
                    time.sleep(1)
                if self.number_of_armour == 1:
                    print(f"You have found a {random.choice(Chest.ArmourList)}.")
                    time.sleep(1)
                    print(f"Adding {self.armour_points} to your health points.")
                    Character.hero_health += self.armour_points
                    time.sleep(1)
                    print(Character)
                    time.sleep(1)
                if self.number_of_armour == 0 and self.number_of_weapons == 0:
                    print('This chest is empty.')
                    time.sleep(1)
            elif response == "no":
                print("You choose not to open the chest.")
            else:
                print("Invalid response, try again.")
                valid_response = False