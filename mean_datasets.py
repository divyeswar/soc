import numpy as np
  
def sets(n):
  data=[]
  for line in open(n):
    row=[]
    for col in line.strip().split(','):
      row.append(float(col))
    row=np.array(row)
    data.append(row)
  return np.array(data)  
def mean_datasets(n):
  m=len(n)
  data=np.array(sets(n[0]))
  for i in range(1,m):
    data=data+sets(n[i])
  return np.round(data/m,1)
print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
