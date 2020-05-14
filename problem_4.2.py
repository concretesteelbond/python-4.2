import random
import statistics
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))

def problem4_2(numList):
    """ Compute the mean and standard deviation of a list of floats """
    print(statistics.mean(numList))
    print(statistics.stdev(numList))
