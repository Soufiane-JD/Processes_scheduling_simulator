import json
import streamlit as st
import pandas as pd
import time
from Algorithms import FCFS
from Algorithms import SJF
from Algorithms import RR
from Algorithms import HPF
from Algorithms import SRTF


def main():
    title_algo = st.empty()
    title_algo.title("FCFS Scheduling Simulator")

    # Example processes data
    processes1 = [
        {"id": 0, "arrivalTime": 2, "burstTime": 4},
        {"id": 1, "arrivalTime": 1, "burstTime": 7},
        {"id": 2, "arrivalTime": 8, "burstTime": 2},
        {"id": 3, "arrivalTime": 5, "burstTime": 8},
        {"id": 4, "arrivalTime": 4, "burstTime": 4},
    ]

    processes = [
        {"id": 1, "arrivalTime": 2, "burstTime": 6},
        {"id": 2, "arrivalTime": 5, "burstTime": 2},
        {"id": 3, "arrivalTime": 1, "burstTime": 8},
        {"id": 4, "arrivalTime": 0, "burstTime": 3},
        {"id": 5, "arrivalTime": 4, "burstTime": 4},
    ]
    processes3 = [
        {"id": 1, "arrivalTime": 0, "burstTime": 5},
        {"id": 2, "arrivalTime": 1, "burstTime": 4},
        {"id": 3, "arrivalTime": 2, "burstTime": 2},
        {"id": 4, "arrivalTime": 3, "burstTime": 1},
    ]

    processes4 = [
        {"id": 1, "arrivalTime": 0, "burstTime": 3, "priority": 3},
        {"id": 2, "arrivalTime": 1, "burstTime": 4, "priority": 2},
        {"id": 3, "arrivalTime": 2, "burstTime": 6, "priority": 4},
        {"id": 4, "arrivalTime": 3, "burstTime": 4, "priority": 6},
        {"id": 5, "arrivalTime": 5, "burstTime": 2, "priority": 10},
    ]

    processes5 = [
        {"id": 1, "arrivalTime": 0, "burstTime": 8, "priority": 3},
        {"id": 2, "arrivalTime": 1, "burstTime": 2, "priority": 4},
        {"id": 3, "arrivalTime": 3, "burstTime": 4, "priority": 4},
        {"id": 4, "arrivalTime": 4, "burstTime": 1, "priority": 5},
        {"id": 5, "arrivalTime": 5, "burstTime": 6, "priority": 2},
        {"id": 6, "arrivalTime": 6, "burstTime": 5, "priority": 6},
        {"id": 7, "arrivalTime": 10, "burstTime": 2, "priority": 1},
    ]

    # Define a list of choices
    choices = ['First Come First Served', 'Shortest Job First', 'Round Robin', 'Highest Priority First', 'Shortest Remaining Time First']

    # Create a selectbox to allow users to select one option
    selected_option = st.selectbox('Choose an option:', choices)

    if st.button('Start Simulation'):
        title_algo.title(selected_option)
        numbers = st.empty()
        states_placeholder = st.empty()
        states = None
        if selected_option == 'First Come First Served':
            states = FCFS.algoFirstComeFirstServed(processes1)
        elif selected_option == 'Shortest Job First':
            states = SJF.algoShortestJobFirst(processes)
        elif selected_option == 'Round Robin':
            states = RR.algoRoundRobin(processes, 2)
        elif selected_option == 'Highest Priority First':
            states = HPF.algoHighestPriorityFirst(processes5)
        elif selected_option == 'Shortest Remaining Time First':
            states = SRTF.algoShortestRemainingTimeFirst(processes5)

        json_data = json.dumps(states, indent=1)
        print(json_data)

        for second, state in enumerate(states["States"]):
            numbers.write(f"Time: {second}")
            df = pd.DataFrame(state)
            time.sleep(1)
            states_placeholder.dataframe(df)


if __name__ == "__main__":
    main()
