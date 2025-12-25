from mpi4py import MPI
import numpy as np
import math

def do_something(it, out):
    for i in range(it):
        out.append(math.sqrt(i))

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    total = comm.size

    # Calculate grid dimensions automatically
    dim_x = int(np.floor(np.sqrt(total)))
    dim_y = total // dim_x

    # Create the virtual Cartesian topology
    grid_comm = comm.Create_cart(dims=(dim_x, dim_y), periods=(True, True), reorder=True)

    # Identify neighbors in the grid
    up, down = grid_comm.Shift(0, 1)
    left, right = grid_comm.Shift(1, 1)

    my_coords = grid_comm.Get_coords(rank)

    print(f"[Rank {rank}] Grid Pos: {my_coords}")
    print(f"   Neighbors -> N:{up}, S:{down}, W:{left}, E:{right}")

    # Process individual computation
    personal_results = []
    do_something(10 + rank, personal_results)