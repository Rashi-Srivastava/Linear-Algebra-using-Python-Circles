import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


A=np.array([2,3])
B=np.array([4,5])
X=np.array([-1,4])
c1=3

C=(A+B)/2
print(C)

m=dir_vec(B,A)
print(m)

Y=np.array([1,1])
c2=7

Aug=(Y,X)
print (Aug)

D=(c2,c1)

O= np.linalg.inv(Aug)@D
print(O)

r=np.linalg.norm(O-A)
print(r)



len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:], x_circ[1,:], label='$circumcircle$')
plt.plot(O[0],O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'o')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')





plt.show()
