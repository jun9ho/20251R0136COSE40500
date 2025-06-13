# round_robin.py

from collections import deque

processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 5},
    {'id': 'P2', 'arrival': 1, 'burst': 4},
    {'id': 'P3', 'arrival': 2, 'burst': 2},
]

time_quantum = 2
time = 0
queue = deque()
remaining = {p['id']: p['burst'] for p in processes}
arrivals = {p['arrival']: [] for p in processes}
for p in processes:
    arrivals[p['arrival']].append(p['id'])

completed = []

while len(completed) < len(processes):
    if time in arrivals:
        for pid in arrivals[time]:
            queue.append(pid)

    if queue:
        pid = queue.popleft()
        exec_time = min(time_quantum, remaining[pid])
        print(f"{pid} runs from {time} to {time + exec_time}")
        time += exec_time
        remaining[pid] -= exec_time

        if time in arrivals:
            for new_pid in arrivals[time]:
                queue.append(new_pid)

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completed.append(pid)
    else:
        time += 1
