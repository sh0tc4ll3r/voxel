# David Lorenzo - Voxel OA for "Software Apprentice" - Snakes and ladders

Kata made for the online coding assignment with Voxel.

## Notes

- To run the program, clone the repository and run game.py from either your console or your IDE, no external libraries are needed.
- The program will automatically play out a full game of a player until the player wins. Ideally this should be expanded giving the player the opportunity to enter their name and also to add multiple players, otherwise the game itself isn't much of a game apart from checking how little turns you manage to need to win.
- I have preemptively parametrized parts like the board size, the positions of the snakes and ladders and such so that the game is open to expansions on that end. As previously mentioned, multiplayer should be the next immediate step I believe and if the board is big enough maybe either multiple dices or increase dice size to make the game faster.
- Tests have been made using the unittest library, I would recommend running them with the '-b' option to make it much clearer to read, otherwise the print statements shown during the game will clutter the test results.
