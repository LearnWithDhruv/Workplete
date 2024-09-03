# src/analysis_engine.py
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

def run_analysis(data):
    model_lr = LinearRegression()
    model_lr.fit(data.iloc[:, :-1], data.iloc[:, -1])
    lr_results = model_lr.predict(data.iloc[:, :-1])
    
    model_kmeans = KMeans(n_clusters=3)
    kmeans_results = model_kmeans.fit_predict(data)
    
    model_dt = DecisionTreeClassifier()
    model_dt.fit(data.iloc[:, :-1], data.iloc[:, -1])
    dt_results = model_dt.predict(data.iloc[:, :-1])
    
    return lr_results, kmeans_results, dt_results
