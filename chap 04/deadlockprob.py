from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 1:
    msg_out = "Message_A"
    # This will block if rank 5 is also in a recv state
    msg_in = comm.recv(source=5)
    comm.send(msg_out, dest=5)
    print(f"Rank 1 exchange complete.")

elif rank == 5:
    msg_out = "Message_B"
    # This will block if rank 1 is also in a recv state
    msg_in = comm.recv(source=1)
    comm.send(msg_out, dest=1)
    print(f"Rank 5 exchange complete.")