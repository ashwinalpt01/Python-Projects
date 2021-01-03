#------------------------------------------Description-----------------------------------------------------------
# In this Tic Tac Toe, the User always plays as 'X' and the Computer as 'O'
# This is an Unbeatable Tic Tac Toe Game which means the User cannot win at all
# The Best Result a User can get is a Tie meaning the Results possible are either "User Lost" or "Game Tied"
# Decription about what each function does is given above the Fucntion Definition as Comments.
#----------------------------------------------------------------------------------------------------------------


# Variable to Check if the Game is still continuing
# Initially its value is True but keeps checking after every move where its value has turned False

game_on = True

# Initialises the Variable 'grid' as list with 9 '-'s

grid = ['-'] * 9

# Function to show the grid initially and after every move

def showgrid():                          
    print(grid[0] + " | " + grid[1] + " | " + grid[2] + "      1 | 2 | 3")          
    print(grid[3] + " | " + grid[4] + " | " + grid[5] + "      4 | 5 | 6")
    print(grid[6] + " | " + grid[7] + " | " + grid[8] + "      7 | 8 | 9")

# Function to play the first turn of the computer as 'O'

def first_o_turn():
    print("\nMy(O's) Turn\n")
    if n == '5':
        grid[2] = 'O'
    else:
        grid[4] = 'O'
    showgrid()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~")

# Function to insert 'O' if there are two 'X's present in a row so that it prevents win of the User

def row_check():
    for j in range(0,7,3):
        k = 0
        for i in range(j, j+3):
            if (grid[i] == 'X'):
                k = k + 1
        if k == 2:
            for i in range(j, j+3):
                if (grid[i] == '-'):
                    grid[i] = 'O'
                    return 2
                else:
                    k = 0
        else:
            k = 0

# Function to insert 'O' if there are two 'X's present in a Column so that it prevents win of the User

def col_check():
    for j in range(0, 3):
        k = 0
        for i in range(j, j + 7, 3):
            if (grid[i] == 'X'):
                k = k + 1
        if k == 2:
            for i in range(j, j + 7, 3):
                if (grid[i] == '-'):
                    grid[i] = 'O'
                    return 2
                else:
                    k = 0
        else:
            k = 0

# Function to insert 'O' if there are two 'X's present in a Diagonal so that it prevents win of the User

def diag_check():
    for j in range(0,3,2):
        k = 0
        for i in range(j, 9-j, 4-j):
            if (grid[i] == 'X'):
                k = k + 1
        if k == 2:

            for i in range(0, 9-j, 4-j):
                if (grid[i] == '-'):
                    grid[i] = 'O'

                    return 2
                else:
                    k = 0
        else:
            k = 0

# Function to Check whether the User or Computer have won the game row wise

def row_win():
    for i in range(0, 7, 3):
        if grid[i] == grid[i + 1] == grid[i + 2] == 'X' or grid[i] == grid[i + 1] == grid[i + 2] == 'O':
            if grid[i] == 'X':
                print("\n!!!!!! You(X) WON !!!!!!")
                return 1
            else:
                print("\n!!!!!! You(X) LOST !!!!!!")
                return 1
    return 0

# Function to Check whether the User or Computer have won the game column wise

def col_win():
    for i in range(0, 3):
        if grid[i] == grid[i + 3] == grid[i + 6] == 'X' or grid[i] == grid[i + 3] == grid[i + 6] == 'O':
            if grid[i] == 'X':
                print("\n!!!!!! You(X) WON !!!!!!")
                return 1
            else:
                print("\n!!!!!! You(X) LOST !!!!!!")
                return 1

    return 0

# Function to Check whether the User or Computer have won the game diagonal wise

def diag_win():
    if grid[0] == grid[4] == grid[8] == 'X' or grid[0] == grid[4] == grid[8] == 'O':
        if grid[0] == 'X':
            print("\n!!!!!! You(X) WON !!!!!!")
            return 1
        else:
            print("\n!!!!!! You(X) LOST !!!!!!")
            return 1
    elif grid[2] == grid[4] == grid[6] == 'X' or grid[2] == grid[4] == grid[6] == 'O':
        if grid[2] == 'X':
            print("\n!!!!!! You(X) WON !!!!!!")
            return 1
        else:
            print("\n!!!!!! You(X) LOST !!!!!!")
            return 1
    else:
        return 0

