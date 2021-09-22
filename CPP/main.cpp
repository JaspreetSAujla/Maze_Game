#include<iostream>
#include "MazeGame.h"
#include "MazeGame.cpp"
#include "HeroClass.h"
#include "HeroClass.cpp"
#include "MonsterClass.h"
#include "MonsterClass.cpp"
#include "ChestClass.h"
#include "ChestClass.cpp"
#include "RoomClass.h"
#include "RoomClass.cpp"
#include "RandomNumber.h"
#include "RandomNumber.cpp"
using namespace std;

int main() {
    MazeGame mazeGame;
    mazeGame.runGame();
    return 0;
}