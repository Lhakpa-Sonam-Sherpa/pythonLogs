pages = [1, 2, 3, 4, 5]


def lru_page_replacement(pages, capacity):
    """
    :param pages: list of page requests
    :param capacity: no of page frames in memory
    """
    memory = []  # Tracks pages in memory, recent at end
    page_faults = 0

    for page in pages:  # Process each page request
        if page in memory:  # Page HIT
            # Move to end (most recently used)
            memory.remove(page)
            memory.append(page)
            status = "HIT"
        else:  # Page MISS
            page_faults += 1
            status = "MISS"
            
            if len(memory) < capacity:  # Memory not full
                memory.append(page)
            else:  # Memory full
                # Remove least recently used (first item)
                memory.pop(0)
                memory.append(page)
        
        print(f"Request {page}: Memory {memory} ({status})")

    return page_faults

page_list = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
max_memory_capacity = 3

faults = lru_page_replacement(page_list, max_memory_capacity)
print(f"Total page faults : {faults}")