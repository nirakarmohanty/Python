import numpy as np

L=[1,2,3]
print('Array Declaration',L)
LAsNp= np.array([1,2,3])
print('Array as Numpy',LAsNp)

print("Printing through Looping")
for l in L:
    print(l)
print("========================")
for lasNp in LAsNp:
    print(lasNp)

print("Append value to List")
L.append(4)
print(L)

print("Append value to numpy List")
#LAsNp.append(4)
#print(LAsNp)

