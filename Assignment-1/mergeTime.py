import random
import timeit
# Max value for size of array to sort
MAX_VALUE = 10000

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


# Randomly-generated size of Array
n = 1000

print("Generating unsorted arrays...")
print("========")
for z in range(1, 4):
    array = []
    for i in range(1, n):
        # Append random value to array
        array.append(random.randint(1, MAX_VALUE))

    print("%d) Merge Sort - Sorting..." % z)
    def timeMergeSort():
        mergeSort(array)
    # Print n size of array, time to sort (ms)
    print("Sorted [%d] in <%f> seconds \n" % (n, timeit.timeit(timeMergeSort, number=100)))

print("========")
