# Semaphore synchronization example

import threading
import time

semaphore = threading.Semaphore(2)

def task(name):
    print(f"{name} waiting to enter critical section")
    with semaphore:
        print(f"{name} entered critical section")
        time.sleep(2)
        print(f"{name} exiting critical section")

threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
