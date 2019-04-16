import sys

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

# Read first argument passed through command line
file = open(sys.argv[1], "r")
line = file.readline()

# Output file open for writing
outputFile = open("merge.txt", "a")
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
    mergeSort(intValues)

    # Write each sorted integer to the output file
    for i in intValues:
        outputFile.write("%d " % i)
    outputFile.write('\n')

    line = file.readline()

# Close the outputFile
outputFile.close()