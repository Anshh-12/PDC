from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()

# Initialize data on the root process
if my_rank == 0:
    data_to_distribute = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
else:
    data_to_distribute = None

# Distribute chunks of data
received_value = comm.scatter(data_to_distribute, root=0)

output_list = []
do_something(5, output_list)

print(f"Process {my_rank} received value: {received_value}. Done.")