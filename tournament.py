import game
import othello
import agents
import random
import time


def RunSelectedSimulation(epochs, agent_name, opponent_name):
    white_wins, black_wins, opponent_wins, agent_wins = 0, 0, 0, 0
    agent_win_percentage_aggregate = []
    agent_completion_time = []
    for i in range(int(epochs/2)):
        try:
            black, white = game.get_players_tournament(agent_name, opponent_name)
            start_time = time.time()
            board, score = othello.play(black, white)
            end_time = time.time()
            agent_completion_time.append(end_time - start_time)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print('Goodbye.')
            
        if score > 0:
            print(f"{agent_name} black")
            print("WIN")
            black_wins += 1
        else:
            print(f"{agent_name} black")
            print("LOSS")
            white_wins += 1
        agent_win_percentage = (black_wins / (i+1)) * 100
        agent_win_percentage_aggregate.append(agent_win_percentage)
        
        
    agent_wins += black_wins
    opponent_wins += white_wins

    black_wins = 0
    white_wins = 0

    for i in range(int(epochs/2)):
        try:
            black, white = game.get_players_tournament(opponent_name, agent_name)
            start_time = time.time()
            board, score = othello.play(black, white)
            end_time = time.time()
            agent_completion_time.append(end_time - start_time)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print('Goodbye.')
            
        if score > 0:
            print(f"{agent_name} white")
            print("LOSS")
            black_wins += 1
        else:
            print(f"{agent_name} white")
            print("WIN")
            white_wins += 1
        agent_win_percentage = (white_wins / (i+1)) * 100
        total_win_percentage = ((agent_wins+white_wins)/(i+6)) * 100
        agent_win_percentage_aggregate.append(total_win_percentage)

    # agent_wins += white_wins
    # opponent_wins += black_wins

        
    # agent_win_percentage = (agent_wins / (agent_wins + opponent_wins)) * 100
    # agent_win_percentage_dict.update({agent_name: agent_win_percentage})
    return agent_win_percentage_aggregate, agent_completion_time

def RunMultipleSelectedSimulations(num_simulations, epochs, agent_name, opponent_name):
    agent_win_percentage_dict = {epochs : [i for i in range(1,epochs+1)]}
    for i in range(num_simulations):

        return RunSelectedSimulation(epochs, agent_name, opponent_name)
    #     for key in simulation:
    #         if key in agent_win_percentage_dict:
    #             agent_win_percentage_dict[key] += simulation[key]
    #         else:
    #             agent_win_percentage_dict.update(simulation)
    #         print(agent_win_percentage_dict)
    
    # SetAverageValues(agent_win_percentage_dict, num_simulations)
    
    # print(agent_win_percentage_dict)
def RunAllSimulations(epochs):
    auto_agents = ["ab-weighted-diff", "QLearning"]
    opponents = ["ab-weighted-diff", "QLearning", "random"]
    agent_win_percentage_dict = {"epochs" : [i for i in range(1,epochs+1)]}
    for i in auto_agents:
        for j in opponents:
            print(f"{i} {j}")
            win_pct, epoch_times = RunSelectedSimulation(epochs, i, j)
            agent_win_percentage_dict.update({f"{i}_{j}_win_pct" : win_pct})
            agent_win_percentage_dict.update({f"{i}_{j}_times" : epoch_times})

    #     for key in simulation:
    #         if key in agent_win_percentage_dict:
    #             agent_win_percentage_dict[key] += simulation[key]
    #         else:
    #             agent_win_percentage_dict.update(simulation)
    #         print(agent_win_percentage_dict)
    
    # SetAverageValues(agent_win_percentage_dict, num_simulations)
    
    print(agent_win_percentage_dict)
    return agent_win_percentage_dict
def SetAverageValues(total_dict, num_simulations):
    for key in total_dict:
        total_dict[key] /= num_simulations
    return total_dict
    

def main():
    RunMultipleSelectedSimulations(1, 10, 'ab-weighted-diff', 'random')


if __name__ == '__main__':
    main()