from communication import *
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



if __name__ == '__main__':
  x = None
  if rank == 0:
    print('Test started with %d processors.'%size)

    nrn = 5
    x = np.round(np.random.rand(nrn,nrn)*100)

    print('Total Array:\n%s\n'%x)

  comm.Barrier()

  x_scatt = scatter_array(x)

  time.sleep(float(rank)/10.)

  print('Rank %d:\n%s\n'%(rank,x_scatt))

MPI.Finalize()
