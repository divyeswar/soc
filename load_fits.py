from astropy.io import fits
import numpy as np

def load_fits(filename):
  hdulist = fits.open(filename)
  data = hdulist[0].data
#the data consists of an array similiar to a matrix of data.shape(like 200*200)

  arg_max = np.argmax(data)  
 #the np.argmax finds the index of the maximum value of the data by converting it into a 1d array
  max_pos = np.unravel_index(arg_max, data.shape)
# the np.unravel_index gives the position of the max index obtained by argmax in the forms of data.shape.
  
  return max_pos
