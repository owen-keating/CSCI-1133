
import random

#warmup

def print_board(board):
    print(board[0]+board[1]+board[2])
    print(board[3]+board[4]+board[5])
    print(board[6]+board[7]+board[8])

#warmup2

list = []
win = ''

def open_spots(board):
    global list
    list = []
    for i in range(9):
        if(board[i]=='-'):
            list.append(i)
    return list

#warmup3

def random_move(board,symbol):
    open_spots(board)
    x = random.choice(list)
    board[x] = symbol
    print_board(board)

#stretch

def check_three(board,idx1,idx2,idx3):
    global win
    win = ''
    if(board[idx1]==board[idx2] and board[idx1]==board[idx3]):
        win = board[idx1]
    else:
        win = '-'
    return win

#stretch2

def winner(board):
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    global win
    for triple in combos:
        check_three(board,triple[0],triple[1],triple[2])
        if(win=='X' or win=='O'):
            break
    open_spots(board)
    if(win!='X' and win!='O' and list==[]):
        win = 'D'
    return win

#workout

def tic_tac_toe():
    board = ['-','-','-','-','-','-','-','-','-']
    random_move(board,'X')
    print("\n")
    for i in range(4):
        random_move(board,'O')
        print("\n")
        x = winner(board)
        if(x=='X' or x=='O'):
            break
        random_move(board,'X')
        print("\n")
        y = winner(board)
        if(y=='X' or y=='O'):
            break
    return win

#challenge

def tic_tac_sim():
    xwin = 0
    owin = 0
    draw = 0
    for i in range(100):
        x = tic_tac_toe()
        if(x=='X'):
            xwin+=1
        if(x=='O'):
            owin+=1
        if(x=='D'):
            draw+=1
    print("X wins: " + str(xwin))
    print("O wins: " + str(owin))
    print("Draws: " + str(draw))
