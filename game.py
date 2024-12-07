import othello
import agents
import random
#
def check(move, player, board):
    return othello.is_valid(move) and othello.is_legal(move, player, board)
#
def human(player, board):
    print(othello.print_board(board))
    print('Your move?')
    while True:
        move = input('> ')
        if move and check(int(move), player, board):
            return int(move)
        elif move:
            print('Illegal move--try again.')
#
def get_choice(prompt, options):
    print(prompt)
    print('Options:', options.keys())
    while True:
        choice = input('> ')
        if choice in options:
            return options[choice]
        elif choice:
            print('Invalid choice.')

def set_choice_random(options, black_name, white_name):
    agents = [options[black_name], options[white_name]]
    black = random.choice(agents)
    if black == options[white_name]:
        white = options[black_name]
    else:
        white = options[white_name]
    return black, white

def set_choice(options, black_name, white_name):
    black = options[black_name]
    white = options[white_name]
    return black, white

def get_players():
    print('Welcome to OTHELLO!')
    options = { 'human': human,
                'random': agents.random_strategy,
                'max-diff': agents.maximizer(othello.score),
                'max-weighted-diff': agents.maximizer(agents.weighted_score),
                'ab-diff': agents.alphabeta_searcher(3, othello.score),
                'ab-weighted-diff':
                    agents.alphabeta_searcher(3, agents.weighted_score) }
    black = get_choice('BLACK: choose a strategy', options)
    white = get_choice('WHITE: choose a strategy', options)
    return black, white

def get_players_tournament(black, white):
    options = { 'human': human,
                'random': agents.random_strategy,
                'max-diff': agents.maximizer(othello.score),
                'max-weighted-diff': agents.maximizer(agents.weighted_score),
                'ab-diff': agents.alphabeta_searcher(3, othello.score),
                'ab-weighted-diff':
                    agents.alphabeta_searcher(3, agents.weighted_score) }
    return set_choice(options, black, white)

def main():
    try:
        black, white = get_players()
        board, score = othello.play(black, white)
    except othello.IllegalMoveError as e:
        print(e)
    except EOFError as e:
        print('Goodbye.')
    print('Final score:', score)
    print('%s wins!' % ('Black' if score > 0 else 'White'))
    print(othello.print_board(board))

if __name__ == "__main__":
    main()