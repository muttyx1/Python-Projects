import numpy as np
import random
from random import randint

class Game:
    mat = None
    rows = 0
    cols = 0
    turn = 0
    wins = 0


def display_board(game):
    print(np.flip(game.mat,0))  #   flips and then displays/prints the board so that [0,0] will be at the bottom left


def check_victory(game):
    player1svictory = False                         # bug fix the pop then
    player2svictory = False
    cond1ver = []                                   #   creates empty list of vertical consecutive discs for player 1
    cond2ver = []                                   #   creates empty list of vertical consecutive discs for player 2
    for c in range(game.cols):                      #   checks column by column
        cond1ver = []                               #   resets list when changing column
        cond2ver = []
        for r in range(game.rows):                  #   checks row by row by column
            if game.mat[r,c] == 1:                  #   if the coordinates in the matrix is a player disc,
                cond1ver.append(1)                  #   append to the respective vertical list
                cond2ver = []                       #   resets player 2's list to 0
                if len(cond1ver) == game.wins:      #   if the number of items in the list is == game.wins,
                    return 1                        #   player 1 victory
            elif game.mat[r,c] == 2:
                cond2ver.append(1)
                cond1ver = []
                if len(cond2ver) == game.wins:
                    return 2                        #   player 2 victory
            else:
                cond1ver = []                       #   reinitialize the list to make sure only consecutive discs will be appended
                cond2ver = []


    cond1hor = []                                   #   creates empty list of horizontal consecutive discs for player 1
    cond2hor = []                                   #   creates empty list of horizontal consecutive discs for player 2
    for r in range(game.rows):                      #   checks row by row
        cond1hor = []
        cond2hor = []
        for c in range(game.cols):                  #   checks column by column by row
            if game.mat[r,c] == 1:                  #   if the coordinates in the matrix is a player disc,
                cond1hor.append(1)                  #   append to the respective horizontal list
                cond2hor = []
                if len(cond1hor) == game.wins:      #   if the number of items in the horizontal list is ==  game.wins 
                    player1svictory = True          #   player 1 victory might be true
            elif game.mat[r,c] == 2:
                cond2hor.append(1)
                cond1hor = []
                if len(cond2hor) == game.wins:
                    player2svictory = True          #   player 2 victory might be true
            else:
                cond1hor = []                       #   reinitialize the list to make sure only consecutive discs will be appended
                cond2hor = []


    cond1posdia = []                                #   creates empty list of positive gradient diagonal consecutive discs for player 1 
    cond2posdia = []                                #   creates empty list of positive gradient diagonal consecutive discs for player 2
    for r in range(0,game.rows-1):                  #   this line and below goes through every coordinate in the matrix
        for c in range(0,game.cols-1):              #
            cond1posdia = []
            cond2posdia = []
            for i,j in zip((range(r,game.rows-1)),(range(c,game.cols-1))):  # checks diagonally / for every coordinate if the 2 values are ==
                if game.mat[i,j] == game.mat[i+1,j+1] and game.mat[i,j] == 1:
                    cond1posdia.append(1)
                    cond2posdia = []
                    if len(cond1posdia) == game.wins-1:
                        player1svictory = True
                elif game.mat[i,j] == game.mat[i+1,j+1] and game.mat[i,j] == 2:
                    cond2posdia.append(1)
                    cond1posdia = []
                    if len(cond2posdia) == game.wins-1:
                        player2svictory = True
                else:
                    cond1posdia = []
                    cond2posdia = []


    cond1negdia = []    # by now the code below should be self explanatory given all the comments
    cond2negdia = []
    for r in range(game.rows-1,0,-1):
        for c in range(0,game.cols-1):
            cond1negdia = []
            cond2negdia = []
            for i,j in zip((range(r,0,-1)),(range(c,game.cols-1))):
                if game.mat[i,j] == game.mat[i-1,j+1] and game.mat[i,j] == 1:
                    cond1negdia.append(1)
                    cond2negdia = []
                    if len(cond1negdia) == game.wins - 1:
                        player1svictory = True
                elif game.mat[i,j] == game.mat[i-1,j+1] and game.mat[i,j] == 2:
                    cond2negdia.append(1)
                    cond1negdia = []
                    if len(cond2negdia) == game.wins - 1:
                        player2svictory = True
                else:
                    cond1negdia = []
                    cond2negdia = []


    if player1svictory == True and player2svictory == True: # for when a pop results in a simultaneous victory
        if game.turn == 2:                                  # by now move has been applied and turn has been changed so game.turn should == opp turn
            return 1
        elif game.turn == 1:
            return 2
    elif player1svictory == True and player2svictory == False:
        return 1
    elif player2svictory == True and player1svictory == False:
        return 2


    gamematrixlist = [] # creates a list of all the values in the game matrix that is != 0
    for r in range(0,game.rows):
        for c in range(0,game.cols):
            if game.mat[r,c] == 1 or game.mat[r,c] == 2:
                gamematrixlist.append(1)
                if len(gamematrixlist) == game.rows*game.cols:
                    return 3
            else:
                gamematrixlist = []

    return 0 # if no victory checks pass, obviously there's no victory so what else


