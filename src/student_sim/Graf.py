
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
    plt.figure(figsize=(8,4))
    sns.barplot(x=endpoint_counts.index, y=endpoint_counts.values, palette='pastel')
    plt.title("Students per Endpoint")
    plt.ylabel("Number of Students")
    plt.show()

    # Histogram of steps
    final_steps = df.groupby('Student')['Steps'].max()
    plt.figure(figsize=(8,4))
    sns.histplot(final_steps, bins=10, kde=True, color='skyblue')
    plt.title("Distribution of Steps Taken")
    plt.xlabel("Steps")
    plt.show()

    # Histogram of positions visited
    plt.figure(figsize=(10,4))
    sns.histplot(df['Position'], bins=range(0,101), color='lightgreen')
    plt.title("Frequency of Positions Visited")
    plt.xlabel("Position")
    plt.show()

    # Pie chart move directions
    move_counts = df['Move'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(move_counts, labels=move_counts.index, autopct='%1.1f%%', colors=['lightgreen','salmon','lightgray'])
    plt.title("Move Direction Distribution")
    plt.show()

    # Average position over time
    avg_pos = df.groupby('Time')['Position'].mean()
    plt.figure(figsize=(10,4))
    sns.lineplot(x=avg_pos.index, y=avg_pos.values)
    plt.title("Average Position Over Time")
    plt.ylabel("Position")
    plt.xlabel("Time (seconds)")
    plt.show()
    
    # Heatmap: position frequency over time 
    heat_data = df.pivot_table(index='Student', columns='Time', values='Position', fill_value=np.nan)
    plt.figure(figsize=(12,6))
    sns.heatmap(heat_data, cmap="viridis", cbar_kws={'label': 'Position'})
    plt.title("Heatmap of Student Positions Over Time")
    plt.xlabel("Time")
    plt.ylabel("Student")
    plt.show()
    
    # Boxplot: steps per endpoint 
    steps_endpoint = df.groupby('Student').agg({'Steps':'max','Destination':'first'}).dropna()
    plt.figure(figsize=(8,4))
    sns.boxplot(x='Destination', y='Steps', data=steps_endpoint, palette='pastel')
    plt.title("Steps Taken per Endpoint")
    plt.show()
    
    # Boxplot: time per endpoint 
    time_endpoint = df.groupby('Student').agg({'Time':'max','Destination':'first'}).dropna()
    plt.figure(figsize=(8,4))
    sns.boxplot(x='Destination', y='Time', data=time_endpoint, palette='pastel')
    plt.title("Time Taken per Endpoint")
    plt.show()
    
    # Cumulative steps over time 
    cum_steps = df.groupby('Time')['Steps'].sum().cumsum()
    plt.figure(figsize=(10,4))
    sns.lineplot(x=cum_steps.index, y=cum_steps.values)
    plt.title("Cumulative Steps Over Time")
    plt.ylabel("Total Steps")
    plt.xlabel("Time")
    plt.show()
    
    # Cumulative students finished over time 
    finished_df = df[df['Destination'].notna()]
    cum_finished = finished_df.groupby('Time')['Student'].nunique().cumsum()
    plt.figure(figsize=(10,4))
    sns.lineplot(x=cum_finished.index, y=cum_finished.values)
    plt.title("Cumulative Students Finished Over Time")
    plt.ylabel("Number of Students Finished")
    plt.xlabel("Time")
    plt.show()
    
    # Scatter: final position vs steps 
    final_df = df.groupby('Student').agg({'FinalPos':'max','Steps':'max'})
    plt.figure(figsize=(8,4))
    sns.scatterplot(x='Steps', y='FinalPos', data=final_df)
    plt.title("Final Position vs Steps")
    plt.show()
    
    # Scatter: final position vs time 
    final_df['Time'] = df.groupby('Student')['Time'].max()
    plt.figure(figsize=(8,4))
    sns.scatterplot(x='Time', y='FinalPos', data=final_df)
    plt.title("Final Position vs Time")
    plt.show()
    
    # Histogram: time per endpoint 
    plt.figure(figsize=(8,4))
    sns.histplot(time_endpoint, x='Time', hue='Destination', multiple='stack', bins=10)
    plt.title("Time to Reach Endpoint")
    plt.show()
    
    # Histogram: steps per endpoint 
    plt.figure(figsize=(8,4))
    sns.histplot(steps_endpoint, x='Steps', hue='Destination', multiple='stack', bins=10)
    plt.title("Steps to Reach Endpoint")
    plt.show()
    
    # Endpoint occupancy over time
    endpoint_times = df[df['Destination'].notna()].groupby(['Destination','Time']).size().unstack(fill_value=0)
    endpoint_times.T.plot(figsize=(10,4))
    plt.title("Endpoint Occupancy Over Time")
    plt.ylabel("Number of Students")
    plt.xlabel("Time")
    plt.show()
    
    # steps smoth
    plt.figure(figsize=(10,4))
    sns.kdeplot(final_steps, fill=True, color='skyblue')
    plt.title("Steps Distribution (KDE)")
    plt.show()
    
    
    # Top 10 most visited coordinates 
    pos_counts = df['Position'].value_counts().sort_values(ascending=False).head(10)
    plt.figure(figsize=(8,4))
    sns.barplot(x=pos_counts.index, y=pos_counts.values, palette='viridis')
    plt.title("Top 10 Most Visited Coordinates")
    plt.ylabel("Visits")
    plt.xlabel("Coordinate")
    plt.show()