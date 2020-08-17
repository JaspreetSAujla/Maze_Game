# Maze_Game
A simple text-based maze game where you have to find your way out of the maze of rooms. Each room has different obstacles to overcome. There are also items to aid you through your quest.

# RunMe.py:
    This is the file that needs to be ran in order to play the game.
    Allows player to pick a character and introduces them to the game.
    The code calls functions from the Room class, which allows the player to encounter different things.

# RoomClass.py:
    Room class defines each room as it is made.
    Each room has a random number of monsters and chests and player has to clear each room.

# HeroClass.py:
    Hero class defines the heroes that the player can play as.
    Each hero has it's own health and attack.

# MonsterClass.py:
    Monster class defines the monsters in the game.
    When a room is generated, the monsters will also be generated at the same time.
    The monsters each have random health and attack and the player must defeat them in order to proceed.

# ChestClass.py:
    Chest class defines the chests in the game.
    When a room is generated, the chests will also be genereated at the same time.
    Each chest has random items inside of it, which can aid the player.
