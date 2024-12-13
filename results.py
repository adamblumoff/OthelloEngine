import numpy as np
import matplotlib.pyplot as plt
import tournament
import pandas as pd
import random

if __name__ == '__main__':
    random.seed(2010)
    # Sample dictionary
    my_dict = tournament.RunAllSimulations(6)

    # Convert to DataFrame
    df = pd.DataFrame(my_dict)

    print(df)

