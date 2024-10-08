import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(corr_matrix):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()
