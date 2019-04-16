import math, sys

# Implement MergeSort
def stoogeSort(array, n, m):
    if array[n] > array[m]:
        temp = array[n]
        array[n] = array[m]
        array[m] = temp
    if (m-n+1) > 2:
        mid = (int)((m-n+1)/3)
        stoogeSort(array, n, m-mid)
        stoogeSort(array, n+mid, m)
        stoogeSort(array, n, m-mid)

# Read first argument passed through command line
file = open(sys.argv[1], "r")
line = file.readline()

# Output file open for writing
outputFile = open("insert.txt", "a")
# While file.readline() has a line
while line:
    # Split file.readline() by spaces
    currentLine = line.split()

    # Count of numbers to sort
    count = int(currentLine[0])

    # Get values from line and convert into an array
    values = currentLine[1:]

    # Convert values into integers
    intValues = []
    for i in values:
        if i != '' or i != '\n':
            intValues.append(int(i))
    # Do sort
    stoogeSort(intValues, 0, count-1)

    # Write each sorted integer to the output file
    for i in intValues:
        outputFile.write("%d " % i)
    outputFile.write('\n')

    line = file.readline()

# Close the outputFile
outputFile.close()