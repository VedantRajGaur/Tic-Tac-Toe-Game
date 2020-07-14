print("Tic-Tac-Toe GAME")


#Assigning values to the matrix
#  1 | 2 | 3
#  4 | 5 | 6
#  7 | 8 | 9
TTT = ['o', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Lets assign 1 to the player
player = 1

#Prints the matrix after each turn
def PrintGrid():
    print("Player 1: O\tvs\tPlayer 2: X");
    print("     |     |     ");
    print("  " + TTT[1] + "  |  " + TTT[2] + "  |  " + TTT[3] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TTT[4] + "  |  " + TTT[5]+"  |  " + TTT[6] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TTT[7] + "  |  " + TTT[8]+"  |  " + TTT[9] + "  ")
    print("     |     |     ");

def Check():
    #Check First Row
    if((TTT[1] == TTT[2]) and (TTT[2] == TTT[3])):
        return 1
    #Check First Column
    elif((TTT[1] == TTT[4]) and (TTT[4] == TTT[7])):
        return 1

    elif((TTT[1] == TTT[5]) and (TTT[5] == TTT[9])):
        return 1

    elif((TTT[2] == TTT[5]) and (TTT[5] == TTT[8])):
        return 1

    elif((TTT[3] == TTT[6]) and (TTT[6] == TTT[9])):
        return 1

    elif((TTT[3] == TTT[5]) and (TTT[5] == TTT[7])):
        return 1

    elif((TTT[4] == TTT[5]) and (TTT[5] == TTT[6])):
        return 1

    elif((TTT[7] == TTT[8]) and (TTT[8] == TTT[9])):
        return 1

  #Check Condition of a tie
    elif(TTT[1] != '1' and TTT[2] != '2' and TTT[3] != '3' and TTT[4] != '4' and TTT[5] != '5'
    and TTT[6] != '6' and TTT[7] != '7' and TTT[8] != '8' and TTT[9] != '9'):
            return 0

  #Return -1 if there's a tie
    else:
        return -1



#MAIN FUNCTION
player = player % 2 #Player number changes after each turn
#i is a value returned by Check() function that determines whether the game is over or still incomplete
i = -1
while i == -1:
    PrintGrid()
    if player % 2:
        player = 1
    else:
        player = 2
    #Takes input from the user to fill in the grid
    print("player ", end="")
    print(player, end="")
    choice = int(input(", enter a number: "))

    mark = player
    if player == 1:
        mark = 'O'
    else:
        mark = 'X'
    print(choice)
    #Checks if the grid element is already filled or not. If not, fills it as user desired.
    if (choice == 1 and TTT[1] == '1'):
        TTT[1] = mark

    elif(choice == 2 and TTT[2] == '2'):
        TTT[2] = mark

    elif(choice == 3 and TTT[3] == '3'):
        TTT[3] = mark

    elif(choice == 4 and TTT[4] == '4'):
        TTT[4] = mark

    elif(choice == 5 and TTT[5] == '5'):
        TTT[5] = mark

    elif(choice == 6 and TTT[6] == '6'):
        TTT[6] = mark

    elif(choice == 7 and TTT[7] == '7'):
        TTT[7] = mark

    elif(choice == 8 and TTT[8] == '8'):
        TTT[8] = mark

    elif(choice == 9 and TTT[9] == '9'):
        TTT[9] = mark
    else:
        print("Invalid Input")
        player = player - 1

    #increase the number of player for next turn
    player = player + 1
    i = Check()
#Prints the grid finally
PrintGrid()

#If I was returned as 1 from Check() function:
if(i == 1):
    print("Player ", end="")
    print(player-1, end="")
    print(" won!", end="")
else: #Otherwise, it's a tie
    print("It's a Tie")
