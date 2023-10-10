import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
def gender_plot(df2):
    plt.figure(1 , figsize = (15 , 6)) # sets the dimensions of image
    n = 0 
    plt.figure(1 , figsize = (15 , 5))
    sns.countplot(y = 'Gender' , data = df2)
    plt.show()

df2 = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Mini-Project-main\clustered_customers.csv')
df2.head()


