import copy

"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None

win_indices = [
    [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], #Rows
    [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], #Columns
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
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)

    if count_x > count_o:
        return "O"
    else:
        return "X"

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
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for combination in win_indices:
        a, b, c = combination
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != None:
            return board[a[0]][a[1]]  # Return the winner ('X' or 'O')

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for square in row:
            if square == EMPTY:
                return False
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        value, action = float('-inf'), None
        for action in actions(board):
            min_value = Minvalue(result(board, action))
            if min_value > value:
                value, action = min_value, action
        return action
    else:
        value, action = float('inf'), None
        for action in actions(board):
            max_value = Maxvalue(result(board, action))
            if max_value < value:
                value, action = max_value, action
        return action

def Maxvalue(state):
    v = float('-inf')
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = max(v,Minvalue(result(state,action)))
    return v

def Minvalue(state):
    v = float('inf')
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = min(v,Maxvalue(result(state,action)))
    return v