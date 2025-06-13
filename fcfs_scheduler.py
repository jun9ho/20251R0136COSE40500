# fcfs_scheduler.py

processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 5},
    {'id': 'P2', 'arrival': 2, 'burst': 3},
    {'id': 'P3', 'arrival': 4, 'burst': 1},
]

processes.sort(key=lambda x: x['arrival'])

time = 0
for p in processes:
    if time < p['arrival']:
        time = p['arrival']
    print(f"{p['id']} starts at {time}")
    time += p['burst']
    print(f"{p['id']} finishes at {time}")
