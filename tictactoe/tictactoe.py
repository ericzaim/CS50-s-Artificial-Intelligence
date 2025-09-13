import copy

X = "X"
O = "O"
EMPTY = None

win_indices = [
    [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], # Rows
    [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], # Columns
    [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)] # Diagonals
]

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return O if count_x > count_o else X

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for combo in win_indices:
        a, b, c = combo
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != EMPTY:
            return board[a[0]][a[1]]
    return None

def terminal(board):
    return winner(board) is not None or all(square is not EMPTY for row in board for square in row)

def utility(board):
    w = winner(board)
    if w == X: return 1
    if w == O: return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses alpha-beta pruning.
    """
    if terminal(board):
        return None

    turn = player(board)

    if turn == X:
        best_val, best_move = float('-inf'), None
        for action in actions(board):
            val = min_value(result(board, action), float('-inf'), float('inf'))
            if val > best_val:
                best_val, best_move = val, action
        return best_move

    else:  # turn == O
        best_val, best_move = float('inf'), None
        for action in actions(board):
            val = max_value(result(board, action), float('-inf'), float('inf'))
            if val < best_val:
                best_val, best_move = val, action
        return best_move

def max_value(state, alpha, beta):
    if terminal(state):
        return utility(state)
    v = float('-inf')
    for action in actions(state):
        v = max(v, min_value(result(state, action), alpha, beta))
        if v >= beta:
            return v  # prune
        alpha = max(alpha, v)
    return v

def min_value(state, alpha, beta):
    if terminal(state):
        return utility(state)
    v = float('inf')
    for action in actions(state):
        v = min(v, max_value(result(state, action), alpha, beta))
        if v <= alpha:
            return v  # prune
        beta = min(beta, v)
    return v
