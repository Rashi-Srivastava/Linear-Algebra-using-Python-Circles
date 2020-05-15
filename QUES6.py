import numpy as np

P=np.array([-2,4])
Q=np.array([0,2])
N1=np.array([0,1])
c1=N1@Q
print(c1)
N2 = 2*(P-Q)
print(N2)
M1=np.linalg.norm(P)
print(M1)
M2=np.linalg.norm(Q)
print(M2)
c2=(M1**2)-(M2**2)
print(c2)
Aug1=(N1,N2)
Aug2=(c1,c2)
O=np.linalg.inv(Aug1)@(Aug2)
print(O)

opt_d1=np.array([4,5])
opt_s1=6

opt_d2=np.array([2,-3])
opt_s2=-10

opt_d3=np.array([3,4])
opt_s3=3

opt_d4=np.array([5,2])
opt_s4=-4

if int(opt_d1@O)==opt_s1:
	print("Option A is correct.")
	
if int(opt_d2@O) == opt_s2:
	print ( "Option B is correct.")
	
if int(opt_d3@O)==opt_s3:
	print("Option C is correct")
		
if int(opt_d4@O)==opt_s4:
	print("Option D is correct.")
