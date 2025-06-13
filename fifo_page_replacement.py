# FIFO Page Replacement Algorithm

pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 3
frames = []
page_faults = 0

for page in pages:
    if page not in frames:
        page_faults += 1
        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
    print(f"Frames: {frames}")

print(f"Total page faults: {page_faults}")
