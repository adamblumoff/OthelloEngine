import othello
import agents
import random

def SetChoice(options, black_name, white_name):
    black = options[black_name]
    white = options[white_name]
    return black, white

def GetPlayersTournament(black, white):
    QLearning = agents.QLearning()
    options = { 'random': agents.random_strategy,
                'max-diff': agents.maximizer(othello.score),
                'max-weighted-diff': agents.maximizer(agents.weighted_score),
                'ab-diff': agents.alphabeta_searcher(3, othello.score),
                'ab-weighted-diff':
                    agents.alphabeta_searcher(3, agents.weighted_score), 
                'QLearning': QLearning.QLearningAgent()}
    return SetChoice(options, black, white)

def RunSelectedSimulation(epochs, agent_name, opponent_name):
    white_wins, black_wins, opponent_wins, agent_wins = 0, 0, 0, 0
    agent_win_percentage_dict = {}
    
    for i in range(int(epochs/2)):
        try:
            black, white = GetPlayersTournament(agent_name, opponent_name)
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
            black, white = GetPlayersTournament(opponent_name, agent_name)
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
    
def ListAllAgents():
    print('Here are the list of agents you can choose from:')
    print('1. random')
    print('2. max-diff')
    print('3. max-weighted-diff')
    print('4. ab-diff')
    print('5. ab-weighted-diff')
    print('6. QLearning')

def StartTournament():
    print('Welcome to the Othello Tournament!')
    random.seed(1)
    ListAllAgents()
    agent = input('Enter the name of the agent you want to test: ')
    opponent = input('Enter the name of the opponent you want to test against: ')
    epochs = int(input('Enter the number of games you want to run for each simulation: '))
    return agent, opponent, epochs

def DebugTournament():
    random.seed(1)
    agent, opponent, epochs = 'QLearning', 'ab-weighted-diff', 20
    simulation = RunSelectedSimulation(epochs, agent, opponent)
    print(simulation)

def main():
    DebugTournament()
    #agent, opponent, num_simulations, epochs = StartTournament()
    #RunMultipleSelectedSimulations(num_simulations, epochs, agent, opponent)


if __name__ == '__main__':
    main()