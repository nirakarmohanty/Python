#Define simple List and print them
nameList=['Stela','Dia','Kiara','Anna']
print(nameList)

#List indexing
print(nameList[1],nameList[2],nameList[3])
print(nameList[-1],nameList[-2])

#length of List
print(len(nameList))

#Add a new list to the original list
nameList= nameList + ['Budapest','Croatia','Prague']

print(nameList)
print("Length of the List =", len(nameList))

# Slicing of list
print("print upto 3",nameList[:3])

#Assign values to list
nameList[3]='XXXX'
print("Assign at 3rd position ",nameList)
