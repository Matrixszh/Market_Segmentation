import tkinter as tk
from tkinter import ttk
from Correlations import plot_distplots, df1
from scatterplots import scatter_plot_age_income, scatter_plot_age_spending, scatter_plot_income_spending, df
from Segmentation import plot_inertia, X_age_spending
from GenderAnalysis import gender_plot, df2
from KMeans import plot_kmeans, df3
from SOM import plot_frequency, plot_clustcust, plot_occurrences, df4
from final2 import plot_final, data
from graph import plot_quant,df8

def show_graph_selection():
    root = tk.Tk()
    root.title("Graph Selection")

    def show_graph():
        selected_option = selected.get().split(":")[0].strip()
        selected_option = int(selected_option)

        if selected_option == 1:
            scatter_plot_age_spending(df)
        elif selected_option == 2:
            scatter_plot_age_income(df)
        elif selected_option == 3:
            scatter_plot_income_spending(df)
        elif selected_option == 4:
            plot_inertia(X_age_spending)
        elif selected_option == 5:
            plot_distplots(df1)
        elif selected_option == 6:
            gender_plot(df2)
        elif selected_option == 7:
            plot_kmeans(df3)
        elif selected_option == 8:
            plot_frequency(df4)
        elif selected_option == 9:
            plot_clustcust(df4)
        elif selected_option == 10:
            plot_occurrences(df4)
        elif selected_option == 11:
            plot_final(data)
        elif selected_option == 12:
            plot_quant(df8)
        else:
            print("Choose a correct number.")

        root.destroy()

    selected = tk.StringVar(root)
    selected.set("Select Graph")
    options = [
        "1: Scatter Plot - Age vs Spending Score",
        "2: Scatter Plot - Age vs Annual Income",
        "3: Scatter Plot - Annual Income vs Spending Score",
        "4: Inertia Plot",
        "5: Distribution Plots",
        "6: Gender Analysis",
        "7: KMeans Clustering",
        "8: Frequency Plot",
        "9: Clustered Customers Plot",
        "10: Occurrences Plot",
        "11: Final Plot",
        "12: Quantisation plot",
    ]


    dropdown = ttk.Combobox(root, textvariable=selected, values=options)
    dropdown.config(width=30)
    dropdown.pack(pady=10)

    button = ttk.Button(root, text="Show Graph", command=show_graph)
    button.config(width=20)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_graph_selection()
