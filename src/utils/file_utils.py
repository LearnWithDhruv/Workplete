import os
import pandas as pd

def save_processed_data(data, file_name='processed_data.pkl'):
    data.to_pickle(os.path.join('data', file_name))

def load_processed_data(file_name='processed_data.pkl'):
    return pd.read_pickle(os.path.join('data', file_name))
