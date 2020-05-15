import numpy as np

n=np.array([-4,6])
O1 = -n/2
print(O1)
O2 = np.array([-3,2]) 
O = O1.transpose()
print(O)
r1=np.sqrt((O1@O)-12)
print(r1)
n=np.linalg.norm(O1-O2)
print(n)
r2=np.sqrt(n**2-r1**2)
print(r2)