# Function to Check if the Game has ended in a Tie

def game_tie(s):
    if "-" not in grid:
        if s == 1:
            return
        elif s == 0:
            print("\n!!!!!! Game TIED !!!!!!")
            return False
    else:
        return True

# Function to insert 'O' if there are two 'O's present in a row so that it results in the win of the Computer

def o_win_row():
    for j in range(0, 7, 3):
        m = 0
        for i in range(j, j + 3):
            if (grid[i] == 'O'):
                m = m + 1
        if m == 2:
            for i in range(j, j + 3):
                if (grid[i] == '-'):
                    grid[i] = 'O'
                    return 2
                else:
                    m = 0
        else:
            m = 0

# Function to insert 'O' if there are two 'O's present in a column so that it results in the win of the Computer

def o_win_col():
    for j in range(0, 3):
        m = 0
        for i in range(j, j + 7, 3):
            if (grid[i] == 'O'):
                m = m + 1
        if m == 2:
            for i in range(j, j + 7, 3):
                if (grid[i] == '-'):
                    grid[i] = 'O'
                    return 2
                else:
                    m = 0
        else:
            m = 0

# Function to insert 'O' if there are two 'O's present in a diagonal so that it results in the win of the Computer

def o_win_diag():
    for j in range(0, 3, 2):
        m = 0
        for i in range(j, 9 - j, 4 - j):
            if (grid[i] == 'O'):
                m = m + 1
        if m == 2:
            for i in range(j, 9 - j, 4 - j):
                if (grid[i] == '-'):
                    grid[i] = 'O'
                    return 2
                else:
                    m = 0
        else:
            m = 0

# Function to Decide the Appropriate Result of the Game

def res():
    s = [0] * 4
    s[0] = row_win()
    if s[0] == 1:
        return False
    elif s[0] == 0:
        s[1] = col_win()
        if s[1] == 1:
            return False
        elif s[1] == 0:
            s[2] = diag_win()
            if s[2] == 1:
                return False
            elif s[2] == 0:
                s[3] = game_tie(0)
                return s[3]

# Function to Let the User take his turn avoiding all the Invalid and Illogical User Inputs 

def x_turn():
    global game_on
    print("\nYour(X's) Turn\n")
    global n
    n = input("Select a Position from 1 to 9 : ")
    inp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if int(n) not in inp_list:
        while int(n) not in inp_list:
            print("Invalid Entry\n")
            n = input("Select a Position from 1 to 9 : ")
            if int(n) not in inp_list:
                continue
            while grid[int(n) - 1] != '-':
                print("Invalid Entry\nSelected Position Already Taken\n")
                n = input("Select a Position from 1 to 9 : ")
                if int(n) not in inp_list:
                    break
    elif grid[int(n) - 1] != '-':
        while grid[int(n) - 1] != '-':
            print("Invalid Entry\nSelected Position Already Taken\n")
            n = input("Select a Position from 1 to 9 : ")
            if int(n) <= 9:
                if grid[int(n) - 1] != '-':
                    continue
            while int(n) not in inp_list:
                print("Invalid Entry\n")
                n = input("Select a Position from 1 to 9 : ")
                if int(n) not in inp_list:
                    break
    grid[(int(n) - 1)] = 'X'
    print("\n")
    showgrid()
    print("\n------------------------")
    game_on = res()

# Function to play the turn of the Computer

def o_turn():
    global game_on
    print("\nMy(O's) Turn\n")
    m = [0] * 3
    l = [0] * 3
    m[0] = o_win_row()
    m[1] = o_win_col()
    m[2] = o_win_diag()
    if 2 not in m:
        l[0] = row_check()
        l[1] = col_check()
        l[2] = diag_check()
    if 2 not in m and 2 not in l:
        if grid[4] == 'O':
            if grid[1] == '-':
                grid[1] = 'O'
            elif grid[3] == '-':
                grid[3] = 'O'
            elif grid[5] == '-':
                grid[5] = 'O'
            elif grid[7] == '-':
                grid[7] = 'O'
        else:
            grid[8] = 'O'
    showgrid()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
    game_on = res()

# Calling the Functions in the required order so as to execute the Game Correctly

showgrid()
print("\nYou will play as X")
while game_on:
    x_turn()
    if game_on == False:
        break

    if 'O' not in grid:
        first_o_turn()
    else:
        o_turn()
        if game_on == False:
            break