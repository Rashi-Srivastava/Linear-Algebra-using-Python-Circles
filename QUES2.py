import numpy as np


P=np.array([2,2])
O2=np.array([-1,2])
O=O2.transpose()
print(O)
r2=np.sqrt(4+O@O2)
print(r2)
O1=2*P-O2
print(O1)
m=np.array([1,0])
a=1
b=-10
c=20
d1=(-b+np.sqrt((b*b)-(4*a*c)))/2*a
print(d1)
d2=(-b-np.sqrt((b*b)-(4*a*c)))/2*a
print(d2)
