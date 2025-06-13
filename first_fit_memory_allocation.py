# First Fit memory allocation simulation

memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

allocation = [-1] * len(process_sizes)

for i in range(len(process_sizes)):
    for j in range(len(memory_blocks)):
        if memory_blocks[j] >= process_sizes[i]:
            allocation[i] = j
            memory_blocks[j] -= process_sizes[i]
            break

for i in range(len(process_sizes)):
    if allocation[i] != -1:
        print(f"Process {i+1} of size {process_sizes[i]} allocated in block {allocation[i]+1}")
    else:
        print(f"Process {i+1} of size {process_sizes[i]} not allocated")
