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
def visualize(times, populations):
    plt.figure(figsize=(10, 5))
    plt.step(times, populations, where='post')
    plt.title('Pure Birth Process Simulation')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.grid()
    st.pyplot(plt)

# Diagram
def plot_state_transition_diagram(max_population, birth_rate):
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

def display_statistics(populations):
    average_population = np.mean(populations)
    variance_population = np.var(populations)
    expected_births = populations[-1]  

    st.write(f"### Summary Statistics")
    st.write(f"**Average Population Size:** {average_population:.2f}")
    st.write(f"**Variance in Population Size:** {variance_population:.2f}")
    st.write(f"**Expected Number of Births:** {expected_births}")
