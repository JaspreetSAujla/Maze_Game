#include<iostream>
#include<vector>
#include<stdlib.h>
#include "RandomNumber.h"
#include "MonsterClass.h"
#include "HeroClass.h"
using namespace std;

Monster::Monster() {
    this->monsterName = MonsterNames[randomNumberGenerator(0, MonsterNames.size())];
    this->monsterHealth = randomNumberGenerator(20, 96);
    this->monsterAttack = randomNumberGenerator(5, 46);
}



Monster::Monster(string MonsterName, int MonsterHealth, int MonsterAttack) {
    this->monsterName = MonsterName;
    this->monsterHealth = MonsterHealth;
    this->monsterAttack = MonsterAttack;
}



void Monster::description() {
    /*
    Prints the stats of the monster.
    */
    cout << this->monsterName << " --- Health: " << this->monsterHealth << 
            ", Attack: " << this->monsterAttack << endl;
}



void Monster::fight(Hero hero) {
    /*
    Performs the code for the fight scene.
    Player can choose to block or dodge attacks from the monster. 
    Random probability of of either decision being successful.

    Parameters:
        hero = Uses the character object to perform the fight 
               scene.
                    
    Variables:
        response = Stores the response of the player for whether they 
                   want to dodge or block the attack.
            
        chance = Stores the value that is picked from the 
                 NumbersForBlocking and NumbersForDodging list, 
                 and executes the corresponding code.
            
        validResponse = Stores whether a valid response was entered.
    */
    bool validResponse;
    int chance;
    string response;
    cout << "You must fight the " << this->monsterName << endl;
    cout << "You attack first. \n";

    // Loops as long as the monster is alive.
    while (this->monsterHealth > 0) {
        cout << "You inflicted " << hero.heroAttack << " damage to the monster. \n";
        this->monsterHealth -= hero.heroAttack;
        if (this->monsterHealth < 1) {
            continue;
        }
        cout << this->monsterName << " health: " << this->monsterHealth << endl;

        // Player can pick whether to block or dodge.
        // Both have different outcomes.
        validResponse = false;
        while (validResponse == false) {
            validResponse = true;
            cout << "Do you want to block or dodge the next attack? \n(block/dodge) \n";
            cin >> response;
            if (response == "dodge") {
                chance = NumbersForDodging[randomNumberGenerator(0, NumbersForDodging.size())];
                if (chance == 1) {
                    cout << "You have dodged the attack. \n";
                } else if (chance == 0) {
                    cout << "You have failed to dodge the attack. \n";
                    cout << this->monsterName << " inflicts " << this->monsterAttack << " damage to you. \n";
                    hero.heroHealth -= this->monsterAttack;
                }
            } else if (response == "block") {
                chance = NumbersForBlocking[randomNumberGenerator(0, NumbersForBlocking.size())];
                if (chance == 1) {
                    cout << "You have blocked the attack. \n";
                } else if (chance == 0) {
                    cout << "You have failed to block the attack. \n";
                    cout << this->monsterName << " inflicts " << this->monsterAttack << " damage to you. \n";
                    hero.heroHealth -= this->monsterAttack;
                }
            } else {
                cout << "Invalid response, try again. \n";
                validResponse = false;
            }
        }
        // Checks hero health after each attack.
        // Ends game if hero health is zero.
        if (hero.heroHealth < 1) {
            cout << "Your health has been reduced to zero. \n";
            cout << "You have died. \n";
            exit(0);
        }
        cout << "Your health: " << hero.heroHealth << endl;
    }
    cout << "You have killed the " << this->monsterName << endl;
}