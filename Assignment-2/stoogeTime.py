import random
import timeit
import math

# Implement MergeSort
def stoogeTime(array, n, m):
    if n == 2 and array[n] > array[m]:
        temp = array[n]
        array[n] = array[m]
        array[m] = temp
    if (m-n+1) > 2:
        mid = (int)((m-n+1)/3)
        stoogeTime(array, n, m-mid)
        stoogeTime(array, n+mid, m)
        stoogeTime(array, n, m-mid)


# Max value for size of array to sort
MAX_VALUE = 10000

# Size of Array
n = 250

array = []
for i in range(0, n):
    # Generate random value
    randomValue = random.randint(1, MAX_VALUE)
    # Append random value to array
    array.append(randomValue)


def timeStoogeSort():
    stoogeTime(array, 0, n - 1)

print("%d %f" % (n, timeit.timeit(timeStoogeSort, number=100)))
