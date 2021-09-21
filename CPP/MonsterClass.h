#include<iostream>
#include<vector>
#include "RandomNumber.cpp"
#include "HeroClass.h"
using namespace std;

#ifndef MONSTERCLASS_H
#define MONSTERCLASS_H

class Monster {
    /*
    Defines the monsters.
    Takes the Name, Health and Attack of the monster as inputs.
    Description outputs the monsters stats.
    The fight method runs the code for the fight scene.

    Class Variables:
        NumbersForBlocking = Stores a list of numbers which are 
                             used to determine the probability 
                             of blocking an attack.
        
        NumbersForDodging = Stores a list of numbers which are 
                            used to determine the probability 
                            of dodging an attack.
        
        MonsterNamesList = Stores a list of names for the monsters.
    
    Attributes:
        MonsterName = Stores the name of the monster.

        MonsterHealth = Stores the health of the monster.

        MonsterAttack = Stores the attack of the monster.
    
    Methods:
        Monster = Initialises the object with input variables.

        description = Prints the stats of the monster.

        fight = Performs the fight scene.
    */
    
    public:
        string monsterName;

        Monster();

        Monster(string MonsterName, int MonsterHealth, int MonsterAttack);

        void fight(Hero hero);

    private:
        int monsterHealth;
        int monsterAttack;

        vector<int> NumbersForBlocking = {0, 0, 0, 1, 1, 1};
        vector<int> NumbersForDodging = {0, 1, 1};
        vector<string> MonsterNamesList = {"Troll", "Giant Lizard", "Weeping Angel", 
                                           "Bear", "Spider", "Skeleton", "Rat", 
                                           "Baby Dragon", "Snake", "Zombie"};
};

#endif