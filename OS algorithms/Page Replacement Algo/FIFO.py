#Page replacement Algorithm
#   1) FIFO

# Necessary base knowledge of python for implementing this algorithm

# lists
pages = [1, 2, 3, 4, 5]
pages.append(6) # adds 6 to the end of list [.., .., 5, 6]
pages.pop() # removes first value from the list [2, .., .., 5, 6]

# Queue's
from collections import deque as dq

queue = dq(pages)
queue.append(4)
queue.popleft()

# Set
memory_set_of_pages = {1, 2, 3, 4, 5}
if 4 in memory_set_of_pages:
    print("Hit : page in memory")


# Program:

def fifo_page_replacement(pages, capacity):
    """
    Docstring for fifo_page_replacement
    
    :param pages: list of page requests
    :param capacity: no of page frame in memory
    """
    memory = []
    page_falults = 0

    for page in pages: # a requested page from list of pages
        if page not in memory: # if its a Miss:
            page_falults += 1

            if len(memory) == capacity:
                memory.pop(0)

            memory.append(page)
        
        print(f"Request {page}: Memory {memory}")
    
    return page_falults

page_list = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
max_memory_capacity = 2

faults = fifo_page_replacement(page_list, max_memory_capacity)
print(f"Total page faults : {faults}")
