import numpy as np
# Array declaration

A=[1,2,3]
print(A)

# converting Array to List

L = np.array([1,2,3])
print(L)
LConverting = np.array(A)
print(LConverting)

L1 = np.array([0,1,2])
L2 = np.array([4,5,6])

print("################### Mathematical Operation #############")

print("Adding Number [2] to Individual : ",L+2)
print("Finding Square of Individual : ",L*2)
print("Dividing a number :",L/3)
print("Adding two Arrays : ", L1+L2)
print("Subtracting two Arrays : ", L2-L1)

print("Square Root",np.sqrt(A))
print("Log of Array",np.log(A))
print("Expontial of Array" ,np.exp(A))


print("################### Shape of An Array#############")
s = L.size
print("Size of Array : ",s)
type = L.dtype
print("Data Type : ",type)

type_Float=np.array([1.2,2.3])
print("Data Type : ",type_Float.dtype)

print("######## 1 Dimension array ####################")

d= np.array([1,1,3,5,5,6,7,12,11,14,16])
v= np.array([1.98,1.23,3.0,5.34,5.5,0.36,0.7,0.012,1.1,1.04,1.086])

print("D :",d)
print("V :",v)

print("Type of D :",d.dtype)
print("Type of V :",v.dtype)

print("Dimension of D",np.ndim(d))
print("Dimension of D",np.ndim(v))

print("######## 2 Dimension array ####################")
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d)

print("######## Horizontal & Vertically Stack ####################")

A1 = np.array([1,2,3])
A2 = np.array([10,20,30])
print("Horizontal adding elements",np.hstack((A1,A2)))
print("Vertically adding elements ",np.vstack((A1,A2)))



print(" ############ Generate Random Numbers ############# ")
random_number=np.random.normal(5,0.5,12)
print("Random Number : ",random_number)

print("########### Arrange number #####################")
range = np.arange(1,20,2)
print(range)

range1 = np.arange(1,20)
print(range1)

range2= np.arange(20,1,-2)
print(range2)

print("################Line Space ####################")

line_space = np.linspace(1,10,num=10)
print("Linspace gives evenly spaced samples: ",line_space)

line_space1 = np.linspace(1,10,num=5)
print("Linspace gives evenly spaced samples: ",line_space1)

print(np.linspace(1,5,num=5))
print(np.linspace(1,5,num=10))

print(np.linspace(1,10,num=10))
print(np.linspace(1,5,num=15))

print(np.linspace(1,5,num=2,endpoint=False))


