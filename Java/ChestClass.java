package Java;

import java.util.Random;
import java.util.Scanner;

class Chest {
    /**
    Class which defines chests.
    Takes the number of weapons and number of armour as inputs.
    Randomly chooses which item to give and assigns a value to it.
    Has a method which allows the player to open a chest.

    Class Variables:        
        WeaponsList = Stores a string list of random weapons.

        ArmourList = Stores a string list of random bits of armour.

        RandomNumber = Initialises random so that random numbers can 
                       be generated.

    Methods:
        Chest = Defines the initial variables using the attributes.

        open = Runs the code for when the player wants to open the chest.
    */
    private String[] WeaponsList = {"a Sword", "a Hammer", "a Knife", "a Dagger", 
                                    "an Axe", "a Trident"};
    private String[] ArmourList = {"Helmet", "Vest", "Chest Plate", "Shield", 
                                   "pair of Boots", "bit of mesh"};
    private Random RandomNumber = new Random();
    private int numberOfWeapons;
    private int numberOfArmour;
    private int weaponPoints;
    private int armourPoints;
    

    
    Chest() {
        /**
        Defines the initial variables using the attributes passed into the 
        class.

        Variables:
            this.number_of_weapons = Defines how many weapons can be 
                                     found in the chest.

            this.number_of_armour = Defines how many pieces of armour 
                                    can be found in the chest.

            this.weapon_points = Stores the attack points of the weapon.

            this.armour_points = Stores the health points of the armour.
        */
        // Picks random number of weapons and armour between 0 and 1.
        this.numberOfWeapons = RandomNumber.nextInt(2);
        this.numberOfArmour = RandomNumber.nextInt(2);

        // Assign points to weapons.
        if (this.numberOfWeapons == 1) {
            this.weaponPoints = RandomNumber.nextInt(22);
        }
        if (this.numberOfArmour == 1) {
            this.armourPoints = RandomNumber.nextInt(22);
        }
    }



    public void open(Hero hero, Scanner scn) {
        /**
        Tells the code what to do when a player encounters a chest.
        Player can either open the chest or choose to ignore it.

        Parameters:
            hero = Passes in the player so that its attributes 
                   can be accessed.
            
            scn = Passes in the scanner.

        Variables:
            response = Stores the response of the player. Tells the code 
                       if the player wants to open a chest or not.
            
            validResponse = Stores whether the response was valid.
        */
        boolean validResponse = false;
        while (validResponse == false) {
            validResponse = true;
            System.out.println("There is a chest here, would you like to open it? \r\n(yes/no)");
            String response = scn.nextLine();

            if (response.equals("yes")) {
                if (this.numberOfWeapons == 1) {
                    System.out.println("You have found " + WeaponsList[RandomNumber.nextInt(WeaponsList.length)]);
                    System.out.println("Adding " + this.weaponPoints + " to your attack points.");
                    hero.heroAttack += this.weaponPoints;
                    hero.description();
                }
                if (this.numberOfArmour == 1) {
                    System.out.println("You have found a " + ArmourList[RandomNumber.nextInt(ArmourList.length)]);
                    System.out.println("Adding " + this.armourPoints + " to your health points.");
                    hero.heroHealth += this.armourPoints;
                    hero.description();
                }
                if (this.numberOfArmour == 0 && this.numberOfWeapons == 0) {
                    System.out.println("This chest is empty.");
                }
            } else if (response.equals("no")) {
                System.out.println("You choose not to open the chest.");
            } else {
                System.out.println("invalid response, try again.");
                validResponse = false;
            }
        }
    }
}