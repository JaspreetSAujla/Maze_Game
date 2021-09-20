#include<iostream>
#include<vector>
#include "HeroClass.h"
using namespace std;

#ifndef CHESTCLASS_H
#define CHESTCLASS_H

class Chest {
    /*
    Class which defines chests.
    Takes the number of weapons and number of armour as inputs.
    Randomly chooses which item to give and assigns a value to it.
    Has a method which allows the player to open a chest.

    Class Variables:        
        WeaponsList = Stores a string list of random weapons.

        ArmourList = Stores a string list of random bits of armour.

    Methods:
        Chest = Defines the initial variables using the attributes.

        open = Runs the code for when the player wants to open the chest.
    */
    
    public:
        Chest();

        void open(Hero hero);
    
    private:
        vector<string> WeaponsList = {"a Sword", "a Hammer", "a Knife", "a Dagger", 
                                      "an Axe", "a Trident"};
        vector<string> ArmourList = {"Helmet", "Vest", "Chest Plate", "Shield", 
                                     "pair of Boots", "bit of mesh"};
        
        int numberOfWeapons;
        int numberOfArmour;
        int weaponPoints;
        int armourPoints;
};

#endif