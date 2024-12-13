
import agents
#

def set_choice(options, black_name, white_name):
    black = options[black_name]
    white = options[white_name]
    return black, white


def get_players_tournament(black, white):
    options = { 'random': agents.random_strategy,
                'ab-weighted-diff':
                    agents.alphabeta_searcher(3, agents.weighted_score),
                'QLearning': agents.QLearning().QLearningAgent()}
    return set_choice(options, black, white)