def apply_move(game,col,pop):
    if pop == False:                                        #   when player chooses to insert,
        for r in range(game.rows):                          #   checks row by row
            if game.mat[r,col] == 0:                        #   for a coordinate with value 0
                game.mat[r,col] = game.turn                 #   and adds the player disc when it is found
                break
    elif pop == True:                                       #   when player chooses to pop
        if game.mat[0,col] == game.turn:                    #   checks bottom row ONLY for a value == game.turn
            for r in range(game.rows - 1):                  #   for each row,
                game.mat[r,col] = game.mat[r + 1,col]       #   the value of each coordinate in the given column is assigned the value of the coordinate above
            game.mat[game.rows - 1, col] = 0                #   assigns the top row coordinate a value 0
    game.turn = (game.turn%2) + 1                           #   changes the turns/players
    return game


def check_move(game,col,pop):
    if pop == True:                                         #   if player chooses to pop,
        if game.mat[0,col] == game.turn:                    #   if the bottom coordinate of the chosen column is the player's disc,
            return True                                     #   it is a valid move
        else:
            return False                                    #   invalid move
    if pop == False:                                        #   if player chooses to insert,
        for r in range(game.rows):                          #   checks row by row
            if game.mat[r,col] == 0:                        #   if there is a coordinate with value 0 in the chosen column,
                return True                                 #   it is a valid move
        else:
            return False                                    #   invalid move


def computer_move(game,level):
    if level == 1:                                  # level 1 opponent, no logic involved
        col = randint(0,game.cols -1)               # pulls a random int
        pop = random.choice([True,False])           # pulls a random bool
        validmove = check_move(game,col,pop)        # checks move for [int,bool], returns a bool
        while validmove == False:                   # if invalid move
            col = randint(0,game.cols -1)           # run everything until 
            pop = random.choice([True,False])       #
            validmove = check_move(game,col,pop)    # check move returns True
        return col, pop                             # returns the final [int,bool]
            
    elif level == 2:                                # im not even sure how i would comment this. i spent too much time debugging this to work for cpu vs cpu
        computermat = np.copy(game.mat)             # creates and assigns a copy of the board in its current state
        for p in [True,False]:
            for c in range(0,game.cols-1):
                if check_move(game,c,p) == True:            # basically if a move can be made that will result in a victory for the player or computer
                    apply_move(game,c,p)                    # the computer will play in that spot
                    game.turn = game.turn%2 + 1             # because rejecting an opponents win and making a win is the same thing
                    if check_victory(game) == game.turn:
                        game.mat = np.copy(computermat)     # if there is a valid move, revert back the board
                        return [c,p]                        # also return the winning or rejecting col, pop
                    else:
                        game.mat = np.copy(computermat)     # otherwise you still have to revert back the board everytime you make a new move
                        continue
                else:
                    continue
        
        game.turn = game.turn%2 + 1
        for p in [True,False]:                              # wait i forgot what this was for but im not going to touch it lest it breaks my code
            for c in range(0,game.cols-1):                  # i mean it should be smth similar to the code above
                if check_move(game,c,p) == True:
                    apply_move(game,c,p)
                    game.turn = game.turn%2 + 1
                    if check_victory(game) == game.turn:
                        game.mat = np.copy(computermat)
                        if p == True:
                            if game.mat[0,c] == 2:
                                game.turn = game.turn%2 + 1
                                return [c,p]
                            else:
                                continue
                        else:
                            game.turn = game.turn%1 + 1
                            return [c,p]
                    else:
                        game.mat = np.copy(computermat)
                        continue
                else:
                    continue
        
        
        game.turn = game.turn%2 + 1     # if after going through everything there's no winning move then too bad
        col = randint(0,game.cols-1)    # dumb bot has to make a dumb random move
        pop = random.choice([True,False])
        if check_move(game,col,pop) == True:
            return [col,pop]
        else:
            pop = False
            return [col,pop]


