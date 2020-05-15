import numpy as np
import matplotlib.pyplot as plt

#Equation of parabola
q=np.array([0,0])
r=np.array([0,1])
V=(q,r)
print("V=",V)

K=np.array([4,0])
u=-K/2
print("u=",u)

print("The equation of given parabola is", (q.T),"X",V,"x","-",K) 

a=K/4
print(a)
print("The value of 'a' for this parabola is = ", a[0]) 

print()
