# src/utils/analysis_utils.py
def get_correlation_matrix(data):
    """
    Return the correlation matrix of the data.
    """
    return data.corr()

def summarize_statistics(data):
    """
    Return summary statistics of the data.
    """
    return data.describe()
