## introduciton
Hi reader. Today Blod will present a step-by-step guide to creating a tic-tac-toe game using python!
You will find information about the Game, libraries and an explanation of the code.

## the Game
Tic-tac-toe is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

## Gameplay
Tic-tac-toe is played on a three-by-three grid by two players, alternately placing the marks X and O in one of the nine spaces in the grid.

In the following example, the first player (X) wins the Game in seven steps:

Game of Tic-tac-toe, won by X
There is no universally-agreed rule as to who plays first, but in this article, the convention that X plays first is used.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n5vrty146roiy13c9tsw.png)

## Breaking The Game into python code, taking into consideration the valuable information of the Game, it's appropriate to turn into data the structure of the Game. 
**The first step is creating a grid.** the grid is a 3x3 matrix (3 rows and 3 columns) composed of just `Integers` Values for each space inside the grid. 

> every empty space, 1 to 9, will be represented by `Integer` 0.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ul5mh1p9xq3p910cyu0i.jpg)

```
#        row_1   row_2   row_3
grid = [[0,0,0],[0,0,0],[0,0,0]]`
```
Each 0 will represent an empty space. Later, those zeros will be substituted by 1 for player One and 2 for player Two.

 **Second step. Define a function to display the grid**

#step One
let's define the function in this way.

```
def print_grid():
    print(grid[0])
    print(grid[1])
    print(grid[2])
```
` output:
[0, 0, 0]
[0, 0, 0]
[0, 0, 0].`

For a fancier look, the aspect of the grid in the console can be improved. 
The code can be changed in this way:

```
#lets create a dicitonary of simbols
grid_simbols = {
    0:'',
    1:'X',
    2:"O"
}

# then change the  print_grid() function
def print_grid():
    row_1 = [grid_simbols[i] for i in grid[0]]
    row_2 = [grid_simbols[i] for i in grid[1]]
    row_3 = [grid_simbols[i] for i in grid[2]]
    print(f'      1   2   3  columns \n1  r {row_1}\n2  o {row_2}\n3  w {row_3}')
```
`output: 
      1   2   3  columns
1  r ['X', '', '']
2  o ['', 'O', '']
3  w ['', '', '']
`

#Step two
now there is a need for player user input. The player must choose a row and a column using an integer value that will determine the desired position, which must be, at most, the grid size.
The function will take the player as a parameter that will be used to display who is the current player.

```
def user_input(player):
    row_valid = False
    column_valid = False
    player = player
    While not row_valid:
        row = input(f"{player} please Choose a row: ")
        if row.isnumeric() and int(row) < 4 and int(row) >=1:
            row_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    While not column_valid:
        column = input(f"{player} please Choose a column: ")
        if column.isnumeric() and int(column) < 4 and int(column) >=1:
            column_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    return (int(row),int(column))
```
`output:
Player One, please Choose a row: 
or
Player Two, please Choose a row: 
`


#step Three
create a function to check whether a position in the grid is already taken.

```
def check_grid(row,column):
    if grid[row][column] == 1 or grid[row][column] == 2:
        return False
    else: return True
```

#step four
let's create the main loop where we can actually play the Game.

```
def start_game():
    player_one_choose = True
    while True:
        print_grid()
        if player_one_choose:
            player_row,player_column = user_input("Player One")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 1
                clear()
                player_one_choose = False
            else:
                player_one_choose = True
                clear()
                print("The position is already taken")
        else:
            player_row,player_column = user_input("Player Two")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 2
                clear()
                player_one_choose = True
            else:
                player_one_choose = False
                clear()
                print("The position is already taken")
```
The Game is now playable, but there's one final step. The last function is to determine who will be the winner of the Game.

#step five
create a function to check the winner. Then implement the function inside the main loop of the Game.

```
def checkWinner(grid):
    for i in range(0,3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
            
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][0]

    elif 0 not in grid[0] and 0 not in grid[1] and 0 not in grid[2]:
        return 0
    else:
        return -1

def start_game():
    player_one_choose = True
    while True:
        print_grid()
        if player_one_choose:
            player_row,player_column = user_input("Player One")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 1
                clear()
                player_one_choose = False
            else:
                player_one_choose = True
                clear()
                print("The position is already taken")
        else:
            player_row,player_column = user_input("Player Two")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 2
                clear()
                player_one_choose = True
            else:
                player_one_choose = False
                clear()
                print("The position is already taken")
        if checkWinner(grid) == 1:
            print("X WON!")
            print_grid()
            break
        if checkWinner(grid) == 2:
            print("O WON!")
            print_grid()
            break

```

Great! Now you successfully create a fantastic tik-tac-toe game!

## full code

```
grid = [[0,0,0],[0,0,0],[0,0,0]]
import os
clear = lambda: os.system('cls')
clear()
grid_simbols = {
    0:'',
    1:'X',
    2:"O"
}

def start_game():
    player_one_choose = True
    while True:
        print_grid()
        if player_one_choose:
            player_row,player_column = user_input("Player One")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 1
                clear()
                player_one_choose = False
            else:
                player_one_choose = True
                clear()
                print("The position is already taken")
        else:
            player_row,player_column = user_input("Player Two")
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 2
                clear()
                player_one_choose = True
            else:
                player_one_choose = False
                clear()
                print("The position is already taken")
        if checkWinner(grid) == 1:
            print("X WON!")
            print_grid()
            break
        if checkWinner(grid) == 2:
            print("O WON!")
            print_grid()
            break
        
def user_input(player):
    row_valid = False
    column_valid = False
    player = player
    while not row_valid:
        row = input(f"{player} please Choose a row: ")
        if row.isnumeric() and int(row) < 4 and int(row) >=1:
            row_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    while not column_valid:
        column = input(f"{player} please Choose a column: ")
        if column.isnumeric() and int(column) < 4 and int(column) >=1:
            column_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    return (int(row),int(column))

def print_grid():
    row_1 = [grid_simbols[i] for i in grid[0]]
    row_2 = [grid_simbols[i] for i in grid[1]]
    row_3 = [grid_simbols[i] for i in grid[2]]
    print(f'      1   2   3  columns \n1  r {row_1}\n2  o {row_2}\n3  w {row_3}')



def check_grid(row,column):
    if grid[row][column] == 1 or grid[row][column] == 2:
        return False
    else: return True

def checkWinner(grid):
    for i in range(0,3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
            
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][0]

    elif 0 not in grid[0] and 0 not in grid[1] and 0 not in grid[2]:
        return 0
    else:
        return -1
