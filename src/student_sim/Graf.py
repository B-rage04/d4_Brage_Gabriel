"""
Authors:
Brage Bromset Bestvold
Gabriel Røer
"""


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set(style="whitegrid")


def plot_simulation(world, sim):
    """Generates a wide range of plots for the simulation."""
    #  Collect data
    data = []
    for s in world.students:
        for t, (pos, move) in enumerate(s.history):
            data.append({
                'Student': s.name,
                'Time': t+1,
                'Position': pos,
                'Move': move,
                'Steps': s.steps_taken,
                'FinalPos': s.position,
                'Destination': s.destination
            })
    df = pd.DataFrame(data)

    # Students per endpoint
    endpoint_counts = df.groupby('Destination')['Student'].nunique()
    plt.figure(figsize=(8, 4))
    sns.barplot(x=endpoint_counts.index, y=endpoint_counts.values, palette='pastel')
    plt.title("Students per Endpoint")
    plt.ylabel("Number of Students")
    plt.show()

    # Histogram of steps
    final_steps = df.groupby('Student')['Steps'].max()
    plt.figure(figsize=(8, 4))
    sns.histplot(final_steps, bins=10, kde=True, color='skyblue')
    plt.title("Distribution of Steps Taken")
    plt.xlabel("Steps")
    plt.show()
