import othello
import random
import heapq

def random_strategy(player, board):
    return random.choice(othello.legal_moves(player, board))

def maximizer(evaluate):
#
    def strategy(player, board):
#
        def score_move(move):
            return evaluate(player, othello.make_move(move, player, list(board)))
        return max(othello.legal_moves(player, board), key=score_move)
    return strategy

SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

def weighted_score(player, board):
#
    opp = othello.opponent(player)
    total = 0
    for sq in othello.valid_squares():
        if board[sq] == player:
            total += SQUARE_WEIGHTS[sq]
        elif board[sq] == opp:
            total -= SQUARE_WEIGHTS[sq]
    return total

MAX_VALUE = sum(map(abs, SQUARE_WEIGHTS))
MIN_VALUE = -MAX_VALUE

def final_value(player, board):
#
    diff = othello.score(player, board)
    if diff < 0:
        return MIN_VALUE
    elif diff > 0:
        return MAX_VALUE
    return diff



def alphabeta(player, board, alpha, beta, depth, evaluate):
#
    if depth == 0:
        return evaluate(player, board), None
#
    def value(board, alpha, beta):
        return -alphabeta(othello.opponent(player), board, -beta, -alpha, depth-1, evaluate)[0]
    
    moves = othello.legal_moves(player, board)
    if not moves:
        if not othello.any_legal_move(othello.opponent(player), board):
            return final_value(player, board), None
        return value(board, alpha, beta), None
    
    utilities = []
    for move in moves:
        utilities.append(value(othello.make_move(move, player, list(board)), alpha, beta))
    
    ordered_set = [(utilities[i], moves[i]) for i in range(len(moves))]
    heapq.heapify(ordered_set)
    ordered_moves = [ordered_set[i][1] for i in range(len(ordered_set))]

    
    best_move = ordered_moves[0]
    for move in ordered_moves:
        if alpha >= beta:
            break
        val = value(othello.make_move(move, player, list(board)), alpha, beta)
        if val > alpha:
            alpha = val
            best_move = move
    return alpha, best_move



def alphabeta_searcher(depth, evaluate):
    def strategy(player, board):
        return alphabeta(player, board, MIN_VALUE, MAX_VALUE, depth, evaluate)[1]
    return strategy