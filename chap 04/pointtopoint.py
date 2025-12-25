from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.rank

# Direct messaging between specific processes
if rank == 0:
    packet = 5555
    comm.send(packet, dest=4)
    print(f"Rank 0 -> Sent {packet} to Rank 4")

elif rank == 1:
    packet = "MPI_MESSAGE"
    comm.send(packet, dest=8)
    print(f"Rank 1 -> Sent '{packet}' to Rank 8")

elif rank == 4:
    received_packet = comm.recv(source=0)
    print(f"Rank 4 <- Received {received_packet} from Rank 0")

elif rank == 8:
    received_packet = comm.recv(source=1)
    print(f"Rank 8 <- Received '{received_packet}' from Rank 1")

# Standard worker task
results = []
do_something(5, results)