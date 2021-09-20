#include<iostream>
using namespace std;

#ifndef HEROCLASS_H
#define HEROCLASS_H

class Hero {
    /*
    Defines Hero's Attributes.
    Name, Health and Attack are the attributes of the class.
    Description method outputs the stats of the hero.

    Attributes:
        HeroName = Defines the name of the hero.

        HeroHealth = Defines the health of the hero.

        HeroAttack = Defines the attack of the hero.
    
    Methods:
        Hero = Defines the initial attributes as variables.

        description = Displays the hero's stats.
    */
    
    public:
        string heroName;
        int heroAttack;
        int heroHealth;

        Hero(string HeroName, int HeroHealth, int HeroAttack);

        void description();
};

#endif