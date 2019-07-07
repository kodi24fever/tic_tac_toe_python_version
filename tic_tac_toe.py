# Initializing Empty Array of length 10
play_board = ['-']*9
player = ''
playerVSplayer = True
playerVScomputer = False

#check for full board
def isBoardFull():
    for i in range(9):
        if play_board[i] == '-':
            return False
    
    return True

#check if someone has won the game
def hasWinner(playerString):
    if (play_board[0] == playerString and play_board[1] == playerString and play_board[2] == playerString or
        play_board[3] == playerString and play_board[4] == playerString and play_board[5] == playerString or
        play_board[6] == playerString and play_board[7] == playerString and play_board[8] == playerString or

        play_board[0] == playerString and play_board[3] == playerString and play_board[6] == playerString or
        play_board[1] == playerString and play_board[4] == playerString and play_board[7] == playerString or
        play_board[2] == playerString and play_board[5] == playerString and play_board[8] == playerString or

        play_board[0] == playerString and play_board[4] == playerString and play_board[8] == playerString or
        play_board[6] == playerString and play_board[4] == playerString and play_board[2] == playerString):
        return True
    else:
        return False

# method to display what user has to play
def whoAmI(playerString):
    print(f"\tIt is the turn of the player {playerString}")
    value = input(f"\n\tWhat is your move {playerString}?")
    isString(value, playerString)
    
#update board
def updateBoard(positionInBoard, player):
    #check if that position is available
    if play_board[positionInBoard] != '-':
        print("\tYou have to re-enter a value because that position is taken\n")
        whoAmI(player)
    else:
        play_board[positionInBoard] = player

# method to tell what player has to play
def thisPlayerHasToMove(playerToMove):
    nextPlayerToMove = playerToMove
    return nextPlayerToMove

#function to print the board 
def print_board(board):
    print(
        f"""
            \t{board[0]}  |   {board[1]}  |  {board[2]} \n
               ----------------\n
            \t{board[3]}  |   {board[4]}  |  {board[5]} \n
               ----------------\n
            \t{board[6]}  |   {board[7]}  |  {board[8]} \n
        """)

#is input a string
def isString(input, player):
    if input == '' or not(input.isdigit()):
        print("\tINVALID VALUE\n")
        whoAmI(player)
    else:
        isInputInRange(input, player)

#check if input is in range
def isInputInRange(input, player):
    if not(int(input) >= 0 and int(input) < 9):
        print("\tINVALID VALUE\n")
        whoAmI(player)
    else: 
        updateBoard(int(input), player)

#It works like a main function which will start the game
def startGame():
    # Welcome message
    print("\n\n  Hello, Welcome To the Tic Tac Toe Game.\n")
    print_board(play_board)


    player = thisPlayerHasToMove('X')
    isGamePlaying = True
    
    #loop to keep playing until board is completed
    while isGamePlaying:
        if player == 'X':
            whoAmI(player)
            print_board(play_board)
            if hasWinner(player):
                print(f"The winner is {player}")
                isGamePlaying = False
                break
            player = thisPlayerHasToMove('O')
        elif player == 'O':
            whoAmI(player)
            print_board(play_board)
            if hasWinner(player):
                print(f"There winner is {player}")
                print_board(play_board)
                isGamePlaying = False
                break
            player = thisPlayerHasToMove('X')
        
        if isBoardFull():
            print("The game is tie!!")
            break



#method to start the game. Have Fun!!!!
startGame()