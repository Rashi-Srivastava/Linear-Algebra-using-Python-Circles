import numpy as np

P=np.array([1,-1])
L1=np.array([2,1])
c1=3
L2=np.array([1,-1])
c2=1
X=(L1,L2)
Y=(c1,c2)
O=np.linalg.inv(X)@Y
print(O)
n=O-P
print (n)
N=n.transpose()
C=N@P
print(C)
print("The equation of the desired tangent is",n,"x =",C)
