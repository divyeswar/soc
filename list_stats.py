import numpy as np
def list_stats(a):
    
    n = len(a)
    if n== 0:
       return
    mean = np.mean(a)
    a.sort()
    mid = n//2 # 'n//2' gives the quotient of the division of n with 2
    if n%2 == 0:
        median = (a[mid] + a[mid - 1])/2
    else:
        median = a[mid]
    return median, mean
