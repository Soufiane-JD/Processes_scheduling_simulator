def CalculateWaitingTime(processes):
    n = len(processes)
    result_information = [0] * n

    # Array of waiting time
    wt = [0] * n
    tat = [0] * n

    # Sort processes based on burst time and then by arrival time
    processes.sort(key=lambda x: (x['burstTime'], x['arrivalTime'] ))

    # Waiting time for first process is 0
    wt[0] = 0
    tat[0] = wt[0] + processes[0]['burstTime']

    # Print waiting time process 1
    result_information[0] = {
        "id": processes[0]['id'],
        "arrivalTime": processes[0]['arrivalTime'],
        "burstTime": processes[0]['burstTime'],
        "waitingTime": wt[0],
        "turnAroundTime": tat[0]
    }

    # Calculate waiting time for all processes
    for i in range(1, n):
        wt[i] = wt[i - 1] + processes[i - 1]['burstTime'] - processes[i]['arrivalTime']
        wt[i] = max(0, wt[i])  # Waiting time cannot be negative
        tat[i] = wt[i] + processes[i]['burstTime']

        result_information[i] = {
            "id": processes[i]['id'],
            "arrivalTime": processes[i]['arrivalTime'],
            "burstTime": processes[i]['burstTime'],
            "waitingTime": wt[i],
            "turnAroundTime": tat[i]
        }

    # Calculate average Waiting time and Turnaround time
    average_waiting_time = sum(wt) / n
    average_turn_around_time = sum(tat) / n

    # adding Average Waiting Time
    result_information.append({"AverageWaitingTime": average_waiting_time, "AverageTurnAroundTime": average_turn_around_time})

    return result_information


def algoShortestRemainingTimeFirst(processes):
    n = len(processes)

    # Calculate waiting time for each process
    waiting_time_info = CalculateWaitingTime(processes)

    states_processes = []

    # Initialize the state for each process
    for process in processes:
        process["state"] = "Queue"  # Initial state of all processes
        process["order"] = processes.index(process)
        if process["arrivalTime"] == 0:
            process["state"] = "Ready"

    # processes.sort(key=lambda proc: proc["arrivalTime"])

    # Sort processes based on burst time and then by arrival time
    processes.sort(key=lambda x: (x['burstTime'], x['arrivalTime']))

    # Total time of calculation
    total_time = sum(p["burstTime"]+1 for p in processes)

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

    return {"States": states_processes, "result": waiting_time_info}