def gamerows(message): #to deal with the exceptions/cases in which integers are not entered
    while True:
        try:
            userinput = abs(int(input(message)))
            if userinput == 0:
                print("Please input an integer greater than 0.")
                continue
        except ValueError:
            print("Please input an integer")
            continue
        else:
            return userinput


def gamecols(message):
    while True:
        try:
            userinput = abs(int(input(message)))
            if userinput == 0:
                print("Please input an integer greater than 0.")
                continue 
        except ValueError:
            print("Please input an integer")
            continue
        else:
            return userinput


def gamewins(message):
    while True:
        try:
            userinput = abs(int(input(message)))
            if userinput == 0:
                print("Please input an integer greater than 0.")
                continue
        except ValueError:
            print("Please input an integer")
            continue
        else:
            return userinput


def columns(game,message):
    while True:
        try:
            userinput = abs(int(input(message)))
            if userinput not in range(1,game.cols+1):
                print("Please enter a column between the numbers '1' and '" + str(int(game.cols)) + "' (1 starting from the left)")
                continue
        except ValueError:
            print("Please enter a column between the numbers '1' and '" + str(int(game.cols)) + "' (1 starting from the left)")
            continue
        else:
            return userinput


def popout(game,message):
    while True:
        try:
            userinput = int(input(message))
            if userinput < 0 or userinput > 1:
                continue
            elif userinput == 0:
                userinput = False
            else:
                userinput = True
        except ValueError:
            continue
        else:
            return userinput


