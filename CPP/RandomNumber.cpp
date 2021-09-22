#include<iostream>
#include<ctime>
#include<cstdlib>
#include "RandomNumber.h"
using namespace std;

int randomNumberGenerator(int startNumber, int endNumber) {
    /*
    Takes a start number (inclusive) and an end number (exclusive), 
    and returns a random number within that range.

    Parameters:
        startNumber = Takes in the start number (inclusive).

        endNumber = Takes the end number (exclusive).
    
    Variables:
        randomNumber = Stores the random number.
    */
    srand(time(0));
    int randomNumber = startNumber + (rand() % (endNumber - startNumber));
    return randomNumber;
}