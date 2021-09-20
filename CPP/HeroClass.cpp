#include<iostream>
#include "HeroClass.h"
using namespace std;

Hero::Hero() {}

Hero::Hero(string HeroName, int HeroHealth, int HeroAttack) {
    this->heroName = HeroName;
    this->heroHealth = HeroHealth;
    this->heroAttack = HeroAttack;
}



void Hero::description() {
    /*
    Prints the stats of the hero.
    */
    cout << "Name: " << this->heroName << ", Health: " << this->heroHealth << 
            ", Attack: " << this->heroAttack << endl;
}