import game
import othello
import agents
import random
import time
import multiprocessing


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
            time.sleep(0.25)
            agent_completion_time.append(end_time - start_time)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print(f"{e} {agent_name} {opponent_name}")
            print('Goodbye.')
            
        if score > 0:
            black_wins += 1
        else:
            white_wins += 1
        agent_win_percentage = (black_wins / (i+1)) * 100
        agent_win_percentage_aggregate.append(agent_win_percentage)
        
    print(f"{agent_name} {opponent_name} halfway there" )
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
            time.sleep(0.25)
            agent_completion_time.append(end_time - start_time)
        except othello.IllegalMoveError as e:
            print(e)
        except EOFError as e:
            print(f"{e} {agent_name} {opponent_name}")
            print('Goodbye.')
            
        if score > 0:
            black_wins += 1
        else:
            white_wins += 1
        agent_win_percentage = (white_wins / (i+1)) * 100
        total_win_percentage = ((agent_wins+white_wins)/(i+(epochs/2)+1)) * 100
        agent_win_percentage_aggregate.append(total_win_percentage)
    
    print(f"{agent_name} {opponent_name} done" )
    return agent_win_percentage_aggregate, agent_completion_time

def RunMultipleSelectedSimulations(num_simulations, epochs, agent_name, opponent_name):
    agent_win_percentage_dict = {epochs : [i for i in range(1,epochs+1)]}
    for i in range(num_simulations):

        return RunSelectedSimulation(epochs, agent_name, opponent_name)


def run_simulation_task(args):
    
    epochs, agent_name, opponent_name = args
    print(f"{agent_name} {opponent_name}")
    result1, result2 = RunSelectedSimulation(epochs, agent_name, opponent_name)
    return {
        "agent_name": agent_name,
        "opponent_name": opponent_name,
        "win_percentage": result1,
        "completion_time": result2,
    }


def RunAllSimulations(epochs):
    agent_algorithms = ["QLearning", 'ab-weighted-diff']
    opponents = ["random", "QLearning", 'ab-weighted-diff']
    # Create all combinations of agent vs opponent algorithms
    tasks = [
        (epochs, agent, opponent)
        for agent in agent_algorithms
        for opponent in opponents
        
    ]

    # Use multiprocessing to run simulations concurrently
    with multiprocessing.Pool(processes=min(multiprocessing.cpu_count(), 3)) as pool:
        results = pool.map(run_simulation_task, tasks)

    # Aggregate results into a dictionary
    simulation_results = {"epochs" : [i for i in range(1,epochs+1)]}
    for result in results:
        key = f"{result['agent_name']}_{result['opponent_name']}_win_pct"
        simulation_results.update({key : result['win_percentage']})

        key = f"{result['agent_name']}_{result['opponent_name']}_time"
        simulation_results.update({key: result["completion_time"]})
            

    return simulation_results

def SetAverageValues(total_dict, num_simulations):
    for key in total_dict:
        total_dict[key] /= num_simulations
    return total_dict
    

def main():
    RunMultipleSelectedSimulations(1, 10, 'ab-weighted-diff', 'random')


if __name__ == '__main__':
    main()