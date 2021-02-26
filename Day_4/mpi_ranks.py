from mpi4y import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("The rank is:", rank) 

