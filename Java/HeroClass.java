package Java;

class Hero {
    /**
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
    public String heroName;
    public int heroHealth;
    public int heroAttack;



    Hero(String HeroName, int HeroHealth, int HeroAttack) {
        /**
        Defines the intial variables of the object from the attributes 
        that are passed into the class.

        Variables:
            thsi.hero_name = Defines the hero's name.

            this.hero_health = Defines the hero's health.

            this.hero_attack = Defines the hero's attack.
        */
        this.heroName = HeroName;
        this.heroHealth = HeroHealth;
        this.heroAttack = HeroAttack;
    }



    public void description() {
        /**
        Prints the stats of the hero.
        */
        System.out.println("Name: " + this.heroName + ", Health: " + this.heroHealth + 
                           ", Attack: " + this.heroAttack);
    }
}