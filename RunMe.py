import random
import time
import sys
from HeroClass import Hero
from MonsterClass import Monster
from ChestClass import Chest
from RoomClass import Room
import copy

Room1 = 0
Room2 = 0
Room3 = 0
Room4 = 0
Room5 = 0
Room6 = 0
Room7 = 0
Room8 = 0
Room9 = 0

RoomList = [Room(0, 0), Room(0, 1), Room(0, 2), Room(1, 0), Room(1, 1), Room(1, 2), Room(2, 0), Room(2, 1), Room(2, 2)]

Steve = Hero('Steve', 80, 21)
Alex = Hero('Alex', 60, 30)
Chloe = Hero('Chloe', 100, 16)

print('Welcome contender.')
time.sleep(4)
print('You have accepted the challenge of trying to cross this maze of rooms.')
time.sleep(4)
print('But will you be able to make it out?...')
time.sleep(4)
print("Each room will have it's own obstacles to cross, and every room will be randomely generated.")
time.sleep(5)
print('Let us see if you can make it out...')
time.sleep(4)
print('Here are your character choices:')
Steve.str()
Alex.str()
Chloe.str()
time.sleep(7)
charChoice = input('Pick your character: \n(Steve/Alex/Chloe) \n')
if charChoice == 'Steve' or charChoice == 'steve':
    Character = Steve
elif charChoice == 'Alex' or charChoice == 'alex':
    Character = Alex
else:
    Character = Chloe
print('You have chosen:')
Character.str()
time.sleep(5)

print('Now you are ready to enter the first room, good luck.')
time.sleep(5)
Room3 = copy.deepcopy(random.choice(RoomList))
Room3.str()
Room3.run(Character)
print('There are 2 doors you can go through, left and forward.')
Response = input('Which door do you go through? \n(left, forward) \n')
if Response == 'left':
    Room2 = copy.deepcopy(random.choice(RoomList))
    Room2.str()
    Room2.run(Character)
    print('There are 2 doors you can go through, right and forward.')
    Response = input('Which door do you go through? \n(right, forward) \n')
    if Response == 'forward':
        Room1 = copy.deepcopy(random.choice(RoomList))
        Room1.str()
        Room1.run(Character)
        print('There is 1 door to your right, you go through it.')
        Room4 = copy.deepcopy(random.choice(RoomList))
        Room4.str()
        Room4.run(Character)
        print('There are 2 doors you can go through, right and forward.')
        Response = input('Which door do you go through? \n(right, forward) \n')
        if Response == 'forward':
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is 1 door to your left, you go through it.')
        elif Response == 'right':
            Room5 = copy.deepcopy(random.choice(RoomList))
            Room5.str()
            Room5.run(Character)
            print('There are 2 doors you can go through, left and forward.')
            Response = input('Which door do you go through? \n(left, forward) \n')
            if Response == 'left':
                Room8 = copy.deepcopy(random.choice(RoomList))
                Room8.str()
                Room8.run(Character)
                print('There is 1 door to your left, you go through it.')
                Room7 = copy.deepcopy(random.choice(RoomList))
                Room7.str()
                Room7.run(Character)
                print('There is a door ahead of you, you go through it.')
            elif Response == 'forward':
                Room6 = copy.deepcopy(random.choice(RoomList))
                Room6.str()
                Room6.run(Character)
                print('There is 1 door to your left, you go through it.')
                Room9 = copy.deepcopy(random.choice(RoomList))
                Room9.str()
                Room9.run(Character)
                print('There is 1 door to your left, you go through it.')
                Room8 = copy.deepcopy(random.choice(RoomList))
                Room8.str()
                Room8.run(Character)
                print('There is a door ahead of you, you go through it.')
                Room7 = copy.deepcopy(random.choice(RoomList))
                Room7.str()
                Room7.run(Character)
                print('There is a door ahead of you, you go through it.')
    elif Response == 'right':
        Room5 = copy.deepcopy(random.choice(RoomList))
        Room5.str()
        Room5.run(Character)
        print('There are 3 doors you can go through, right, left and forward.')
        Response = input('Which door do you go through? \n(right, left, forward) \n')
        if Response == 'right':
            Room6 = copy.deepcopy(random.choice(RoomList))
            Room6.str()
            Room6.run(Character)
            print('There is 1 door to your left, you go through it.')
            Room9 = copy.deepcopy(random.choice(RoomList))
            Room9.str()
            Room9.run(Character)
            print('There is 1 door to your left, you go through it.')
            Room8 = copy.deepcopy(random.choice(RoomList))
            Room8.str()
            Room8.run(Character)
            print('There is a door ahead of you, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is a door ahead of you, you go through it.')
        elif Response == 'forward':
            Room8 = copy.deepcopy(random.choice(RoomList))
            Room8.str()
            Room8.run(Character)
            print('There is 1 door to your left, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is a door ahead of you, you go through it.')
        elif Response == 'left':
            Room4 = copy.deepcopy(random.choice(RoomList))
            Room4.str()
            Room4.run(Character)
            print('There is 1 door to you right, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is 1 door to your left, you go through it.')



