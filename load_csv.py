import os
import pandas as pd

def load_csv_files(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    dataframes = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(directory, file), encoding='utf-8')
        dataframes.append(df)
    return dataframes

# Usage
csv_directory = 'files'
dataframes = load_csv_files(csv_directory)
