def CalculateWaitingTime(processes):
    n = len(processes)
    result_information = [0] * n
    at = [process['arrivalTime'] for process in processes]
    bt = [process['burstTime'] for process in processes]

    # Array of waiting time
    wt = [0] * n

    # Array of turn_around_time
    tat = [0] * n

    # Waiting time for first process is 0
    wt[0] = 0
    tat[0] = wt[0] + processes[0]['burstTime']

    # Print waiting time process 1
    result_information[0] = {"id": 0, "arrivalTime": at[0], "burstTime": bt[0], "waitingTime": wt[0],
                             "turnAroundTime": tat[0]}

    # Calculating waiting time for all process
    for i in range(1, n):
        wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i]
        tat[i] = wt[i] + bt[i]
        result_information[i] = {"id": i, "arrivalTime": at[i], "burstTime": bt[i], "waitingTime": wt[i],
                                 "turnAroundTime": tat[i]}

    # Calculate average Waiting time
    average_waiting_time = 0.0
    sum_waiting_time = 0

    # Calculate sum of all waiting time
    for i in range(n):
        sum_waiting_time = sum_waiting_time + wt[i]

    # Find average waiting time
    # by dividing it by no. of process
    average_waiting_time = sum_waiting_time / n

    # Calculate average turn around time
    average_turn_around_time = sum(tat) / n

    # adding Average Waiting Time
    result_information.append({"AverageWaitingTime": average_waiting_time, "AverageTurnAroundTime": average_turn_around_time})

    return result_information


def algoFirstComeFirstServed(processes):
    n = len(processes)
    result_wt = CalculateWaitingTime(processes)

    states_processes = []

    # Initialize the state for each process
    for process in processes:
        process["state"] = "Queue"  # Initial state of all processes
        process["order"] = processes.index(process)
        if process["arrivalTime"] == 0:
            process["state"] = "Ready"

    # processes.sort(key=lambda proc: proc["arrivalTime"])

    # Total time of calculation
    total_time = sum(p["burstTime"]+1 for p in processes)+1

    # Ajouter l'état initial de tous les processus à states_processes pour cette seconde
    states_processes.append([{"id": p["id"], "arrivalTime": p["arrivalTime"], "burstTime": p["burstTime"],
                              "state": p["state"], "order": p["order"]} for p in processes])

    cpu_used = False
    for second in range(total_time):
        # Initialiser l'état pour chaque processus
        for process in processes:
            if process["arrivalTime"] <= 0 < process["burstTime"]:
                if process["state"] == "Queue":
                    process["state"] = "Ready"
            elif process["arrivalTime"] > 0 and process["burstTime"] > 0:
                process["arrivalTime"] -= 1

        for process in processes:
            # Run the first ready process
            if (process["state"] == "Ready" and not cpu_used) or process["state"] == "CPU":
                process["state"] = "CPU"
                cpu_used = True
                process["burstTime"] -= 1
                # as Completed if burst tame is null
                if process["burstTime"] <= 0:
                    process["state"] = "Finished"
                    cpu_used = False
                    #process["order"] = -1
                break  # un seul processus run


        # Add the current state of all processes for this second
        states_processes.append([{"id": p["id"], "arrivalTime": p["arrivalTime"], "burstTime": p["burstTime"],
                                  "state": p["state"], "order": p["order"]} for p in processes])

        # If total burstTime is nul so all processes as finished
        if sum(p["burstTime"] for p in processes) == 0:
            break
    return {"States": states_processes, "result": result_wt}
