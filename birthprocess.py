import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Models
def birthProcess(birth_rate,total_time):
    time=0
    population=0
    times=[time]
    populations=[population]
    while time<total_time:
        time_to_next_birth = np.random.exponential(1 / birth_rate)
        time += time_to_next_birth
        population+=1
        times.append(time)
        populations.append(population)
    return times,populations

# Visualization
def visualize_birth(times, populations):
    plt.figure(figsize=(10, 5))
    plt.step(times, populations, where='post')
    plt.title('Pure Birth Process Simulation')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.grid()
    st.pyplot(plt)

# Diagram
def plot_state_transition_diagram_birth(max_population, birth_rate):
    G = nx.DiGraph()
    
    for i in range(max_population + 1):
        G.add_node(i)
        if i < max_population:
            G.add_edge(i, i + 1)  # Just create the edges without weights

    pos = nx.spring_layout(G)  # Calculate positions without weights
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=1800, node_color='lightblue', font_size=12)
    
    # Draw edge labels with birth rate
    edge_labels = {(i, i + 1): f'λ={birth_rate}' for i in range(max_population)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)
    
    plt.title("State Transition Diagram")
    plt.xlabel("Population Size")
    plt.ylabel("Next Population Size")
    plt.grid()
    st.pyplot(plt)

# Statistics
def display_statistics(populations):
    # Calculate statistics
    final_population = populations[-1]
    mean_population = np.mean(populations)
    std_population = np.std(populations)
    
    # Create a DataFrame for more statistics if needed
    df = pd.DataFrame({'Time': range(len(populations)), 'Population': populations})
    
    # Display statistics in Streamlit
    st.write("### Statistics")
    st.write(f"Final Population: {final_population}")
    st.write(f"Mean Population: {mean_population:.2f}")
    st.write(f"Standard Deviation of Population: {std_population:.2f}")

    # Plot population over time
    plt.figure(figsize=(10, 5))
    plt.plot(df['Time'], df['Population'], marker='o', linestyle='-', color='blue')
    plt.title("Population Over Time")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.grid()
    st.pyplot(plt)