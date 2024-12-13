
import random
import agents

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'black', WHITE: 'white'}

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

def valid_squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

def initial_board():
    board = [OUTER] * 100
    for i in valid_squares():
        board[i] = EMPTY
    
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board

def print_board(board):
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
    return rep





def is_valid(move):

    return isinstance(move, int) and move in valid_squares()

def opponent(player):
    return BLACK if player is WHITE else WHITE

def find_bracket(square, player, board, direction):
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    return None if board[bracket] in (OUTER, EMPTY) else bracket

def is_legal(move, player, board):
    hasbracket = lambda direction: find_bracket(move, player, board, direction)
    return board[move] == EMPTY and any(map(hasbracket, DIRECTIONS))

def make_move(move, player, board):
    board[move] = player
    for d in DIRECTIONS:
        make_flips(move, player, board, d)
    return board

def make_flips(move, player, board, direction):
    bracket = find_bracket(move, player, board, direction)
    if not bracket:
        return
    square = move + direction
    while square != bracket:
        board[square] = player
        square += direction




class IllegalMoveError(Exception):
    def __init__(self, player, move, board):
        self.player = player
        self.move = move
        self.board = board
    def __str__(self):
        return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)

def legal_moves(player, board):
    return [sq for sq in valid_squares() if is_legal(sq, player, board)]

def any_legal_move(player, board):
    return any(is_legal(sq, player, board) for sq in valid_squares())

def play(black_strategy, white_strategy):
    board = initial_board()
    player = BLACK
    strategy = lambda who: black_strategy if who == BLACK else white_strategy
    while player is not None:
        move = get_move(strategy(player), player, board)
        make_move(move, player, board)
        player = next_player(board, player)
    agents.QLearning().save()
    return board, score(BLACK, board)

def next_player(board, prev_player):
    opp = opponent(prev_player)
    if any_legal_move(opp, board):
        return opp
    elif any_legal_move(prev_player, board):
        return prev_player
    return None

def get_move(strategy, player, board):
    copy = list(board) # copy the board to prevent cheating
    move = strategy(player, copy)
    if not is_valid(move) or not is_legal(move, player, board):
        raise IllegalMoveError(player, move, copy)
    return move

def score(player, board):
    mine, theirs = 0, 0
    opp = opponent(player)
    for sq in valid_squares():
        piece = board[sq]
        if piece == player: mine += 1
        elif piece == opp: theirs += 1
    return mine - theirs






