# CPU Scheduling Algorithms API

## Overview
This repository contains a Python Flask API for simulating various CPU scheduling algorithms. These algorithms are crucial for understanding how an operating system manages process scheduling based on different criteria and rules. This project is designed to help students and professionals alike to visualize and comprehend the behavior of different scheduling algorithms in a practical setting.

## Algorithms Implemented
- **FCFS (First Come, First Served)**: Also known as FIFO, this algorithm schedules processes in the order they arrive in the ready queue.
- **SJF (Shortest Job First)**: This algorithm selects the process that has the smallest execution time left when it gets the chance to make a decision.
- **SRTF (Shortest Remaining Time First)**: A preemptive version of SJF where the process with the shortest execution time remaining is always selected next.
- **RR (Round Robin)**: Processes are dispatched in a round-robin order, sharing time slices in a cyclic manner.
- **HPF (Highest Priority First)**: Prioritizes processes based on their priority level, with various tie-breaking strategies.

## Features
- **API Endpoints for Each Algorithm**: Test and compare how each scheduling algorithm handles different process loads.
- **Customizable Parameters**: Users can define the number of processes, burst time, arrival time, priority levels, etc.

## How to Use
refer to the documentation included in the folder "Example_usage"

### Installation:
<pre>
  <code class="language-java">
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    pip install -r requirements.txt

  </code>
</pre>
### Usage:

<pre>
  <code class="language-java">
    python run_server.py
  </code>
</pre>

Once the server is running, you can access the API at http://localhost:5000. Use the following endpoint:
Post: /schedule

## Acknowledgements
**Flask** for the micro web framework used.
**Postman** for testing the API.

