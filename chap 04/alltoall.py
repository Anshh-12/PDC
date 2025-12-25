from mpi4py import MPI
import numpy as np
from do_something import do_something

comm = MPI.COMM_WORLD
procs = comm.Get_size()
rank = comm.Get_rank()

# Each rank creates data to send to every other rank
outgoing = np.arange(procs, dtype=int) + (rank * 10)
incoming = np.empty(procs, dtype=int)

comm.Alltoall(outgoing, incoming)

storage = []
do_something(4, storage)

print(f"Rank {rank}: Sent {outgoing} | Received {incoming}")