# LRU Page Replacement Algorithm

pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 3
frames = []
page_faults = 0
recent = []

for page in pages:
    if page not in frames:
        page_faults += 1
        if len(frames) < frame_size:
            frames.append(page)
        else:
            lru = recent.pop(0)
            frames.remove(lru)
            frames.append(page)
    else:
        recent.remove(page)
    recent.append(page)
    print(f"Frames: {frames}")

print(f"Total page faults: {page_faults}")
