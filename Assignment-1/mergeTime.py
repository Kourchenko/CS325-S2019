import random
import timeit

# Implement MergeSort
def mergeSort(array):
    # Divide array if there's at least 1 value
    if (len(array) > 1):
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        # Merge the array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

# Max value for size of array to sort
MAX_VALUE = 10000
# Randomly-generated size of Array
n = 20000


for z in range(0, 3):
    array = []
    for i in range(1, n):
        # Generate random value
        randomValue = random.randint(1, MAX_VALUE)
        # Append random value to array
        array.append(randomValue)

    def timeMergeSort():
        mergeSort(array)

    print("%d %f" % (n, timeit.timeit(timeMergeSort, number=100)))

