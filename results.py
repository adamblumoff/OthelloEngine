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
    epochs = df["epochs"].to_numpy()
    y1 = df["QLearning_random_win_pct"].to_numpy()
    y2 = df["QLearning_QLearning_win_pct"].to_numpy()
    y3 = df["QLearning_ab-weighted-diff_win_pct"].to_numpy()
    y4 = df["ab-weighted-diff_random_win_pct"].to_numpy()
    y5 = df["ab-weighted-diff_QLearning_win_pct"].to_numpy()
    y6 = df["ab-weighted-diff_ab-weighted-diff_win_pct"].to_numpy()
    y7 = df["QLearning_random_time"].to_numpy()
    y8 = df["QLearning_QLearning_time"].to_numpy()
    y9 = df["QLearning_ab-weighted-diff_time"].to_numpy()
    y10 = df["ab-weighted-diff_random_time"].to_numpy()
    y11 = df["ab-weighted-diff_QLearning_time"].to_numpy()
    y12 = df["ab-weighted-diff_ab-weighted-diff_time"].to_numpy()
    fig1 = plt.figure(figsize=(12, 8))  # Create a new figure
    fig1.canvas.manager.set_window_title("Figure 1")
    plt.plot(epochs, y1, label="QLearning vs. random opponent")
    plt.plot(epochs, y2, label="QLearning vs. QLearning opponent")
    plt.plot(epochs, y3, label="QLearning vs. AB Weighted opponent")
    plt.plot(epochs, y4, label="AB Weighted vs. random opponent")
    plt.plot(epochs, y5, label="AB Weighted vs. QLearning opponent")
    plt.plot(epochs, y6, label="AB Weighted vs. AB Weighted opponent")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.legend(loc="best")
    plt.title("AI Win Percentages vs # of Games Played")
    plt.xlabel("# of Games")
    plt.ylabel("Win %")
    fig2 = plt.figure(figsize=(12, 8))  # Create a new figure
    fig2.canvas.manager.set_window_title("Figure 2")
    plt.plot(epochs, y7, label="QLearning vs. random opponent")
    plt.plot(epochs, y8, label="QLearning vs. QLearning opponent")
    plt.plot(epochs, y9, label="QLearning vs. AB Weighted opponent")
    plt.plot(epochs, y10, label="AB Weighted vs. random opponent")
    plt.plot(epochs, y11, label="AB Weighted vs. QLearning opponent")
    plt.plot(epochs, y12, label="AB Weighted vs. AB Weighted opponent")
    plt.legend(loc="best")
    plt.title("AI Time to Complete Game vs # of Games Played")
    plt.xlabel("# of Games")
    plt.ylabel("Time (sec)")
    plt.show()
    

