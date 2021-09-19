package Java;

import java.util.Random;
import java.util.Scanner;

class Monster {
    /**
    Defines the monsters.
    Takes the Name, Health and Attack of the monster as inputs.
    Description outputs the monsters stats.
    The fight method runs the code for the fight scene.

    Class Variables:
        NumbersForBlocking = Stores a list of numbers which are 
                             used to determine the probability 
                             of blocking an attack.
        
        NumbersForDodging = Stores a list of numbers which are 
                            used to determine the probability 
                            of dodging an attack.
        
        MonsterNamesList = Stores a list of names for the monsters.

        RandomNumber = Generates a random number when needed.
    
    Attributes:
        MonsterName = Stores the name of the monster.

        MonsterHealth = Stores the health of the monster.

        MonsterAttack = Stores the attack of the monster.
    
    Methods:
        Monster = Initialises the object with input variables.

        description = Prints the stats of the monster.

        fight = Performs the fight scene.
    */
    public String monsterName;
    private int monsterHealth;
    private int monsterAttack;
    private Random RandomNumber = new Random();
    private String[] MonsterNames = {"Troll", "Giant Lizard", "Weeping Angel", 
                                     "Bear", "Spider", "Skeleton", "Rat", 
                                     "Baby Dragon", "Snake", "Zombie"};
    private int[] NumbersForBlocking = {0, 0, 0, 1, 1, 1};
    private int[] NumbersForDodging = {0, 1, 1};



    Monster() {
        this.monsterName = MonsterNames[RandomNumber.nextInt(MonsterNames.length)];
        this.monsterHealth = 20 + RandomNumber.nextInt(76);
        this.monsterAttack = 5 + RandomNumber.nextInt(36);
    }



    Monster(String MonsterName, int MonsterHealth, int MonsterAttack) {
        this.monsterName = MonsterName;
        this.monsterHealth = MonsterHealth;
        this.monsterAttack = MonsterAttack;
    }



    public void description() {
        /**
        Prints the stats of the monster.
        */
        System.out.println(this.monsterName + " --- Health: " + this.monsterHealth +
                           ", Attack: " + this.monsterAttack);
    }



    public void fight(Hero hero, Scanner scn) {
        /**
        Performs the code for the fight scene.
        Player can choose to block or dodge attacks from the monster. 
        Random probability of of either decision being successful.

        Parameters:
            hero = Uses the character object to perform the fight 
                   scene.
            
            scn = Passes in the scanner.
        
        Variables:
            response = Stores the response of the player for whether they 
                       want to dodge or block the attack.
            
            chance = Stores the value that is picked from the 
                     NumbersForBlocking and NumbersForDodging list, 
                     and executes the corresponding code.
            
            validResponse = Stores whether a valid response was entered.
        */
        boolean validResponse;
        int chance;
        String response;
        System.out.println("You must fight the " + this.monsterName);
        System.out.println("You attack first.");

        // Loops as long as the monster is alive.
        while (this.monsterHealth > 0) {
            System.out.println("You inflicted " + hero.heroAttack + " damage to the monster.");
            this.monsterHealth -= hero.heroAttack;
            if (this.monsterHealth < 1) {
                continue;
            }
            System.out.println(this.monsterName + " health: " + this.monsterHealth);

            // Player can pick whether to block or dodge.
            // Both have different outcomes.
            validResponse = false;
            while (validResponse == false) {
                validResponse = true;
                System.out.println("Do you want to block or dodge the next attack? \r\n(block/dodge)");
                response = scn.nextLine();
                if (response.equals("dodge")) {
                    chance = NumbersForDodging[RandomNumber.nextInt(NumbersForDodging.length)];
                    if (chance == 1) {
                        System.out.println("You have dodged the attack.");
                    } else if (chance == 0) {
                        System.out.println("You have failed to dodge the attack.");
                        System.out.println(this.monsterName + " inflicts " + this.monsterAttack + " damage to you.");
                        hero.heroHealth -= this.monsterAttack;
                    }
                } else if (response.equals("block")) {
                    chance = NumbersForBlocking[RandomNumber.nextInt(NumbersForBlocking.length)];
                    if (chance == 1) {
                        System.out.println("You have blocked the attack.");
                    } else if (chance == 0) {
                        System.out.println("You have failed to block the attack.");
                        System.out.println(this.monsterName + " inflicts " + this.monsterAttack + " damage to you.");
                        hero.heroHealth -= this.monsterAttack;
                    }
                } else {
                    System.out.println("Invalid response, try again.");
                    validResponse = false;
                }
            }
            // Checks hero health after each attack.
            // Ends game if hero health is zero.
            if (hero.heroHealth < 1) {
                System.out.println("Your health has been reduced to zero.");
                System.out.println("You have died.");
                System.exit(0);
            }
            System.out.println("Your health: " + hero.heroHealth);
        }
        System.out.println("You have killed the " + this.monsterName);
    }
}