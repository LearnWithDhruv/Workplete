# src/utils/file_utils.py
import os
import pandas as pd

def save_processed_data(data, file_name='processed_data.pkl'):
    """
    Save processed data to a file.
    """
    data.to_pickle(os.path.join('data', file_name))

def load_processed_data(file_name='processed_data.pkl'):
    """
    Load processed data from a file.
    """
    return pd.read_pickle(os.path.join('data', file_name))
