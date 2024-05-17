def CalculateWaitingTime(processes):
    n = len(processes)
    # Adding indices for later retrieval of results in original order
    for i, process in enumerate(processes):
        process['index'] = i

    # Sorting processes by arrival time then by priority for initial setup
    processes.sort(key=lambda x: (x['arrivalTime'], x['priority']))

    remaining_processes = processes[:]
    time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    last_completed_time = 0

    result_information = [{} for _ in range(n)]

    while remaining_processes:
        # Filter processes that have arrived by the current time
        available_processes = [p for p in remaining_processes if p['arrivalTime'] <= time]
        if not available_processes:  # If no processes are available, advance time
            time = min(p['arrivalTime'] for p in remaining_processes)
            continue

        # Select process with the highest priority (lowest number)
        process_to_run = min(available_processes, key=lambda x: x['priority'])
        remaining_processes.remove(process_to_run)

        # Calculate start time for the selected process
        if time < process_to_run['arrivalTime']:
            start_time = process_to_run['arrivalTime']
        else:
            start_time = time

        # Update time and calculate metrics
        time = start_time + process_to_run['burstTime']
        turnaround_time[process_to_run['index']] = time - process_to_run['arrivalTime']
        waiting_time[process_to_run['index']] = start_time - process_to_run['arrivalTime']

        # Store results
        result_information[process_to_run['index']] = {
            "id": process_to_run['id'],
            "arrivalTime": process_to_run['arrivalTime'],
            "burstTime": process_to_run['burstTime'],
            "priority": process_to_run['priority'],
            "waitingTime": waiting_time[process_to_run['index']],
            "turnAroundTime": turnaround_time[process_to_run['index']]
        }

    # Calculate average waiting time and turnaround time
    average_waiting_time = sum(waiting_time) / n
    average_turn_around_time = sum(turnaround_time) / n

    result_information.append({
        "AverageWaitingTime": average_waiting_time,
        "AverageTurnAroundTime": average_turn_around_time
    })

    return result_information


def algoHighestPriorityFirst(processes):
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

    # Total time of calculation
    total_time = sum(p["burstTime"]+1 for p in processes)

    # Ajouter l'état initial de tous les processus à states_processes pour cette seconde
    states_processes.append([{"id": p["id"], "arrivalTime": p["arrivalTime"], "burstTime": p["burstTime"],
                              "priority": p["priority"],
                              "state": p["state"], "order": p["order"]} for p in processes])

    cpu_used = False
    process_in_cpu = processes[0]
    for second in range(total_time):
        # Initialiser l'état pour chaque processus
        for process in processes:
            if process["arrivalTime"] <= 0 < process["burstTime"]:
                if process["state"] == "Queue":
                    process["state"] = "Ready"
            elif process["arrivalTime"] > 0 and process["burstTime"] > 0:
                process["arrivalTime"] -= 1

        for process in processes:
            if process["state"] == "CPU":
                process_in_cpu = process

        for index, process in enumerate(processes):
            if process_in_cpu["priority"] > process['priority']:
                current_process = processes.pop(index)  # Remove the process at the current index
                processes.insert(0, current_process)  # Add it back to the top
                process_in_cpu["state"] = "Ready"
                cpu_used = False
                # as Completed if burst tame is null
                if process_in_cpu["burstTime"] <= 0:
                    process_in_cpu["state"] = "Finished"

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
                                  "priority": p["priority"],
                                  "state": p["state"], "order": p["order"]} for p in processes])

        # If total burstTime is nul so all processes as finished
        if sum(p["burstTime"] for p in processes) == 0:
            break
    return {"States": states_processes, "result": waiting_time_info}
