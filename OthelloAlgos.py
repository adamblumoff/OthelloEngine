#Code adapted from https://github.com/mohammadfahimtajwar/othello-game-ai-backend




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
    # Make a move for player on board
    # Return the new board
    new_board = [row[:] for row in board]
    lines = FindLines(board, x, y, player)
    new_board[y][x] = player
    for line in lines:
        for u, v in line:
            new_board[v][u] = player

    final 

    