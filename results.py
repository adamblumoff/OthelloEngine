import numpy as np
import matplotlib.pyplot as plt
import tournament
import pandas as pd

if __name__ == '__main__':

    # Sample dictionary
    my_dict = tournament.RunAllSimulations(10)

    # Convert to DataFrame
    df = pd.DataFrame(my_dict)

    print(df)