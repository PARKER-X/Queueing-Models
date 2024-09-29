# Import 
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from birthprocess import birthProcess,plot_state_transition_diagram_birth,visualize_birth,display_statistics
from deathprocess import *

st.write("Queueing Models")

models = st.selectbox("Select Your Queueing Model",
                      ("Pure Birth Process","Pure Death Process","Pure Birth-Death Process"),
                      help="Select one")
st.write("You selected:",models)

# Pure Birth Process Models 
if models=="Pure Birth Process":    
    birth_rate = st.sidebar.slider("Birth Rate (λ)",0.1,10.0,1.0)
    total_time = st.sidebar.slider("Total Time ",1,100,10)
    if st.button("Run Simulation"):
        times, populations = birthProcess(birth_rate, total_time)
        # Plotting
        visualize_birth(times, populations)
        final_population=populations[-1]
        st.write(f"Final population after {total_time} time units: {final_population}")
        plot_state_transition_diagram_birth(final_population,birth_rate)
        display_statistics(populations)
        st.markdown("""
### Pure Birth Process
The pure birth process is a stochastic process.
- **Defination**:
It is a counting process {N(t), t ∈ [0,∞)}, where N(t) denotes the number of arrivals (births)
occurred in time t, i.e., in [0, t] with N(0) = 0 and average rate of arrival λ > 0, and which 
satisfies the following three assumptions:
1) The probability that an arrival occurs between time t and time t + Δt is equal to λΔt + o(Δt). 
That is, Pr {one arrival occurs between t and t + Δt } = λΔt + o(Δt), where λ is a constant 
independent of N(t), Δt is an incremental element, and o(Δt) denotes a quantity that 
becomes negligible when compared to Δt as Δt → 0.
2) Pr { more than one arrival between t and t + Δt } = o(Δt), i.e., almost negligible.
3) The numbers of arrivals in non-overlapping intervals are statistically independent; 
that is, the process has independent increments. 
                    
The key characteristics include:

- **State**: Defined by the current population size.
- **Birth Rate**: The rate at which new individuals/arrivals are born, influencing the population growth.
- **Time**: The total duration of the simulation.

The process can be visualized using a state transition diagram, which shows possible population states and transitions.

                    [time_to_next_birth = np.random.exponential(1 / birth_rate)] 
we use np.random bcoz poisson processs is random in nature and follows memoryless property.
                    
Average Rate of Births is 1/λ.

""")
        

# Pure Death Process Models 
if models=="Pure Death Process":    
    death_rate = st.sidebar.slider("Death Rate (µ)",0.1,10.0,1.0)
    total_time = st.sidebar.slider("Total Time ",1,100,10)
    Population = st.sidebar.slider("Initial Population ",1,100,10)
    if st.button("Run Simulation"):
        times, populations = deathProcess(death_rate, total_time,Population)
        # Plotting
        visualize_death(times, populations)
        final_population=populations[-1]
        st.write(f"Final population after {total_time} time units: {final_population}")
        plot_state_transition_diagram_death(final_population,death_rate)
        display_statistics(populations)
        st.markdown("""It is a counting process {N(t), t ∈ [0,∞)}, where N(t) denotes the number of departures 
(deaths) occurred in time t, i.e., in [0, t] with N(0) = 0 and average rate of departure 
µ> 0, and which satisfies the following three assumptions:
1) Pr { one departure occurs between t and t + Δt } = µΔt + o(Δt), where µ is a constant 
independent of N(t), Δt is an incremental element, and o(Δt) denotes a quantity 
that becomes negligible when compared to Δt as Δt → 0.
2) Pr { more than one departure between t and t + Δt } = o(Δt), i.e., negligible.
3) The numbers of departures in non-overlapping intervals are statistically 
independent; that is, the process has independent increments.

                    A pure death process {N(t), t ∈ [0,∞)} is same as a truncated Poisson process, PP(µ).
This means :
• The random variable N(t) denoting number of departures in time t follows a 
truncated Poisson distribution with parameter µt, i.e., P(µt).
• Equivalently, it can be said that the time between successive departures, 
i.e., the service time / inter-departure time follows an exponential 
distribution with parameter µ, i.e., exp(µ).
""")