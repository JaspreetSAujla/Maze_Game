#include<iostream>
#include<vector>
#include "ChestClass.h"
#include "HeroClass.h"
#include "RandomNumber.h"
using namespace std;

Chest::Chest() {
    /*
    Defines the initial variables.

    Variables:
        this.number_of_weapons = Defines how many weapons can be 
                                 found in the chest.

        this.number_of_armour = Defines how many pieces of armour 
                                can be found in the chest.

        this.weapon_points = Stores the attack points of the weapon.

        this.armour_points = Stores the health points of the armour.
    */
    // Picks random number of weapons and armour between 0 and 1.
    this->numberOfWeapons = randomNumberGenerator(0, 2);
    this->numberOfArmour = randomNumberGenerator(0, 2);

    if (this->numberOfWeapons == 1) {
        this->weaponPoints = randomNumberGenerator(1, 22);
    }
    if (this->numberOfArmour == 1) {
        this->armourPoints = randomNumberGenerator(1, 22);
    }
}



void Chest::open(Hero hero) {
    /*
    Tells the code what to do when a player encounters a chest.
    Player can either open the chest or choose to ignore it.

    Parameters:
        hero = Passes in the player so that its attributes 
                can be accessed.
            
    Variables:
        response = Stores the response of the player. Tells the code 
                   if the player wants to open a chest or not.
            
        validResponse = Stores whether the response was valid.
    */
    string response;
    bool validResponse = false;

    while (validResponse == false) {
        validResponse = true;
        cout << "There is a chest here, would you like to open it? \n(yes/no) \n";
        cin >> response;

        if (response == "yes") {
            if (this->numberOfWeapons == 1) {
                cout << "You have found " << WeaponsList[randomNumberGenerator(0, WeaponsList.size())] << endl;
                cout << "Adding " << this->weaponPoints << " to your attack points. \n";
                hero.heroAttack += this->weaponPoints;
                hero.description();
            }
            if (this->numberOfArmour == 1) {
                cout << "You have found a " << ArmourList[randomNumberGenerator(0, ArmourList.size())] << endl;
                cout << "Adding " << this->armourPoints << " to your health points. \n";
                hero.heroHealth += this->armourPoints;
                hero.description();
            }
            if (this->numberOfArmour == 0 && this->numberOfWeapons == 0) {
                cout << "This chest is empty. \n";
            }
        } else if (response == "no") {
            cout << "You choose not to open the chest. \n";
        } else {
            validResponse = false;
            cout << "Invalid response, try again. \n";
        }
    }
}