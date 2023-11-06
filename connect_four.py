def initialize_board(num_rows, num_cols): #create the 2d list necesary for the connect four games
    board = [] #creates a simple list at first
    for i in range(num_rows): #runs through a loop that will create a 2d list, which carries columns, which contain rows
        board.append(['-'] * num_cols)
    return board #returns the created board

def print_board(board): #when called, this will print the current board for us
    for row in board:
        print(' '.join(row)) #when printed, it will actually look like a 2d list

def insert_chip(board, col, chip_type): #allows the users to input chips
    for row in range(len(board) - 1, -1, -1): #sets the range
        if board[row][col] == '-': #if there is no chip, it places the chip
            board[row][col] = chip_type
            return row
    return -1  # column is full

def check_if_winner(board, col, row, chip_type):#function that will allow for checking of horizontal wins or vertical wins
    if (check_horizontal(board, row, chip_type) or
        check_vertical(board, col, chip_type)):
        return True
    return False #returns the true or false, as instructed in the instructions

def check_horizontal(board, row, chip_type):
    count = 0 #uses a count variable to count up how many times a chip is in the horizontal
    for c in range(len(board[0])): #goes through the 2d list and checks for 4 in a rows
        if board[row][c] == chip_type: #ues teh actual row
            count += 1
            if count == 4:
                return True
        else:
            count = 0 #resets the coutn back to 0
    return False

def check_vertical(board, col, chip_type):
    count = 0 #uses a count variable to count up how many times a chip is in the vertical
    for r in range(len(board)):
        if board[r][col] == chip_type: #uses the column
            count += 1
            if count == 4:
                return True
        else:
            count = 0 #resets the count back to 0
    return False

if __name__ == '__main__':
    #all the basic stuf to allow the game to actually be played
    num_rows = int(input('What would you like the height of the board to be? '))
    num_cols = int(input('What would you like the length of the board to be? '))
    print()
    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print()
    print('Player 1: x')
    print('Player 2: o')
    print()
    game_won = False #allows for a loop to be made
    moves = 0 #to check if there is a tie, and to choose who is playing(will be explianed later on in the code)

    while not game_won and moves < num_rows * num_cols: #checks if the game has been won or if there has been a tie
        if moves % 2 == 0:
            player = 'Player 1'
            chip = 'x'
        else:
            player = 'Player 2'
            chip = 'o'
        col = int(input(f'{player}: Which column would you like to choose? '))
        print()
        row = insert_chip(board, col, chip)
        if row == -1:#checks if clumn is full
            print("Column is full. Try again.")
            continue
        print_board(board)
        print()
        if check_if_winner(board, col, row, chip):
            print(f'{player} won the game!')
            game_won = True
            break
        moves += 1

    if not game_won: #for when there is a draw
        print("Draw. Nobody wins.")
