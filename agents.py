import othello
import random
import heapq
import pickle
import os

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



def pvs(player, board, alpha, beta, depth, evaluate):
#
    if depth == 0:
        return evaluate(player, board), None
#
    def value(board, alpha, beta):
        return -pvs(othello.opponent(player), board, -beta, -alpha, depth-1, evaluate)[0]
    
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



def pvs_searcher(depth, evaluate):
    def strategy(player, board):
        return pvs(player, board, MIN_VALUE, MAX_VALUE, depth, evaluate)[1]
    return strategy


class QLearning(): #Code adapted from Problem Set 4
    def __init__(self, alpha=.1, epsilon=.2, discount=0.9):
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount
        self.qVals = self.load()
        

    def getQValue(self, board, move):
        if (tuple(board), move) in self.qVals:
            return self.qVals[(tuple(board), move)]
        
        return 0.0
            
    def computeValueFromQValues(self, player, board):
        
        moves = othello.legal_moves(player, board)
        qValues = []
        for move in moves:
            qValues.append(self.getQValue(board, move))
        
        return max(qValues) if len(qValues) > 0 else 0.0

    def computeActionFromQValues(self, player, board):
        
        bestValue = self.getValue(player, board)
        bestMoves = []

        for move in othello.legal_moves(player, board):
            if self.getQValue(board, move) == bestValue:
                bestMoves.append(move)
        
        return random.choice(bestMoves) if len(bestMoves) > 0 else None

    def getMove(self, player, board):
        legalMoves = othello.legal_moves(player, board)
        move = None
        
        if(self.flipCoin(self.epsilon)):
            move = random.choice(legalMoves)
            
        
        elif len(legalMoves) > 0: 
            move = self.getPolicy(player, board)
            

        return move
    
    def flipCoin(self, prob):
        r = random.random()
        return r < prob
    
    def numGames(self, games):
        if games > 0:
            return self.qVals
        return {}

    
    def update(self, player, prev_board, move, board):
        
        reward = weighted_score(player, board) - weighted_score(player, prev_board)
        discount = self.discount
        alpha = self.alpha
        qval = self.getQValue(prev_board, move)
        nextVal = self.getValue(player, board)
        
        
        newQVal = qval + alpha * (reward + (discount * nextVal) - qval)
        
        self.qVals[(tuple(prev_board), move)] = newQVal
        
        
    def getPolicy(self, player, board):
        return self.computeActionFromQValues(player, board)

    def getValue(self, player, board):
        return self.computeValueFromQValues(player, board)
    
    def save(self, filename = 'q_table2.pk1'):
        q_vals = self.qVals
        with open(filename, 'wb') as f: 
            pickle.dump(q_vals, f)
            
    

    def load(self, filename="q_table2.pk1"):
        try:
            with open(filename, 'rb') as f:
               return pickle.load(f)
        except EOFError:
            return {}  
    def QLearningAgent(self):
       def strategy(player, prev_board):
            move = self.getMove(player, prev_board)
            board = othello.make_move(move, player, list(prev_board))
            self.update(player, prev_board, move, board)
            return self.getMove(player, prev_board)
       return strategy


