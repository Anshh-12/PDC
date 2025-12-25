from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
comm_size = comm.Get_size()
rank_id = comm.Get_rank()

# Generate local data based on rank
local_info = (rank_id + 2) * 3
gathered_data = comm.gather(local_info, root=0)

comp_results = []
do_something(3, comp_results)

if rank_id == 0:
    print(f"Master Rank 0 collected: {gathered_data}")
    for sender_rank, val in enumerate(gathered_data):
        print(f" -> Data from rank {sender_rank}: {val}")