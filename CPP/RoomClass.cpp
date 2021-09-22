#include<iostream>
#include "RoomClass.h"
#include "HeroClass.h"
#include "MonsterClass.h"
#include "ChestClass.h"
#include "RandomNumber.h"
using namespace std;

Room::Room() {
    /*
    Defines the variables when the class is initialised.
    Defines the correct number of monsters and chests.
        
    Variables:
        this->numberOfMonsters = Stores how many monsters are 
                                in the room.
            
        this->numberOfChests = Stores how many chests are in 
                              the room.
            
        this->monster1/2 = Defines a monster.

        this->chest1/2 = Defines a chest.
    */
    this->numberOfMonsters = randomNumberGenerator(0, 2);
    this->numberOfChests = randomNumberGenerator(0, 2);

    if (this->numberOfMonsters == 2) {
        this->monster1 = Monster();
        this->monster2 = Monster();
    } else if (this->numberOfMonsters == 1) {
        this->monster1 = Monster();
    }
    if (this->numberOfChests == 2) {
        this->chest1 = Chest();
        this->chest2 = Chest();
    } else if (this->numberOfChests == 1) {
        this->chest1 = Chest();
    }
}



void Room::description() {
    /*
    Prints whats in the room.
    */
    if (this->numberOfMonsters == 2) {
        cout << "There is a " << this->monster1.monsterName << " in the room. \n";
        cout << "There is a " << this->monster2.monsterName << " in the room. \n";
    } else if (this->numberOfMonsters == 1) {
        cout << "There is a " << this->monster1.monsterName << " in the room. \n";
    }
    if (this->numberOfChests == 2) {
        cout << "There are 2 chests in this room. \n";
    } else if (this->numberOfChests == 1) {
        cout << "There is a chest in this room. \n";
    }
}



void Room::runRoom(Hero hero) {
    /*
    Runs the code for when the player is in a room.
    Checks to see if there are any monsters and chests, 
    and performs the appropriate code.

    Parameters:
        hero = Passes in the player so the attributes 
               can be accessed.
    */
    if (this->numberOfMonsters == 2) {
        this->monster1.description();
        this->monster1.fight(hero);
        this->monster2.description();
        this->monster2.fight(hero);
    } else if (this->numberOfMonsters == 1) {
        this->monster1.description();
        this->monster1.fight(hero);
    } else {
        cout << "There are no monsters in the room. \n";
    }
    if (this->numberOfChests == 2) {
        this->chest1.open(hero);
        this->chest2.open(hero);
    } else if (this->numberOfChests == 1) {
        this->chest1.open(hero);
    } else {
        cout << "There are no chests in this room. \n";
    }
}



void Room::bossBattle(Hero hero) {
    /*
    This function runs the final boss battle.
    Once the player reaches the final room, they must fight the boss.
    Takes the Character as a parameter.
    Two lists have been defined for the monster attack and health.
    A new monster object is defined and the fight function is run.

    Parameters:
        hero = Passes in the player so the attributes can be used.
        
    Variables:            
        dragon = Defines the boss.
    */
    Monster dragon = Monster("Giant Dragon", 
                             randomNumberGenerator(150, 251), 
                             randomNumberGenerator(30, 91));
    cout << "You enter the room and see a Giant Dragon. \n";
    cout << "You can see the exit behind it. \n";
    cout << "You nust fight the dragon to escape. \n";
    dragon.description();
    dragon.fight(hero);  
}