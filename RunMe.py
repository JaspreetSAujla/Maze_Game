import random
import time
import sys
from HeroClass import Hero
from MonsterClass import Monster
from ChestClass import Chest
from RoomClass import Room
import copy

if __name__ == "__main__":
    input("Press enter if code does not continue.")
    #Defines initial variables.
    number_list = [0, 1, 2]
    room_list = []
    max_rooms = random.randint(3, 10)
    room_number = 0
    Steve = Hero('Steve', 80, 21)
    Alex = Hero('Alex', 60, 30)
    Chloe = Hero('Chloe', 100, 16)

    #Introduces the player to the game.
    print('Welcome contender.')
    time.sleep(3)
    print('You have accepted the challenge of trying to cross this maze of rooms.')
    time.sleep(3)
    print('But will you be able to make it out?...')
    time.sleep(3)
    print("Each room will have it's own obstacles to cross, and every room will be randomely generated.")
    time.sleep(3)
    print('Let us see if you can make it out...')
    time.sleep(3)
    print('Here are your character choices:')
    Steve.str()
    Alex.str()
    Chloe.str()
    time.sleep(3)
    #Allows player to pick a character.
    charChoice = input('Pick your character: \n(Steve/Alex/Chloe) \n')
    if charChoice == 'Steve' or charChoice == 'steve':
        Character = Steve
    elif charChoice == 'Alex' or charChoice == 'alex':
        Character = Alex
    else:
        Character = Chloe
    print('You have chosen:')
    Character.str()
    time.sleep(3)

    print('Now you are ready to enter the first room, good luck.')
    time.sleep(3)

    #Loops over for the number of rooms there are.
    while room_number < max_rooms:
        for i in range(max_rooms):
            #Runs the code for each room.
            room_list.append(Room(random.choice(number_list), random.choice(number_list)))
            print(room_list[i])
            room_list[i].run(Character)
            print('There are 3 doors you can go through, left, right and forward.')
            Response = input('Which door do you go through? \n(left/right/forward) \n')
            room_number += 1
    #Ends the game if the player makes it out.
    print('Well done!')
    print('You actually made it out.')
    time.sleep(3)
    print("Your character's stats are:")
    Character.str()
    time.sleep(3)
    print('You got lucky...')
    input('Press any button to exit.')
    sys.exit()