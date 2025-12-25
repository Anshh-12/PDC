import math

def do_something(iterations, results_container):
    """
    Simulates a heavy computational workload.
    """
    for count in range(iterations):
        # Perform a calculation to mimic CPU activity
        calc = math.pow(math.sqrt(count), 2)
        results_container.append(calc)