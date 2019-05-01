import random, timeit

def insertion_sort(array):

    # All elements after the wall are unsorted
    for wall in range(1, len(array)):
        element = array[wall] # first unsorted element

        # All elements before the wall are sorted
        e = wall-1
        while e >= 0:
            if element < array[e]:
                array[e+1] = array[e] # shift right
                array[e] = element # replace with element
            e-=1

    return array
# Randomly-generated size of Array
n = 26000

print("Generating unsorted arrays...")
print("========")
for z in range(1, 4):
    array = []
    for i in range(1, n):
        # Append random value to array
        array.append(random.randint(1, n))

    print("%d) Insertion Sort - Sorting..." % z)
    def timeMergeSort():
        insertion_sort(array)
    # Print n size of array, time to sort (ms)
    print("Sorted [%d] in <%f> seconds \n" % (n, timeit.timeit(timeMergeSort, number=1)))

print("========")