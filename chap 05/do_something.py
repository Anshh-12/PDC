import math

def do_something(item_count, data_store):
    """
    Standard worker function used across various concurrency scripts.
    """
    for val in range(item_count):
        # Perform calculation and store result
        computed_val = math.pow(math.sqrt(val), 2)
        data_store.append(computed_val)