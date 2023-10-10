import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

def plot_inertia(X_age_spending):
    plt.figure(figsize=(15, 6))
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=300, tol=0.0001, random_state=111, algorithm='elkan')
        model.fit(X_age_spending)
        inertia.append(model.inertia_)
        
    plt.plot(np.arange(1, 11), inertia, 'o')
    plt.plot(np.arange(1, 11), inertia, '-', alpha=0.5)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal Cluster Number')
    plt.show()

# Load the data
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Mini-Project-main\clustered_customers.csv')
df.head()

# Extract age and spending score information from the dataframe
X_age_spending = df[['Age', 'Spending Score (1-100)']].iloc[:, :].values

# Call the function to show the 