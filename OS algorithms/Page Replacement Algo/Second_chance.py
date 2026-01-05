def second_chance_page_replacement(pages, capacity):
    """
    Docstring for second_chance_page_replacement
    
    :param pages: list of page requests
    :param capacity: No of page frames in memory
    """

    memory = []          # Pages in memory
    reference_bits = []  # Reference bits for each page
    pointer = 0          # Clock hand
    page_faults = 0

    for page in pages:
        if page in memory:
            # Page HIT → give second chance
            index = memory.index(page)
            reference_bits[index] = 1
            status = "HIT "
        else:
            # Page MISS
            page_faults += 1
            status = "MISS"

            if len(memory) < capacity:
                # Empty frame available
                memory.append(page)
                reference_bits.append(1)
            else:
                # Find page to replace
                while reference_bits[pointer] == 1:
                    reference_bits[pointer] = 0
                    pointer = (pointer + 1) % capacity

                # Replace page
                memory[pointer] = page
                reference_bits[pointer] = 1
                pointer = (pointer + 1) % capacity

        print(f"Request {page}: ({status}) Memory {memory}, Ref {reference_bits}")

    return page_faults


# Example input
page_list = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3

faults = second_chance_page_replacement(page_list, capacity)
print(f"Total page faults: {faults}")
