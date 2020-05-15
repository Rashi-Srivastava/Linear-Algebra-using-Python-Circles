import numpy as np
import matplotlib.pyplot as plt

P = np.array([4,7])

n = np.array([0,0])

O = n/2
print("O =",O)

# Calculating the PA*PB values
d = np.linalg.norm(P)**2 - 9
print("The product of PA and PB = ",d)
r = 3
theta = np.linspace(0,2*np.pi,100)

x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x,y,label="Circle 1")
plt.grid()
plt.axis("equal")
plt.title("gvv_linlag_2d_circle\n Question 3")
plt.show()
