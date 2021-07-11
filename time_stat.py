import numpy as np
import statistics
import time

def time_stat(function, size, n):
  Time = 0
  for i in range(n):
    data = np.random.rand(size)
    # the np.random.rand(a) genertaes an array of a random numbers.
    a = time.perf_counter()
    # the time.perf_counter() takes the time from ur current device and notes it.
    res = func(data)
    Time =Time +time.perf_counter() - a # here again it takes the time and we are taking the difference between the times.
  return Time/n
