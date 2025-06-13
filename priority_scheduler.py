# Priority Scheduling (Non-preemptive)

processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 5, 'priority': 2},
    {'id': 'P2', 'arrival': 1, 'burst': 3, 'priority': 1},
    {'id': 'P3', 'arrival': 2, 'burst': 4, 'priority': 3},
]

time = 0
completed = []
ready_queue = []

while len(completed) < len(processes):
    for p in processes:
        if p not in completed and p['arrival'] <= time and p not in ready_queue:
            ready_queue.append(p)

    if ready_queue:
        ready_queue.sort(key=lambda x: x['priority'])
        current = ready_queue.pop(0)
        print(f"{current['id']} starts at {time}")
        time += current['burst']
        print(f"{current['id']} finishes at {time}")
        completed.append(current)
    else:
        time += 1
