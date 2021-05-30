import random


def display_board(board):
    print('\n'*10)
    print (board[7] + '|' + board[8] + '|' + board[9])
    print (board[4] + '|' + board[5] + '|' + board[6])
    print (board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
    
    # Keep Asking Player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input ('Player 1, choose X or O: ').upper()
    # Assign Player 2, the opposite marker
    player1 = marker
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    mark_win = False
    
    # Check All Rows
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        
        # Check all Columns
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        
        # Check diagonals
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark)
    )

def choose_first():
    starting = random.randint(1, 3)
    if starting == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
        # Board is full if we return True
    return True

def player_choice(board):
    avail_list = list(range(1, 10))
    position = 0
    while position not in avail_list or not space_check(board, position):
        position = int(input ('Please put index of position (1-9) where you want to mark:'))
        if position not in avail_list:
            print ("Sorry, I don't understand, please choose between 1 to 9")
        
        return position

def replay():
    play_again = 'nah'
    while play_again not in ['Y', 'N']:
        play_again = input ('Do you want to play again?: (Enter Y or N)').upper()
        if play_again not in ['Y', 'N']:
            print ("Sorry, I don't understand, please choose Y or N")
    return play_again == 'Y'


print('Welcome to Tic Tac Toe!')
# While loo to keep running the game
while True:
    # Play the game

    ## Set Everything up (Board, whos first, choose markers)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? (Y or N)').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## Game play
    while game_on:
        ## Player One turn
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False

            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break

            # No tie and no win? Then the next player's turn
                else:
                    turn = 'Player 2'

        ## Player Two turn
        else:
            # Show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False

            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break

            # No tie and no win? Then the next player's turn
                else:
                    turn = 'Player 1'

    # Break out of the while loop on replay()
    if not replay():
        break
