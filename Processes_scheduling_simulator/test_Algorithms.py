import json
from Algorithms import FCFS
from Algorithms import SJF
from Algorithms import SRTF
from Algorithms import RR
from Algorithms import HPF

processes = [
    {"id": 0, "arrivalTime": 0, "burstTime": 4},
    {"id": 1, "arrivalTime": 1, "burstTime": 3},
    {"id": 2, "arrivalTime": 2, "burstTime": 1},
    {"id": 3, "arrivalTime": 3, "burstTime": 2},
    {"id": 4, "arrivalTime": 4, "burstTime": 5},
]
processes2 = [
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
json_data = json.dumps(FCFS.algoFirstComeFirstServed(processes), indent=4)
#json_data = json.dumps(SJF.algoShortestJobFirst(processes), indent=4)
#json_data = json.dumps(SRTF.algoShortestRemainingTimeFirst(processes), indent=4)
#json_data = json.dumps(RR.algoRoundRobin(processes3, 2), indent=4)
#json_data = json.dumps(HPF.algoHighestPriorityFirst(processes4), indent=4)
print(json_data)