def menu():
    game = Game()
    print("Welcome to Connect 4!")
    print("")
    print("A standard game has 6 rows, 7 columns and 4 consecutive discs")
    print("")
    print("If you'd like to play a standard game, enter 0")
    print("")
    print("Otherwise, if you'd like to customise, enter any key")

    customchoice = input() # user inputs to choose a standard or custom game
    if customchoice != '0':
        game.rows = gamerows("Number of rows (Negative integers will be treated as positive): ")                        # initializes custom variables
        game.cols = gamecols("Number of columns (Negative integers will be treated as positive): ")                     #                                                                                                  #
        game.wins = gamewins("Number of consecutive discs to win (Negative integers will be treated as positive): ")    #

    elif int(customchoice) == 0:
        game.rows = 6   # initializes default variables
        game.cols = 7   #
        game.wins = 4   #
    
    game.turn = 1                                           # initializes independent variables
    game.mat = np.zeros((int(game.rows),int(game.cols)))    # creates the matrix
    level = False                                           #
    gamechoice = 0                                          #
    victory = 0                                             #

    while game.wins > game.cols or  game.wins > game.rows:     # making sure the discs input is not greater than the no. of rows or columns
        game.wins = gamewins("Please enter a number of discs less than either the number of rows or columns ")
        if game.wins < game.cols or game.wins < game.rows:
            break
    
    while gamechoice == 0:  # player chooses how they would like to play
        print("")
        print("How would you like to play?")
        print("1. Player vs. Player   2. Player vs. Computer    3. Computer vs. Computer")
        try:
            gamechoice = int(input()) # choosing player or computer opponent
            if gamechoice == 2:
                print("Difficulty level of computer:")
                print("1: Easy")
                print("2: Normal") 
                level = int(input())    # inputting the difficulty of the computer opponent
            elif gamechoice == 1:
                break
            elif gamechoice == 3:
                break
            else:
                continue
        except ValueError:  # a value error is returned when a string or null is returned, this handles that
            continue
    
    display_board(game) #prints the empty matrix
        
    #beginning of the game

    if gamechoice == 1: #another player as opponent
        while victory == 0:
            print("")
            print("Player " + str(game.turn) + "'s turn!")
            col = columns(game,"Which column would you like to make a play in? (1 to 7) ") - 1
            pop = popout(game,"Insert or pop a disc (0 for insert, 1 for pop) ")
            if check_move(game,col,pop) == True:
                apply_move(game,col,pop)        # chunks of code here and below signalling the diff game types and their execution
                display_board(game)             # should be self explanatory
                victory = check_victory(game)    
            else:
                print()
                print("Invalid move!")

        if victory == 1:
            print("Congratulations, Player 1 has won!")
        elif victory == 2:
            print("Congratulations, Player 2 has won!")
        elif victory == 3:
            print("Too bad! Nobody won.")
    
    elif level == 1:    #level 1 computer as opponent
        while victory == 0:
            print("")
            print("Player " + str(game.turn) + "'s turn!")
            if game.turn == 2:
                col, pop = computer_move(game,level)
                if check_move(game,col,pop) == True:
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)    
            elif game.turn == 1:
                col = columns(game,"Which column would you like to make a play in? (1 to 7) ") - 1
                pop = popout(game,"Insert or pop a disc (0 for insert, 1 for pop) ")
                if check_move(game,col,pop) == True:
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)
                    
        if victory == 1:
            print("Congratulations, Player 1 has won!")
        elif victory == 2:
            print("Congratulations, Player 2 has won!")
        elif victory == 3:
            print("Too bad! Nobody won.")

    elif level == 2:    #level 2 computer as opponent
        while victory == 0:
            print("")                                                             
            print("Player " + str(game.turn) + "'s turn!")                              
            if game.turn == 2:
                col, pop = computer_move(game,level)
                if check_move(game,col,pop) == True:
                    game.turn = 2
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)
            elif game.turn == 1:
                col = columns(game,"Which column would you like to make a play in? (1 to 7) ") - 1
                pop = popout(game,"Insert or pop a disc (0 for insert, 1 for pop) ")
                if check_move(game,col,pop) == True:
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)
                    
        if victory == 1:
            print("Congratulations, Player 1 has won!")
        elif victory == 2:
            print("Congratulations, Player 2 has won!")
        elif victory == 3:
            print("Too bad! Nobody won.")

    elif gamechoice == 3:   # computer vs. computer this is very fun and is a super easy way to find bugs by spamming it
        while victory == 0:
            print("")                                                          
            print("Player " + str(game.turn) + "'s turn!")
            if game.turn == 1:                           
                col, pop = computer_move(game,2)
                if check_move(game,col,pop) == True:
                    game.turn = 1
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)
            elif game.turn == 2:
                col, pop = computer_move(game,2)
                if check_move(game,col,pop) == True:
                    game.turn = 2
                    apply_move(game,col,pop)
                    display_board(game)
                    victory = check_victory(game)
                    
        if victory == 1:
            print("Congratulations, Player 1 has won!")
        elif victory == 2:
            print("Congratulations, Player 2 has won!")
        elif victory == 3:
            print("Too bad! Nobody won.")
    


# menu()