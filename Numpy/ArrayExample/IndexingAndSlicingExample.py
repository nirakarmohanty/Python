import numpy as np
print("###### Indexing and Slicing ##################")

list_indexing = np.array([(1,2,3),(4,5,6)])
print(list_indexing)

print("First Row",list_indexing[0])
print("Second Row",list_indexing[1])

print("First Column ",list_indexing[:,0])
print("Second Column ",list_indexing[:,1])
print("Third Column ",list_indexing[:,2])


print("Second Row First two values",list_indexing[1,:2])
print("Second Row second two value",list_indexing[1,1:3])
