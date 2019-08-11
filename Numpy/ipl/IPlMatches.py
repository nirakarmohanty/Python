# from pandas import pd
import pandas as pd

# read data through panda
matches_data = pd.read_csv('OriginalMatches.csv', sep=',', header=None,skiprows=1)
print(matches_data[1][1])
# Convert data frame to Numpy
npy_data = matches_data.values
# Set to hold YEAR
year_set = set()
# Dictionary to hold {Place,Count}
place_dictionary = {}
for data in npy_data:
    # print("Match played at {} on {}".format(data[2],data[1]))
    year_set.add(data[1])
    if data[2] in place_dictionary:
        count = place_dictionary.get(data[2])
        place_dictionary[data[2]] = count + 1
    else:
        place_dictionary[data[2]] = 1

print("Year : ",year_set)
print("Places with count : ", place_dictionary)
