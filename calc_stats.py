import numpy as np
def calc_stats(n):
  data=[]
  for line in open(n):
    row=[]
    for col in line.strip().split(','):
      row.append(float(col))
  data.append(row)
  return np.mean(data),np.median(data)
mean = calc_stats('data3.csv')
print(mean)
