#include<iostream>
#include "MazeGame.h"
#include "HeroClass.h"
#include "RoomClass.h"
#include "RandomNumber.cpp"
using namespace std;

MazeGame::MazeGame() {
    this->maximumRooms = randomNumber(3, 11);
    introduceGame();
}



MazeGame::MazeGame(int MaximumRooms) {
    this->maximumRooms = MaximumRooms;
    introduceGame();
}



void MazeGame::introduceGame() {
    /*
    Introduces the game and allows player to pick a hero.
        
    Variables:
        validResponse = Stores whether the player entered 
                        a valid response or not.
            
        response = Stores the players response for which hero 
                   they want.
    */
    bool validResponse = false;
    string response;

    cout << "Welcome contender. \n";
    cout << "You have accepted the challenge of trying to cross this maze of rooms. \n";
    cout << "But will you be able to make it out?... \n";
    cout << "Each room will have it's own obstacles to cross, and every room will be randomely generated. \n";
    cout << "Let us see if you can make it out... \n";
    cout << "Here are your character choices: \n";
    Steve.description();
    Alex.description();
    Chloe.description();

    // Allows player to pick a hero.
    while (validResponse == false) {
        validResponse = true;
        cout << "Pick your character: \n(steve/alex/chloe) \n";
        cin >> response;
        if (response == "steve") {
            this->hero = Steve;
        } else if (response == "alex") {
            this->hero = Alex;
        } else if (response == "chloe") {
            this->hero = Chloe;
        } else {
            cout << "Invalid response, try again. \n";
            validResponse = false;
        }
    }
    cout << "You have chosen:  \n";
    this->hero.description();
}



void MazeGame::runGame() {
    /*
    Runs the code for the game.
    Loops through till the maximum number of rooms is reached.
        
    Variables:
        currentRoom = Stores the current room object.
            
        currentRoomNumber = Stores the current room number. 
                            Used as a counter in the while loop.
    */
    int currentRoomNumber = 0;
    Room currentRoom = Room();
    cout << "Now you are ready to enter the first room, good luck. \n";

    // Loops over for the number of loops there are.
    while (currentRoomNumber < this->maximumRooms) {
        currentRoom = Room();
        currentRoom.description();
        currentRoom.runRoom(this->hero);
        cout << "There are 3 doors you can go through, left, right and forward. \n";
        cout << "Which door do you go through? \n(left/right/forward) \n";
        cin;
        currentRoomNumber += 1;
    }
    currentRoom.bossBattle(this->hero);
    cout << "Well done, you made it out. \n";
    cout << "Your character's stats are: \n";
    this->hero.description();
}