import pandas as pd
from numpy.core._multiarray_umath import ndarray


class IPLMatchUtil:
    year = 0
    place = ''

    def __init__(self):
        print('IPL Match Util class')

def read_IPLData():
    print("Reading IPL data")
    matches_data = pd.read_csv('OriginalMatches.csv', sep=',', header=None,skiprows=1)
    # Convert data frame to Numpy
    npy_data = matches_data.values
    return npy_data
#Method returns all years
def print_years(result):
    year_set=set()
    for data in result:
        year_set.add(data[1])
    return year_set

def getDeatails_on_perticularDate(date):
    resulted_data = ''
    all_data=read_IPLData()
    for data in all_data:
        if(date == data[3]):
            resulted_data = data
            return resulted_data

iplMatchObject = IPLMatchUtil()
print(iplMatchObject)
noOfMatches: ndarray=read_IPLData()
print("Total no of Matches played till now is {}".format(noOfMatches.size))
totalYear=print_years(noOfMatches)
print('IPL year in sorted  ', sorted(totalYear))
print("So, IPL Started on {}".format(list(sorted(totalYear))[0]))

dataForTheData=getDeatails_on_perticularDate('05-04-2017')
print("On this Date:{} Team-1 {} and team-2 {} were playing  at {}."
      .format(dataForTheData[3],dataForTheData[4],dataForTheData[5],dataForTheData[14]))
