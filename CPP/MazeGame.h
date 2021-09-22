#include<iostream>
#include "HeroClass.h"
using namespace std;

#ifndef MAZEGAME_H
#define MAZEGAME_H

class MazeGame {
    /*
    Class used to initialise the maze game and run it.

    Attributes:
        MaximumRooms = Stores the maximum number of rooms 
                       the game will have.

    CLass Variables:
        Steve/Alex/Chloe = Three different heroes to choose from.

    Methods:
        MazeGame = Defines the initial variables of the game.

        introduceGame = Introduces the game and allows for hero 
                         to be chosen.

        runGame = Runs the game.
    */
    
    public:
        MazeGame();

        MazeGame(int MaximumRooms);

        void runGame();
    
    private:
        int maximumRooms;
        Hero hero;

        Hero Steve = Hero("Steve", 80, 21);
        Hero Alex = Hero("Alex", 60, 30);
        Hero Chloe = Hero("Chloe", 100, 16);

        void introduceGame();
};

#endif