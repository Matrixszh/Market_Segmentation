import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scatter_plot_age_spending(df):
    plt.style.use('fivethirtyeight')
    age = df['Age'].tolist()
    spending_score = df['Spending Score (1-100)'].tolist()
    fig = plt.figure(figsize=(6, 6))
    plt.scatter(age, spending_score)
    plt.suptitle("Scatter Plot of Age and Spending Score")
    plt.xlabel("Age")
    plt.ylabel("Spending Score")
    plt.show()

def scatter_plot_age_income(df):
    age = df['Age'].tolist()
    annual_income = df['Annual Income (k$)'].tolist()
    fig = plt.figure(figsize=(6, 6))
    plt.scatter(age, annual_income)
    plt.suptitle("Scatter Plot of Age and Annual Income")
    plt.xlabel("Age")
    plt.ylabel("Annual Income (k$)")
    plt.show()

def scatter_plot_income_spending(df):
    annual_income = df['Annual Income (k$)'].tolist()
    spending_score = df['Spending Score (1-100)'].tolist()
    fig = plt.figure(figsize=(6, 6))
    plt.scatter(annual_income, spending_score)
    plt.suptitle("Scatter Plot of Annual Income & Spending Score")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.show()

# Load the data
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Mini-Project-main\clustered_customers.csv')
df.head()

# Call the functions to show the plots
#scatter_plot_age_spending(df)
#scatter_plot_age_income(df)
#scatter_plot_income_spending(df)

