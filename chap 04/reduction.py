import numpy as np
from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
my_id = comm.rank

# Create a simple numpy array
array_len = 8
local_array = np.full(array_len, my_id + 1, dtype=np.int32)
result_sum = np.zeros(array_len, dtype=np.int32)

# Perform a sum reduction across all processes
comm.Reduce(local_array, result_sum, op=MPI.SUM, root=0)

if my_id == 0:
    work_list = []
    do_something(5, work_list)
    print(f"Final Reduced Array at Root: {result_sum}")