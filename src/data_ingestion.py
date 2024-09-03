import pandas as pd

def load_data(file_path):
    print(f"Attempting to load data from: {file_path}")
    file_extension = file_path.split('.')[-1]
    if file_extension == 'csv':
        data = pd.read_csv(file_path)
    elif file_extension == 'json':
        data = pd.read_json(file_path)
    elif file_extension in ['xls', 'xlsx']:
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    print("Data loaded successfully.")
    return data

