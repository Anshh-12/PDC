from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    shared_val = 1024  # Value to send to everyone
else:
    shared_val = None

# Spread the value to all ranks
shared_val = comm.bcast(shared_val, root=0)

temp_results = []
# Use shared value to determine workload
do_something(shared_val // 100, temp_results)

print(f"Rank {rank} has the broadcasted value: {shared_val}")