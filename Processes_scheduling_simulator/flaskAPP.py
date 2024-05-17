from flask import Flask, request, jsonify
from Algorithms import FCFS, SJF, SRTF, RR, HPF

app = Flask(__name__)


@app.route('/schedule', methods=['POST'])
def schedule_processes():
    data = request.json
    algorithm = data.get('Algorithm')
    all_processes = data.get('processes')

    if not algorithm or not all_processes:
        return jsonify({'error': 'Missing algorithm or processes'}), 400
    states = None
    if algorithm == 'First Come First Served':
        states = FCFS.algoFirstComeFirstServed(all_processes)
    elif algorithm == 'Shortest Job First':
        states = SJF.algoShortestJobFirst(all_processes)
    elif algorithm == 'Round Robin':
        states = RR.algoRoundRobin(all_processes, data.get('quantum'))
    elif algorithm == 'Highest Priority First':
        states = HPF.algoHighestPriorityFirst(all_processes)
    elif algorithm == 'Shortest Remaining Time First':
        states = SRTF.algoShortestRemainingTimeFirst(all_processes)

    response = {
        "States": states["States"],
        "result": states["result"]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
