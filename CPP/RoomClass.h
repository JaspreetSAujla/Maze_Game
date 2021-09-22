#include<iostream>
#include "HeroClass.h"
#include "MonsterClass.h"
#include "ChestClass.h"
#include "RandomNumber.cpp"
using namespace std;

#ifndef ROOMCLASS_H
#define ROOMCLASS_H

class Room {
    /*
    Defines the rooms as they get appended to the room list.
    The class will create the correct number of monster and chest objects.
    This depends on the values in the constructor.
    The description method outputs what is in the room.
    The runRoom method runs the code for the actions taken within the room.

    Methods:
        Room = Initialises the variables.

        description = Prints what is in the room.

        runRoom = Runs the code for the room.

        bossBattle = Runs the code for the boss battle.
    */
    
    public:
        Room();

        void description();

        void runRoom(Hero hero);

        void bossBattle(Hero hero);
    
    private:
        int numberOfMonsters;
        int numberOfChests;
        Monster monster1;
        Monster monster2;
        Chest chest1;
        Chest chest2;
};

#endif