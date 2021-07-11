from astropy.io import fits
import numpy as np
def mean_fits(files):
  n = len(files)
  hdulist = fits.open(files[0])
  data = hdulist[0].data
  hdulist.close()
    
  for i in range(1, n):
    hdulist = fits.open(files[i])
    data += hdulist[0].data
    #the data + hdulist[0].data does not concatenate the lists but insted behaves as np.array and does element wise addition.
    hdulist.close() # closes the source of current hdulist. 
  mean = data / n
  return mean
