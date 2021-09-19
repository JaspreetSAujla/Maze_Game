package Java;

import java.util.Random;
import java.util.Scanner;

class Room {
    /**
    Defines the rooms as they get appended to the room list.
    The class will create the correct number of monster and chest objects.
    This depends on the values in the __init__ method.
    The __str__ method outputs what is in the room.
    The run_room method runs the code for the actions taken within the room.

    Class Variables:
        RandomNumber = Generates random numbers.

    Methods:
        Room = Initialises the variables.

        description = Prints what is in the room.

        runRoom = Runs the code for the room.

        bossBattle = Runs the code for the boss battle.
    */
    private Random RandomNumber = new Random();
    private int numberOfMonsters;
    private int numberOfChests;
    private Monster monster1;
    private Monster monster2;
    private Chest chest1;
    private Chest chest2;



    Room() {
        /**
        Defines the variables when the class is initialised.
        Defines the correct number of monsters and chests.
        
        Variables:
            this.numberOfMonsters = Stores how many monsters are 
                                    in the room.
            
            this.numberOfChests = Stores how many chests are in 
                                  the room.
            
            this.monster1/2 = Defines a monster.

            this.chest1/2 = Defines a chest.
        */
        this.numberOfMonsters = RandomNumber.nextInt(2);
        this.numberOfChests = RandomNumber.nextInt(2);

        if (this.numberOfMonsters == 2) {
            this.monster1 = new Monster();
            this.monster2 = new Monster();
        } else if (this.numberOfMonsters == 1) {
            this.monster1 = new Monster();
        }
        if (this.numberOfChests == 2) {
            this.chest1 = new Chest();
            this.chest2 = new Chest();
        } else if (this.numberOfChests == 1) {
            this.chest1 = new Chest();
        }
    }



    public void description() {
        /**
        Prints what is in the room.
        */
        if (this.numberOfMonsters == 2) {
            System.out.println("There is a " + this.monster1.monsterName + " in the room.");
            System.out.println("There is a " + this.monster2.monsterName + " in the room.");
        } else if (this.numberOfMonsters == 1) {
            System.out.println("There is a " + this.monster1.monsterName + " in the room.");
        }
        if (this.numberOfChests == 2) {
            System.out.println("There are 2 chests in this room.");
        } else if (this.numberOfChests == 1) {
            System.out.println("There is a chest in this room.");
        }
    }



    public void runRoom(Hero hero, Scanner scn) {
        /**
        Runs the code for when the player is in a room.
        Checks to see if there are any monsters and chests, 
        and performs the appropriate code.

        Parameters:
            hero = Passes in the player so the attributes 
                   can be accessed.
        */
        if (this.numberOfMonsters == 2) {
            this.monster1.description();
            this.monster1.fight(hero, scn);
            this.monster2.description();
            this.monster2.fight(hero, scn);
        } else if (this.numberOfMonsters == 1) {
            this.monster1.description();
            this.monster1.fight(hero, scn);
        } else {
            System.out.println("There are no monsters in the room.");
        }
        if (this.numberOfChests == 2) {
            this.chest1.open(hero, scn);
            this.chest2.open(hero, scn);
        } else if (this.numberOfChests == 1) {
            this.chest1.open(hero, scn);
        } else {
            System.out.println("There are no chests in this room.");
        }
    }



    public void bossBattle(Hero hero, Scanner scn) {
        /**
        This function runs the final boss battle.
        Once the player reaches the final room, they must fight the boss.
        Takes the Character as a parameter.
        Two lists have been defined for the monster attack and health.
        A new monster object is defined and the fight function is run.

        Parameters:
            hero = Passes in the player so the attributes can be used.

            scn = Passes in the scanner.
        
        Variables:            
            dragon = Defines the boss.
        */
        Monster dragon = new Monster("Giant Dragon", 
                                     150 + RandomNumber.nextInt(151), 
                                     30 + RandomNumber.nextInt(61));
        System.out.println("You enter the room and see a Giant Dragon.");
        System.out.println("You can see the exit behind it.");
        System.out.println("You nust fight the dragon to escape.");
        dragon.description();
        dragon.fight(hero, scn);        
    }
}
