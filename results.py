import numpy as np
import matplotlib.pyplot as plt
import tournament
import pandas as pd
import random
def run_sims():
    random.seed(2010)
    # Sample dictionary
    my_dict = tournament.RunAllSimulations(1000)

    # Convert to DataFrame
    df = pd.DataFrame(my_dict)

    df.to_csv("data.csv", index=False)

if __name__ == '__main__':
    #run_sims()
    # tournament.RunSelectedSimulation(1000, "QLearning", "random")
    # tournament.RunSelectedSimulation(1000, "QLearning", "QLearning")
    df = pd.read_csv("data.csv")

