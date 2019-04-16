import random, timeit

MAX_VALUE = 10000 # Max value for size of array to sort

def insertSort(array):
    # Begin insertion 1 ahead of first position, we're comparing 0 and i
   for i in range(1,len(array)):

     currentvalue = array[i]
     position = i

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue

# Randomly-generated size of Array
n = 50000

print("Generating unsorted arrays...")
print("========")
for z in range(1, 4):
    array = []
    for i in range(1, n):
        # Append random value to array
        array.append(random.randint(1, MAX_VALUE))

    print("%d) Insertion Sort - Sorting..." % z)
    def timeMergeSort():
        insertSort(array)
    # Print n size of array, time to sort (ms)
    print("Sorted [%d] in <%f> seconds \n" % (n, timeit.timeit(timeMergeSort, number=100)))

print("========")