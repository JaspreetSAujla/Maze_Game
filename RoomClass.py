import random
import time
import sys
from HeroClass import Hero
from MonsterClass import Monster
from ChestClass import Chest
import copy

class Room:
    """
    Defines the rooms.
    """

    Troll = Monster('Troll', 100, 10)
    GiantLizard = Monster('Giant Lizard', 50, 50)
    WeepingAngel = Monster('Weeping Angel', 80, 25)
    Bear = Monster('Bear', 75, 35)
    Spider = Monster('Radioactive Spider', 20, 45)
    Skeleton = Monster('Skeleton', 60, 40)
    Rat = Monster('Mutant Rat', 40, 20)
    BabyDragon = Monster('Baby Dragon', 35, 70)
    Snake = Monster('Toxic Snake', 60, 30)
    Zombie = Monster('Zombie', 70, 25)
    MonsterList = [Troll, GiantLizard, WeepingAngel, Bear, Spider, Skeleton, Rat, BabyDragon, Snake, Zombie]

    Chest1 = Chest(1, 0)
    Chest2 = Chest(0, 1)
    Chest3 = Chest(0, 0)
    Chest4 = Chest(1, 1)
    ChestList = [Chest1, Chest2, Chest3, Chest4]

    def __init__(self, NumMonsters, NumChests):
        self.nummonsters = NumMonsters
        self.numchests = NumChests

        if self.nummonsters == 2:
            self.monster1 = copy.deepcopy(random.choice(Room.MonsterList))
            self.monster2 = copy.deepcopy(random.choice(Room.MonsterList))
        elif self.nummonsters == 1:
            self.monster1 = copy.deepcopy(random.choice(Room.MonsterList))
        if self.numchests == 2:
            self.chest1 = copy.deepcopy(random.choice(Room.ChestList))
            self.chest2 = copy.deepcopy(random.choice(Room.ChestList))
        elif self.numchests == 1:
            self.chest1 = copy.deepcopy(random.choice(Room.ChestList))

    def str(self):
        if self.nummonsters == 2:
            print('There is a', self.monster1.mname, 'in this room.')
            print('There is a', self.monster2.mname, 'in this room.')
            time.sleep(7)
        elif self.nummonsters == 1:
            print('There is a', self.monster1.mname, 'in this room.')
            time.sleep(6)
        if self.numchests == 2:
            print('There are 2 chests in this room.')
            time.sleep(5)
        elif self.numchests == 1:
            print('There is a chest in this room.')
            time.sleep(5)

    def run(self, Character):
        if self.nummonsters == 2:
            self.monster1.str()
            self.monster1.fight(Character)
            self.monster2.str()
            self.monster2.fight(Character)
        elif self.nummonsters == 1:
            self.monster1.str()
            self.monster1.fight(Character)
        else:
            print('There are no monsters in this room.')
            time.sleep(3)
        if self.numchests == 2:
            self.chest1.open(Character)
            self.chest2.open(Character)
        elif self.numchests == 1:
            self.chest1.open(Character)
        else:
            print('There are no chests in this room.')
            time.sleep(3)