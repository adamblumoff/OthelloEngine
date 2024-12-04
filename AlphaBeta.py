#some code adapted from https://github.com/mohammadfahimtajwar/othello-game-ai-backend


import heapq

def FindLines(board, x, y, player):
    # Find all lines that can be flipped by a move at (x, y) by player
    # Return a list of tuples of (x, y) for each line
    
    lines = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            u = x
            v = y
            line = []

            u+= dx
            v+= dy
            found = False

            while u >= 0 and u < len(board) and v >= 0 and v < len(board):
                if board[v][u] == 0:
                    break
                elif board[v][u] == player:
                    found = True
                    break
                line.append((u, v))
                u+= dx
                v+= dy
            if found and line:
                lines.append(line)
    return lines

def GetValidMoves(board, player):
    # Check if player has a valid move
    valid_moves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == 0:
                if FindLines(board, i, j, player):
                    valid_moves.append((i, j))
    return valid_moves
def MakeMove(board, x, y, player):
    # Make a move for player on board (like successor function)
    # Return the new board
    new_board = [row[:] for row in board]
    lines = FindLines(board, x, y, player)
    new_board[y][x] = player
    for line in lines:
        for u, v in line:
            new_board[v][u] = player

    final = []
    for row in new_board:
        final.append(tuple(row))
    return tuple(final)

def CalculateUtility(board):
    p1_utility = 0
    p2_utility = 0

    for row in board:
        for cell in row:
            if cell == 1:
                p1_utility += 1
            elif cell == 2:
                p2_utility += 1
    
    return p1_utility, p2_utility
def OpponentAlphaBeta(board, alpha, beta, level, limit = float("inf")):
    moves = GetValidMoves(board, 1)

    if(len(moves) == 0):
        return CalculateUtility(board)
    
    utilities = []

    for i in range(len(moves)):
        x, y = moves[i]
        utilities.append(CalculateUtility(MakeMove(board, x, y, 1)))
    
    ordered_set = [(utilities[i], moves[i]) for i in range(len(moves))]
    heapq.heapify(ordered_set)
    ordered_moves = [ordered_set[i][1] for i in range(len(ordered_set))]

    value = float("inf")

    for i in range(len(ordered_moves)):
        x, y = ordered_moves[i]
        if level < limit:
            value = min(value, PlayerAlphaBeta(MakeMove(board, x, y, 1), alpha, beta, level + 1, limit))
        else:
            value = min(value, CalculateUtility(MakeMove(board)))

        if value < alpha:
            return value
        
        beta = min(beta, value)
    
    return value

def PlayerAlphaBeta(board, alpha, beta, level, limit = float("inf")):
    moves = GetValidMoves(board, 2)

    if(len(moves) == 0):
        return CalculateUtility(board)
    
    utilities = []

    for i in range(len(moves)):
        x, y = moves[i]
        utilities.append(CalculateUtility(MakeMove(board, x, y, 2)))
    
    ordered_set = [(utilities[i], moves[i]) for i in range(len(moves))]
    heapq.heapify(ordered_set)
    ordered_moves = [ordered_set[i][1] for i in range(len(ordered_set))]

    value = -float("inf")

    for i in range(len(ordered_moves)):
        x, y = ordered_moves[i]
        if level < limit:
            value = max(value, OpponentAlphaBeta(MakeMove(board, x, y, 2), alpha, beta, level + 1, limit))
        else:
            value = max(value, CalculateUtility(MakeMove(board)))
        
        if value > beta:
            return value
        
        alpha = max(alpha, value)
    
    return value

def AlphaBeta(board, player, level = 1, limit = float("inf")):

    moves = GetValidMoves(board, player, limit = float("inf"))
    utilities = []
    if player == 1:
        for i in range(len(moves)):
            x, y = moves[i]
            utilities.append(OpponentAlphaBeta(MakeMove(board, x, y, 1), -float("inf"), float("inf"), 2, limit))
        return moves[utilities.index(max(utilities))]
    else:
        for i in range(len(moves)):
            x, y = moves[i]
            utilities.append(PlayerAlphaBeta(MakeMove(board, x, y, 2), -float("inf"), float("inf"), 2, limit))
        return moves[utilities.index(min(utilities))]
    

