def CalculateWaitingTime(processes, quantum):
    n = len(processes)
    remaining_bt = [p['burstTime'] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    last_finished_time = [0] * n

    time = 0
    queue = []
    result_information = []

    # Initially load all processes which are available at the start
    for i in range(n):
        if processes[i]['arrivalTime'] <= time:
            queue.append(i)
            last_finished_time[i] = processes[i]['arrivalTime']  # To track last active time

    while queue:
        i = queue.pop(0)  # Remove first element process from queue
        if remaining_bt[i] > quantum:
            time += quantum
            remaining_bt[i] -= quantum
        else:
            time += remaining_bt[i]
            remaining_bt[i] = 0

        # Process has finished its current quantum or completely finished
        last_finished_time[i] = time  # Update last finished time

        # Requeue the current process if it's not finished
        if remaining_bt[i] > 0:
            queue.append(i)

        # Load processes that have arrived in the meantime into the queue
        for j in range(n):
            if processes[j]['arrivalTime'] <= time and remaining_bt[j] > 0 and j not in queue:
                queue.append(j)

    # Calculate waiting and turnaround times
    for i in range(n):
        turnaround_time[i] = last_finished_time[i] - processes[i]['arrivalTime']
        waiting_time[i] = turnaround_time[i] - processes[i]['burstTime']
        result_information.append({
            "id": processes[i]['id'],
            "arrivalTime": processes[i]['arrivalTime'],
            "burstTime": processes[i]['burstTime'],
            "waitingTime": waiting_time[i],
            "turnAroundTime": turnaround_time[i]
        })

    # Calculate average Waiting time and Turnaround time
    average_waiting_time = sum(waiting_time) / n
    average_turn_around_time = sum(turnaround_time) / n

    # adding Average Waiting Time
    result_information.append({
        "AverageWaitingTime": average_waiting_time,
        "AverageTurnAroundTime": average_turn_around_time
    })
    return result_information


def algoRoundRobin(processes, quantum):
    n = len(processes)

    # Calculate waiting time for each process
    waiting_time_info = CalculateWaitingTime(processes, quantum)

    states_processes = []

    # Initialize the state for each process
    for process in processes:
        process["state"] = "Queue"  # Initial state of all processes
        process["order"] = processes.index(process)
        if process["arrivalTime"] == 0:
            process["state"] = "Ready"

    # Total time of calculation
    total_time = sum(p["burstTime"]+1 for p in processes)

    # Ajouter l'état initial de tous les processus à states_processes pour cette seconde
    states_processes.append([{"id": p["id"], "arrivalTime": p["arrivalTime"], "burstTime": p["burstTime"],
                              "state": p["state"], "order": p["order"]} for p in processes])

    cpu_used = False
    remaining_quantum = quantum
    for second in range(total_time):
        # Initialiser l'état pour chaque processus
        for process in processes:
            if process["arrivalTime"] <= 0 < process["burstTime"]:
                if process["state"] == "Queue":
                    process["state"] = "Ready"
            elif process["arrivalTime"] > 0 and process["burstTime"] > 0:
                process["arrivalTime"] -= 1

        for index, process in enumerate(processes):
            if process["state"] == "CPU":
                if remaining_quantum == 0:
                    current_process = processes.pop(index)  # Remove the process at the current index
                    processes.append(current_process)  # Add it back to the end
                    remaining_quantum = quantum
                    process["state"] = "Ready"
                    cpu_used = False
                    # as Completed if burst tame is null
                    if process["burstTime"] == 0:
                        process["state"] = "Finished"
                else:
                    remaining_quantum -= 1

        #
        # for process in processes:
        #     process["order"] = processes.index(process)

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
                    # process["order"] = -1
                break  # un seul processus run

        # Add the current state of all processes for this second
        states_processes.append([{"id": p["id"], "arrivalTime": p["arrivalTime"], "burstTime": p["burstTime"],
                                  "state": p["state"], "order": p["order"]} for p in processes])

        # If total burstTime is nul so all processes as finished
        if sum(p["burstTime"] for p in processes) == 0:
            break
    return {"States": states_processes, "result": waiting_time_info}
