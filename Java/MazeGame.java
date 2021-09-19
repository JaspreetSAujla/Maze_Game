package Java;

import java.util.Random;
import java.util.Scanner;

public class MazeGame {
    /**
    Class used to initialise the maze game and run it.

    Attributes:
        MaximumRooms = Stores the maximum number of rooms 
                       the game will have.

    CLass Variables:
        Steve/Alex/Chloe = Three different heroes to choose from.

    Methods:
        MazeGame = Defines the initial variables of the game.

        introduceGame = Introduces the game and allows for hero 
                         to be chosen.

        runGame = Runs the game.
    */
    private int maximumRooms;
    private Hero Steve = new Hero("Steve", 80, 21);
    private Hero Alex = new Hero("Alex", 60, 30);
    private Hero Chloe = new Hero("Chloe", 100, 16);
    private Scanner scn;
    private Random RandomNumber = new Random();
    private Hero hero;



    MazeGame() {
        this.maximumRooms = 3 + RandomNumber.nextInt(11);
        this.scn = new Scanner(System.in);
        introduceGame();
    }



    MazeGame(int MaximumRooms) {
        this.maximumRooms = MaximumRooms;
        this.scn = new Scanner(System.in);
        introduceGame();
    }



    private void introduceGame() {
        /**
        Introduces the game and allows player to pick a hero.
        
        Variables:
            validResponse = Stores whether the player entered 
                             a valid response or not.
            
            response = Stores the players response for which hero 
                       they want.
        */
        boolean validResponse = false;
        String response;

        System.out.println("Welcome contender.");
        System.out.println("You have accepted the challenge of trying to cross this maze of rooms.");
        System.out.println("But will you be able to make it out?...");
        System.out.println("Each room will have it's own obstacles to cross, and every room will be randomely generated.");
        System.out.println("Let us see if you can make it out...");
        System.out.println("Here are your character choices:");
        Steve.description();
        Alex.description();
        Chloe.description();

        // Allows player to pick a hero.
        while (validResponse == false) {
            validResponse = true;
            System.out.println("Pick your character: \r\n(steve/alex/chloe)");
            response = this.scn.nextLine();
            if (response.equals("steve")) {
                this.hero = Steve;
            } else if (response.equals("alex")) {
                this.hero = Alex;
            } else if (response.equals("chloe")) {
                this.hero = Chloe;
            } else {
                System.out.println("Invalid response, try again.");
                validResponse = false;
            }
            System.out.println("You have chosen: ");
            this.hero.description();
        }
    }



    public void runGame() {
        /**
        Runs the code for the game.
        Loops through till the maximum number of rooms is reached.
        
        Variables:
            currentRoom = Stores the current room object.
            
            currentRoomNumber = Stores the current room number. 
                                Used as a counter in the while loop.
        */
        int currentRoomNumber = 0;
        Room currentRoom = new Room();
        System.out.println("Now you are ready to enter the first room, good luck.");

        // Loops over for the number of loops there are.
        while (currentRoomNumber < this.maximumRooms) {
            currentRoom = new Room();
            currentRoom.description();
            currentRoom.runRoom(this.hero, this.scn);
            System.out.println("There are 3 doors you can go through, left, right and forward.");
            System.out.println("Which door do you go through? \r\n(left/right/forward)");
            this.scn.nextLine();
            currentRoomNumber += 1;
        }
        currentRoom.bossBattle(this.hero, this.scn);
        System.out.println("Well done, you made it out.");
        System.out.println("Your character's stats are: ");
        this.hero.description();
    }
}
