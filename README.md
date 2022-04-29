# MPI4Py_ScatterGatherV
Modules to facilitate communication of arbitrarily sized arrays between an arbitrary number of processors.
* Author: Frank Cerasoli
* Date: 9/30/17
* Pre-requisites
  - Python
  - mpi4py
  - numpy
* Scatter distributes an array of arbitrary size among all processors, across the first dimension. The maximum difference in size from one segment to the next is +/- 1.
* Gather collects all arrays of arbitrary size into an array of size, N*array_size, where N is the number of processors.

*
* Test Usage:
  - 'mpirun -np 2 python main.py'
