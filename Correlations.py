import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distplots(df1):
    plt.figure(figsize=(15, 6))
    n = 0
    for x in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:
        n += 1
        plt.subplot(1, 3, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.distplot(df1[x], bins=20)
        plt.title('Distplot of {}'.format(x))
    plt.show()

# Load the data
df1 = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Mini-Project-main\clustered_customers.csv')
df1.head()

# Call the function to show the plots
