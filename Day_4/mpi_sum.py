
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

sum_the_ranks = comm.Get_size()

sums = 
if rank != 0:
	comm.send(rank, dest = 0)
else:
	for i in range(1,sum_the_ranks):
		sums += comm.recv(source = i)
	print(sums)



