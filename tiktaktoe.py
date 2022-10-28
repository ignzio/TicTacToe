grid = [[0,0,0],[0,0,0],[0,0,0]]
import os
clear = lambda: os.system('cls')
clear()
grid_simbols = {
    0:'',
    1:'X',
    2:"O"
}

def print_grid():
    row_1 = [grid_simbols[i] for i in grid[0]]
    row_2 = [grid_simbols[i] for i in grid[1]]
    row_3 = [grid_simbols[i] for i in grid[2]]
    print(f'      1   2   3  columns \n1  r {row_1}\n2  o {row_2}\n3  w {row_3}')

def user_input():
    row_valid = False
    column_valid = False
    while not row_valid:
        row = input("Player One please Choose a row: ")
        if row.isnumeric() and int(row) < 4 and int(row) >=1:
            row_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    while not column_valid:
        column = input("Player One plase Choose a column: ")
        if column.isnumeric() and int(column) < 4 and int(column) >=1:
            column_valid = True
        else:print("Input invalid please choose a number from 1 to 3")
    return (int(row),int(column))

def check_grid(row,column):
    if grid[row][column] == 1 or grid[row][column] == 2:
        return False
    else: return True

def start_game():
    player_one_choose = True
    while True:
        print_grid()
        if player_one_choose:
            player_row,player_column = user_input()
            if check_grid(player_row - 1,player_column - 1):
                grid[player_row - 1][player_column - 1] = 1
                clear()
                player_one_choose = False
            else:
                player_one_choose = True
                clear()
                print("The position is already taken")
        else:
            player_row,player_column = user_input()
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
                
start_game()