# Producer-Consumer problem with threading and semaphore

import threading
import time
import random

buffer = []
buffer_size = 5

empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    for _ in range(10):
        item = random.randint(1, 100)
        empty.acquire()
        with mutex:
            buffer.append(item)
            print(f"Produced: {item}")
        full.release()
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for _ in range(10):
        full.acquire()
        with mutex:
            item = buffer.pop(0)
            print(f"Consumed: {item}")
        empty.release()
        time.sleep(random.uniform(0.1, 0.5))

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()
