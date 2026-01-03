def optimal_page_replacement(pages, capacity):
    """
    :param pages: list of page requests (future is known)
    :param capacity: number of page frames in memory
    """
    memory = []  # Current pages in memory
    page_faults = 0

    for i, page in enumerate(pages):
        status = "HIT "
        if page not in memory:  # Page fault OR Miss
            page_faults += 1
            status = "MISS"
            if len(memory) < capacity:  # Memory not full
                memory.append(page)
            else:  # Memory full - need to replace a page
                # Find which page in memory will not be used for the longest time
                farthest_index = -1
                page_to_replace = -1
                
                for mem_page in memory:
                    # Check when this page will be used again
                    if mem_page in pages[i+1:]:  # Will be used again
                        # Find the index of next use
                        next_use_index = pages[i+1:].index(mem_page)
                        if next_use_index > farthest_index:
                            farthest_index = next_use_index
                            page_to_replace = mem_page
                    else:  # Will never be used again
                        page_to_replace = mem_page
                        break  # This is the best candidate
                
                # Replace the selected page
                memory.remove(page_to_replace)
                memory.append(page)
        
        print(f"Request {page}: ({status}) Memory {memory}")

    return page_faults
page_list = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
max_memory_capacity = 3

faults = optimal_page_replacement(page_list, max_memory_capacity)
print(f"Total page faults : {faults}")
