# MPI4Py_ScatterGatherV
Author: Frank Cerasoli
Date: 9/30/17
* Pre-requisites
  - Python
  - mpi4py
  - numpy
Modules to facilitate communication of arbitrarily sized arrays between an arbitrary number of processors.
Scatter distributes an array of arbitrary among all processors over the first dimension. The maximum difference in size from one segment to the next is +/- 1.
Gather collects all arrays of arbitrary size into an array of size, N*array_size, where N is the number of processors.
