import numpy as np
from coeffs import *


L1=np.array([1,1])
C1=3

K=np.array([-2,0])

O1 = -K/2
print(O1)

r1 = O1.T@O1
print(r1)

L2 = omat@L1
print(L2)

C2 = L2.T@O1
print(C2)

X=(L1,L2)
Y=(C1,C2)
P=np.linalg.inv(X)@Y
print(P)

O2 = (2*P)-O1
print(O2)