elif Response == 'forward':
    Room6 = copy.deepcopy(random.choice(RoomList))
    Room6.str()
    Room6.run(Character)
    print('There are 2 doors you can go through, left and forward.')
    Response = input('Which door do you go through? \n(left, forward) \n')
    if Response == 'forward':
        Room9 = copy.deepcopy(random.choice(RoomList))
        Room9.str()
        Room9.run(Character)
        print('There is 1 door to your left, you go through it.')
        Room8 = copy.deepcopy(random.choice(RoomList))
        Room8.str()
        Room8.run(Character)
        print('There are 2 doors you can go through, left and forward.')
        Response = input('Which door do you go through? \n(left, forward) \n')
        if Response == 'forward':
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is 1 door straight ahead of you, so you go through it.')
        elif Response == 'left':
            Room5 = copy.deepcopy(random.choice(RoomList))
            Room5.str()
            Room5.run(Character)
            print('There are 2 doors you can go through, right and forward.')
            Response = input('Which door do you go through? \n(right, forward) \n')
            if Response == 'right':
                Room4 = copy.deepcopy(random.choice(RoomList))
                Room4.str()
                Room4.run(Character)
                print('There is 1 door to you right, you go through it.')
                Room7 = copy.deepcopy(random.choice(RoomList))
                Room7.str()
                Room7.run(Character)
                print('There is 1 door to your left, you go through it.')
            elif Response == 'forward':
                Room2 = copy.deepcopy(random.choice(RoomList))
                Room2.str()
                Room2.run(Character)
                print('There is 1 door to your right, you go through it.')
                Room1 = copy.deepcopy(random.choice(RoomList))
                Room1.str()
                Room1.run(Character)
                print('There is 1 door to your right, you go through it.')
                Room4 = copy.deepcopy(random.choice(RoomList))
                Room4.str()
                Room4.run(Character)
                print('There is 1 door ahead of you, you go through it.')
                Room7 = copy.deepcopy(random.choice(RoomList))
                Room7.str()
                Room7.run(Character)
                print('There is 1 door to your left, you go through it.')
    elif Response == 'left':
        Room5 = copy.deepcopy(random.choice(RoomList))
        Room5.str()
        Room5.run(Character)
        print('There are 3 doors you can go through, right, left and forward.')
        Response = input('Which door do you go through? \n(right, left, forward) \n')
        if Response == 'left':
            Room2 = copy.deepcopy(random.choice(RoomList))
            Room2.str()
            Room2.run(Character)
            print('There is 1 door to your right, you go through it.')
            Room1 = copy.deepcopy(random.choice(RoomList))
            Room1.str()
            Room1.run(Character)
            print('There is 1 door to your right, you go through it.')
            Room4 = copy.deepcopy(random.choice(RoomList))
            Room4.str()
            Room4.run(Character)
            print('There is 1 door ahead of you, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is 1 door to your left, you go through it.')
        elif Response == 'forward':
            Room4 = copy.deepcopy(random.choice(RoomList))
            Room4.str()
            Room4.run(Character)
            print('There is 1 door to you right, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is 1 door to your left, you go through it.')
        elif Response == 'right':
            Room8 = copy.deepcopy(random.choice(RoomList))
            Room8.str()
            Room8.run(Character)
            print('There is 1 door to your left, you go through it.')
            Room7 = copy.deepcopy(random.choice(RoomList))
            Room7.str()
            Room7.run(Character)
            print('There is a door straight ahead of you, you go through it.')
                        
            
                        

print('Well done!')
print('You actually made it out.')
time.sleep(5)
print("Your character's stats are:")
Character.str()
time.sleep(5)
print('You got lucky...')
input('Press any button to exit.')
sys.exit()
            
                
