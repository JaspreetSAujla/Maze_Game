class Hero:
    """
    Defines Hero's Attributes.
    Name, Health and Attack are the attributes of the class.
    __str__ method outputs the stats of the hero.

    Attributes:
        HeroName = Defines the name of the hero.

        HeroHealth = Defines the health of the hero.

        HeroAttack = Defines the attack of the hero.
    
    Methods:
        __init__ = Defines the initial attributes as variables.

        __str__ = Displays the hero's stats.
    """


    
    def __init__(self, HeroName, HeroHealth, HAttack):
        """
        Defines the intial variables of the object from the attributes 
        that are passed into the class.

        Variables:
            self.hero_name = Defines the hero's name.

            self.hero_health = Defines the hero's health.

            self.hero_attack = Defines the hero's attack.
        """
        self.hero_name = HeroName
        self.hero_health = HeroHealth
        self.hero_attack = HAttack
        

    
    def __str__(self):
        """
        Returns the stats of the hero.
        """
        return f"Name: {self.hero_name}, Health: {self.hero_health}, Attack: {self.hero_attack}"