import random
import timeit

def insertSort(array):
    # Begin insertion 1 ahead of first position, we're comparing 0 and i
   for i in range(1,len(array)):

     currentvalue = array[i]
     position = i

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue

# Max value for size of array to sort
MAX_VALUE = 10000
# Randomly-generated size of Array
n = 10000

for i in range(0, 3):
    array = []
    for i in range(1, n):
        # Generate random value
        randomValue = random.randint(1, MAX_VALUE)
        # Append random value to array
        array.append(randomValue)

    def timeInsertSort():
        insertSort(array)

    print("%d %f" % (n, timeit.timeit(timeInsertSort, number=100)))