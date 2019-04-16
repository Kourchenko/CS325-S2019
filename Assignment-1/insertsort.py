import sys


def insertSort(array):
    # Begin insertion 1 ahead of first position, we're comparing 0 and i
   for i in range(1,len(array)):

     currentvalue = array[i]
     position = i

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue

# Read first argument passed through command line
file = open(sys.argv[1], "r")
line = file.readline()

# Output file open for writing
outputFile = open("insert.txt", "a")
# While file.readline() has a line
while line:
    # Count of numbers to sort
    count = int(line[0])

    # Get values from line and convert into an array
    values = line[1:].split()

    # Convert values into integers
    intValues = []
    for i in values:
        if i != '' or i != '\n':
            intValues.append(int(i))

    # Do Merge-sort
    insertSort(intValues)

    # Write each sorted integer to the output file
    for i in intValues:
        outputFile.write("%d " % i)
    outputFile.write('\n')

    line = file.readline()

# Close the outputFile
outputFile.close()