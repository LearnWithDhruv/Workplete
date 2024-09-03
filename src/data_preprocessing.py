# src/data_preprocessing.py
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def clean_data(data):
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    
    scaler = StandardScaler()
    data_normalized = pd.DataFrame(scaler.fit_transform(data_imputed), columns=data.columns)
    
    return data_normalized
