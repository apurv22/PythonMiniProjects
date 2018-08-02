def check_win(sym):
    #Function to check if a player has won or not
    if (board[0]==sym and board[1]==sym and board[2]==sym) or (board[3]==sym and board[4]==sym and board[5]==sym) or (board[6]==sym and board[7]==sym and board[8]==sym) or (board[0]==sym and board[3]==sym and board[6]==sym) or (board[1]==sym and board[4]==sym and board[7]==sym) or (board[2]==sym and board[5]==sym and board[8]==sym) or (board[0]==sym and board[4]==sym and board[8]==sym) or (board[2]==sym and board[4]==sym and board[6]==sym):
        return True
    else:
        return False
    
def check_play(loc):
    #Function to check if the entered position number is already occupied
    if loc in position_occupied:
        return False
    else:
        return True
    
def display_board():
    #Function to display the game board
    for i in range(3):
        print(board[3*i]+" "+board[3*i + 1]+" "+board[3*i + 2])



print("Tic-Tac-Toe (Player vs Player)")
print("The structure of the board is as follows:")
print("1  2  3")
print("4  5  6")
print("7  8  9")
print("\nEnter the respective number of the board location at the time of your turn")
player = '1'
symbol = 'X'
play_next = True    #Variable to decide if further play is needed or not
num_turn = 0
position_occupied = []  #List that stores the positions already occupied
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while play_next:
    print("====== Player "+player+"'s turn ======")
    loc = int(input("Enter the location number to play: "))
    #Check if the play is valid
    if check_play(loc):
        position_occupied.append(loc)
        board[loc-1] = symbol
        num_turn += 1
        display_board()

        #Check if player has won
        if check_win(symbol):
            print("\n\n*^*^*^ Player "+player+" wins ^*^*^*")
            play_next = False
        #Check if game is drawn
        elif num_turn == 9:
            print("\n\n*^*^*^ Game Draw ^*^*^*")
            play_next = False

        #Changing the player and symbol
        if player == '1':
            player = '2'
            symbol = 'O'
        else:
            player = '1'
            symbol = 'X'

    else:
        print("Invalid input")
        print("Enter valid position number")
