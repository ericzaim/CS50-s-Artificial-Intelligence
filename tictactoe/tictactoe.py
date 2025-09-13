"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None

win_indices = [
    [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)] #Rows
    [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)] #Columns
    [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)] #Diagonals
    ]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    for line in board:
        count_x = line.count(X)
        count_o = line.count(O)
        count_empty = line.count(EMPTY)
        if count_x > count_o and count_empty!=0:
            return O
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    for i,row in enumerate(board):
        for j in range(len(row)):
            if (i,j) == action:
                board[i,j] = player(board) 
                return board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    maps={}
    for i,row in board:
        for j,cell in row:
            maps[cell].append((i,j))
            
    for combination in win_indices:
        if (combo == combination for combo in maps[combination[0]]):
            return combination[0]
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if (square == EMPTY for square in row):
            return True
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    while True:
        while terminal(board) != True:
            for action in actions(board):
                new_board = result(board,action)
                if utility(new_board) == 1:
                    return action
                
    raise NotImplementedError
