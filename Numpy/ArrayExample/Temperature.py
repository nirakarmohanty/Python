import numpy as np
import matplotlib.pyplot as plt
cvalues = [20.4,21.1,22.2,22.8,23.0,22.6,22.1,21.5,21.2,20.4]
print("Print input values : ", cvalues)
cvalues_array=np.array(cvalues)
print("Print Numpy Array values : ",cvalues_array)
# Converting Celcius to Farenhite - C * 9 / 5 + 32
farenhite = np.array(cvalues_array*9/5+32)
print("Print Farenhite values : ",farenhite)

plt.plot(farenhite)
plt.show()
