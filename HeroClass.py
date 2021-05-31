class Hero:
    """
    Defines Hero's Attributes.
    Name, Health and Attack are the attributes of the class.
    __str__ method outputs the stats of the hero.

    Attributes:
        HName = Defines the name of the hero.

        HHealth = Defines the health of the hero.

        HAttack = Defines the attack of the hero.
    
    Methods:
        __init__ = Defines the initial attributes as variables.

        __str__ = Displays the hero's stats.
    """


    
    def __init__(self, HName, HHealth, HAttack):
        """
        Defines the intial variables of the object from the attributes 
        that are passed into the class.

        Variables:
            self.hname = Defines the hero's name.

            self.hhealth = Defines the hero's health.

            self.hattack = Defines the hero's attack.
        """
        self.hname = HName
        self.hhealth = HHealth
        self.hattack = HAttack
        

    
    def __str__(self):
        """
        Returns the stats of the hero.
        """
        return f"Name: {self.hname}, Health: {self.hhealth}, Attack: {self.hattack}"