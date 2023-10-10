import pandas as pd
import matplotlib.pyplot as plt

def plot_final(data):    # Read the first CSV file

    # Group the data by category and count the number of items in each category
    category_counts = data['Category'].value_counts()

    # Find the item with the highest count within each category
    most_bought_items = data.groupby('Category')['Item Name'].apply(lambda x: x.value_counts().idxmax())

    # Set the plot style
    plt.style.use('seaborn')

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot a horizontal bar graph for the category counts
    category_counts.sort_values().plot(kind='barh', ax=ax, color='#6ca2f7')

    # Set the plot title and axes labels
    ax.set_title('Most Bought Items by Category', fontsize=18, fontweight='bold')
    ax.set_xlabel('Number of Items', fontsize=12)
    ax.set_ylabel('Category', fontsize=12)

    # Display the most bought items as annotations on the bar graph
    for i, count in enumerate(category_counts):
        category = category_counts.index[i]
        item = most_bought_items.get(category, 'N/A')
        ax.text(count, i, f" {item}",color='black', fontweight='bold')

    # Adjust the y-axis ticks and labels
    ax.set_yticks(range(len(category_counts)))
    ax.set_yticklabels(category_counts.index)

    # Invert the y-axis for top-to-bottom ordering
    ax.invert_yaxis()

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add gridlines
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Adjust the plot margins
    plt.tight_layout()

    plt.show()    

data1 = pd.read_csv('items.csv')

    # Read the second CSV file
data2 = pd.read_csv('assigned_items.csv')

    # Concatenate the two datasets
data = pd.concat([data1, data2])
