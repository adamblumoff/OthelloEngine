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

    df = pd.read_csv("data.csv")

    #create numpy arrays for figures
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

    # figure 1
    fig1 = plt.figure(figsize=(12, 8))  # Create a new figure
    fig1.canvas.manager.set_window_title("Figure 1")
    plt.plot(epochs, y1, label="QLearning vs. random opponent")
    plt.plot(epochs, y2, label="QLearning vs. QLearning opponent")
    plt.plot(epochs, y3, label="QLearning vs. PVS opponent")
    plt.plot(epochs, y4, label="PVS vs. random opponent")
    plt.plot(epochs, y5, label="PVS vs. QLearning opponent")
    plt.plot(epochs, y6, label="PVS vs. PVS opponent")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.legend(loc="best")
    plt.title("AI Win Percentages vs # of Games Played")
    plt.xlabel("# of Games")
    plt.ylabel("Win %")

    #figure 2
    fig2 = plt.figure(figsize=(12, 8)) 
    fig2.canvas.manager.set_window_title("Figure 2")
    plt.plot(epochs, y7, label="QLearning vs. random opponent")
    plt.plot(epochs, y8, label="QLearning vs. QLearning opponent")
    plt.plot(epochs, y9, label="QLearning vs. PVS opponent")
    plt.plot(epochs, y10, label="PVS vs. random opponent")
    plt.plot(epochs, y11, label="PVS vs. QLearning opponent")
    plt.plot(epochs, y12, label="PVS vs. PVS opponent")
    plt.legend(loc="best")
    plt.title("AI Time to Complete Game vs # of Games Played")
    plt.xlabel("# of Games")
    plt.ylabel("Time (sec)")
    plt.show()

    # table 1
    final_win_pct = np.around(df.iloc[-1].to_numpy()[1::2], 3)
    default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    print(final_win_pct)
    data = [["QLearning vs. random opponent", "QLearning vs. QLearning opponent", 
             "QLearning vs. PVS opponent", "PVS vs. random opponent", 
             "PVS vs. QLearning opponent", "PVS vs. PVS opponent"],
             final_win_pct]
    plt.axis("off")
    table = plt.table(cellText=data, colLabels=None, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(6)))
    table.scale(1.5, 2.0)
    for i in range(6):
        table[(0, i)].set_facecolor(default_colors[i])  # Set background color
        table[(0, i)].set_text_props(color="white")
        table[(1, i)].set_text_props(fontsize=12)
    plt.text(0.5, 0.6, "Agent Win Rates (%) After 1000 Games", ha="center", fontsize=16, fontweight="bold")
    plt.show()

    # table 2
    np_df = df.to_numpy().T
    
    avg_times = [np.around(np.mean(np_df[i]), 3) for i in range(2, 13, 2)]
    data2 = [["QLearning vs. random opponent", "QLearning vs. QLearning opponent", 
             "QLearning vs. PVS opponent", "PVS vs. random opponent", 
             "PVS vs. QLearning opponent", "PVS vs. PVS opponent"],
             avg_times]
    
    plt.axis("off")
    table2 = plt.table(cellText=data2, colLabels=None, loc='center', cellLoc='center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(10)
    table2.auto_set_column_width(col=list(range(6)))
    table2.scale(1.5, 2.0)
    for i in range(6):
        table2[(0, i)].set_facecolor(default_colors[i])  # Set background color
        table2[(0, i)].set_text_props(color="white")
        table2[(1, i)].set_text_props(fontsize=12)
    plt.text(0.5, 0.6, "Mean Time of Game Completion in Seconds", ha="center", fontsize=16, fontweight="bold")
    plt.show()
    

