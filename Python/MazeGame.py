from HeroClass import Hero
from RoomClass import Room
import random
import time
import sys

class MazeGame:
    """
    Class used to initialise the maze game and run it.

    Attributes:
        MaximumRooms = Stores the maximum number of rooms 
                       the game will have.

    CLass Variables:
        Steve/Alex/Chloe = Three different heroes to choose from.

    Methods:
        __init__ = Defines the initial variables of the game.

        introduce_game = Introduces the game and allows for hero 
                         to be chosen.

        run_game = Runs the game.
    """
    Steve = Hero(HeroName = 'Steve',
                 HeroHealth = 80,
                 HeroAttack = 21)
    Alex = Hero(HeroName = 'Alex',
                HeroHealth = 60,
                HeroAttack = 30)
    Chloe = Hero(HeroName = 'Chloe',
                 HeroHealth = 100,
                 HeroAttack = 16)



    def __init__(self, MaximumRooms = random.randint(3, 10)):
        """
        Defines the initial variables of the game.
        Allows player to pick a character.
        
        Variables:
            self.character = Stores the character the player chose. 

            self.maximum_rooms = Stores the maximum number of rooms 
                                 in the game.   
        """
        self.maximum_rooms = MaximumRooms
        self.character = None
        self.introduce_game()
    


    def introduce_game(self):
        """
        Introduces the game and allows player to pick a hero.
        
        Variables:
            valid_response = Stores whether the player entered 
                             a valid response or not.
            
            response = Stores the players response for which hero 
                       they want.
        """
        valid_response = False

        print('Welcome contender.')
        time.sleep(1)
        print('You have accepted the challenge of trying to cross this maze of rooms.')
        time.sleep(1)
        print('But will you be able to make it out?...')
        time.sleep(1)
        print("Each room will have it's own obstacles to cross, and every room will be randomely generated.")
        time.sleep(1)
        print('Let us see if you can make it out...')
        time.sleep(1)
        print('Here are your character choices:')
        print(MazeGame.Steve)   
        print(MazeGame.Alex)
        print(MazeGame.Chloe)
        time.sleep(1)

        # Allows player to pick a character.
        while valid_response == False:
            valid_response = True
            response = input('Pick your character: \n(Steve/Alex/Chloe) \n')
            if response == 'steve':
                self.character = MazeGame.Steve
            elif response == 'alex':
                self.character = MazeGame.Alex
            elif response == "chloe":
                self.character = MazeGame.Chloe
            else:
                valid_response = False
                print("Invalid input, try again.")
        print('You have chosen:')
        print(self.character)
        time.sleep(1)
    


    def run_game(self):
        """
        Runs the code for the game.
        Loops through till the maximum number of rooms is reached.
        
        Variables:
            current_room = Stores the current room object.
            
            current_room_number = Stores the current room number. 
                                  Used as a counter in the while loop.
        """
        current_room_number = 0

        print('Now you are ready to enter the first room, good luck.')
        time.sleep(1)

        # Loops over for the number of rooms there are.
        while current_room_number < self.maximum_rooms:
            # Defines a new room.
            current_room = Room()
            print(current_room)
            # The main function that runs the room.
            # Takes character as input to be used in other files.
            current_room.run_room(Character = self.character)
            print('There are 3 doors you can go through, left, right and forward.')
            input('Which door do you go through? \n(left/right/forward) \n')
            current_room_number += 1

        # Function to run the final boss battle.
        current_room.boss_battle(Character = self.character)
        # Ends the game if the player makes it out.
        print('Well done!')
        print('You actually made it out.')
        time.sleep(2)
        print("Your character's stats are:")
        print(self.character)
        time.sleep(2)
        print('You got lucky...')
        input('Press any button to exit.')
        sys.exit()