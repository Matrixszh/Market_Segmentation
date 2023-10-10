import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from minisom import MiniSom  
df4 = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Mini-Project-main\clustered_customers.csv')
df4.head()
df4.isnull().sum()
features = df4[['Annual Income (k$)', 'Spending Score (1-100)']]
data = features.values
data.shape
som_shape = (1, 5)
som = MiniSom(som_shape[0], som_shape[1], data.shape[1], sigma=0.5, learning_rate=0.5)
max_iter = 1000
q_error = []
t_error = []
winner_coordinates = np.array([som.winner(x) for x in data]).T
cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)
for i in range(max_iter):
    rand_i = np.random.randint(len(data))
    som.update(data[rand_i], som.winner(data[rand_i]), i, max_iter)
    q_error.append(som.quantization_error(data))
    t_error.append(som.topographic_error(data))
def plot_clustcust(df4):
    winner_coordinates = np.array([som.winner(x) for x in data]).T
    cluster_1index = np.ravel_multi_index(winner_coordinates, som_shape)
    plt.figure(figsize=(10,8))
    for c in np.unique(cluster_index):
        plt.scatter(data[cluster_index == c, 0],
                    data[cluster_index == c, 1], label='cluster='+str(c), alpha=.7)
    for centroid in som.get_weights():
        plt.scatter(centroid[:, 0], centroid[:, 1], marker='x', 
                    s=10, linewidths=20, color='k')
    plt.title("Clusters of Customers")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.show()
def plot_frequency(df4):
    num_clusters = som_shape[1]
    cluster_labels = cluster_index
    df4['Cluster'] = cluster_labels
    num_rows = int(np.ceil(num_clusters / 2))
    num_cols = min(2, num_clusters)
    plt.figure(figsize=(10, 6))
    for cluster in range(num_clusters):
        plt.subplot(num_rows, num_cols, cluster + 1)
        plt.hist(df4['Annual Income (k$)'][df4['Cluster'] == cluster], bins=10, alpha=0.7)
        plt.title('Cluster ' + str(cluster))
        plt.xlabel('Annual Income (k$)')
        plt.ylabel('Frequency')#chuttiya 
    plt.tight_layout()
    plt.show()
def plot_occurrences(df4):
    winner_coordinates = np.array([som.winner(x) for x in data]).T
    cluster_labels = np.ravel_multi_index(winner_coordinates, som_shape)
    df4['Cluster'] = cluster_labels
    df4.to_csv('clustered_customers.csv', index=False)
    cluster_counts = df4['Cluster'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.bar(cluster_counts.index, cluster_counts.values)
    plt.title('Cluster Occurrences')
    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.xticks(cluster_counts.index)
    plt.show()