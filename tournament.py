import game
import othello
import agents
import random


def RunSelectedSimulation(epochs, agent_name, opponent_name):
    white_wins, black_wins, opponent_wins, agent_wins = 0, 0, 0, 0
    agent_win_percentage_dict = {}
    for i in range(int(epochs/2)):
        try:
            black, white = game.get_players_tournament(agent_name, opponent_name)
            board, score = othello.play(black, white)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print('Goodbye.')
            
        if score > 0:
            black_wins += 1
        else:
            white_wins += 1

    agent_wins += black_wins
    opponent_wins += white_wins

    black_wins = 0
    white_wins = 0

    for i in range(int(epochs/2)):
        try:
            black, white = game.get_players_tournament(opponent_name, agent_name)
            board, score = othello.play(black, white)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print('Goodbye.')
            
        if score > 0:
            black_wins += 1
        else:
            white_wins += 1

    agent_wins += white_wins
    opponent_wins += black_wins

        
    agent_win_percentage = (agent_wins / (agent_wins + opponent_wins)) * 100
    agent_win_percentage_dict.update({agent_name: agent_win_percentage})

    return agent_win_percentage_dict

def RunMultipleSelectedSimulations(num_simulations, epochs, agent_name, opponent_name):
    agent_win_percentage_dict = {}
    for i in range(num_simulations):
        simulation = RunSelectedSimulation(epochs, agent_name, opponent_name)
        for key in simulation:
            if key in agent_win_percentage_dict:
                agent_win_percentage_dict[key] += simulation[key]
            else:
                agent_win_percentage_dict.update(simulation)
    
    SetAverageValues(agent_win_percentage_dict, num_simulations)
    
    print(agent_win_percentage_dict)

def SetAverageValues(total_dict, num_simulations):
    for key in total_dict:
        total_dict[key] /= num_simulations
    return total_dict
    

def main():
    RunMultipleSelectedSimulations(1, 10, 'ab-weighted-diff', 'random')


if __name__ == '__main__':
    main()