"""
battleship.py - Extra Credit for Lower Midterm Score (Up to 5% Added)
=====

Write a simplified one player version of Battleship.  In this version of 
Battleship, the computer hides a ship in a 5 x 5 grid.  The player must find
the ship by inputting row and column pairs.  If the player finds the ship,
the player wins.  The player has unlimited turns!

1. The computer will generate a board of 5 x 5 o's:

o o o o o
o o o o o
o o o o o
o o o o o
o o o o o

2. The computer will also generate a random row and column for the location 
   of the ship.  The ship only occupies one "square" (unlike the regular 
   version of Battleship).

3. The player is then asked to input a row and then a column (both are 0-4),
   separated by a comma... for example: 1,2 means row 1, column 2
   a. If the input is just q, the game ends.
   b. If the input is invalid, allow an error to occur in your game (you 
      don't have to worry about invalid input)

4. The row and column input is either a hit or a miss.
   a. If the input uncovers the ship, the player wins and the game ends.
   b. If the input is a miss, the 'o' on the grid is replaced with " " (a 
      space) to keep track of squares that have already been missed.

5. After every turn, the board is printed out again.  See the output at the end
   of this comment for a sample game.

Partial credit will be given!

Hints:
-----
There are many ways to implement this program.  These hints are general guides 
to get started, but don't feel obligated to follow them.

* a list of lists is one way to represent the grid
* (see the lists in lists slide for help)
* both row and column input should not be 'q' for the game to continue
  assignment
* a while loop may be useful to keep the game going until the above
  condition is met
* for testing, it may help to start the ship at a fixed location
* the string method, split, may be helpful in extracting the row and column
  numbers from the user's input
* it may be useful to break down the program into separate functions (for example, creating the board, detecting a hit, etc.)



Sample Output:
-----

One player battleship!
====================

o o o o o
o o o o o
o o o o o
o o o o o
o o o o o
What row and column do you want to try? 
> 1,1


o o o o o
o   o o o
o o o o o
o o o o o
o o o o o
What row and column do you want to try?
> 2,3

The boat was at row 2 and column 3
YOU WON!!!!

o o o o o
o   o o o
o o o x o
o o o o o
o o o o o
"""

#Utkarsh Parasramka
#11/30/2015
#Section: 010

import random
print("One player battleship!\n====================\n")
board = [['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o']]
for item in board:
    board_ = ' '.join(item)
    print(board_)
row = random.randint(0,4)
column = random.randint(0,4)
def hit(row_,column_):
    if row == row_ and column == column_:
        board[row_][column_] = 'x'
    else:
        board[row_][column_] = ' '
    for item in board:
            board_ = ' '.join(item)
            print(board_)
answer = ''
while answer != 'q':
    answer = input('What row and column do you want to try?\n>')
    if answer == 'q':
        break
    answer_ = answer.split(',')
    hit(int(answer_[0]),int(answer_[1]))
    if int(answer_[0]) == row and int(answer_[1]) == column:
        print("The boat was at row", row, "and column", column)
        print("YOU WON!!!")
        break
