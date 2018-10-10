def display_board(board):
    for row in range(3):
        for col in range(3):
            print("|" + str(board[row*3 + col]),end="")
        print("|")

def play_again():
    user_response = input("Play another round? (y/n): ")
    return user_response == 'y'

def choose_symbol():
    right_input = False
    while(not(right_input)):
        p1_response=input(" Player1 Choose X or 0: ")
        if  p1_response in 'X0':
            if p1_response == 'X':
                player_symbol['p1'] = p1_response
                player_symbol['p2'] = '0'
                right_input = True
            else:
                player_symbol['p1'] = p1_response
                player_symbol['p2'] = 'X'
                right_input = True
        else:
            print("Incorrect input")

def check_winner(board, found_winner):
    for row in range(3):
        if board[row*3] == board[row*3+1] == board[row*3+2] and board[row] in 'X0':
            found_winner = True
            print("check p2, col" + str(board[col]) + ", "+ str(col))
            if board[row*3] == player_symbol['p1']:
                print("player1 wins by row " + str(row) )
                break
            else:
                print("player2 wins by row " + str(row) )
    for col in range(3):
        if board[col] == board[col+3] == board[col+6] and board[col] in 'X0':
            print("check p2, col" + str(board[col]) + ", "+ str(col))
            found_winner = True
            if board[col] == player_symbol['p1']:
                print("player1 wins by col "+ str(col))
                break
            else:
                print("player2 wins by col "+ str(col))
    if ((board[0] == board[4] == board[8] or board[2] == board[4] == board[6])and board[4] in 'X0') :
        found_winner = True
        if board[4] == player_symbol['p1']:
            print("player1 wins by diag")
        else:
            print("player2 wins by diag")

def play():
    found_winner = False
    choose_symbol()
    display_board(board)
    while(True):
        # add logic for no overwrite
        p1_move = input("Your move Player1? ")
        board[int(p1_move)] = player_symbol['p1']
        display_board(board)
        check_winner(board, found_winner)
        if found_winner:
            break
        p2_move = input("Your move Player2? ")
        board[int(p2_move)] = player_symbol['p2']
        display_board(board)
        check_winner(board, found_winner)
        if found_winner:
            break
        
while(play_again()):
    player_symbol = {'p1':'', 'p2':''}
    board = [' ']*9
    play()