import sys


def readFileIn(fileName):
    file = open(fileName, "r")
    line = file.readline()

    setsCompleted = 1
    # While we have the next line
    while line:
        currentLine = line.split()
        activitiesN = int(currentLine[0])


        activities = [0] * activitiesN
        activityStartArray = [0] * activitiesN
        activityEndArray = [0] * activitiesN

        for i in range(0, activitiesN):
            # read line
            line = file.readline()
            # split line
            currentLine = line.split()

            # activity number, start time, end time
            # Place into position, activity number
            activities[i] = int(currentLine[0])
            activityStartArray[i] = int(currentLine[1])
            activityEndArray[i] = int(currentLine[2])

        # Sorted Activity Prime, Activity Start Prime, Activity End Prime
        aP, aSP, aEP = sortByFinishTime(activities, activityStartArray, activityEndArray)

        A = greedyActivitySelector(aP, aSP, aEP)
        str1 = ''
        for i in range(0, len(A)-1):
            str1 += str(A[i]) + " "
        str1 += str(A[-1])
        print("Set {}".format(setsCompleted))
        print("Number of activities selected = {}".format(len(A)))
        print("Activities: {}".format(str1))
        print("")
        setsCompleted += 1
        line = file.readline()


def greedyActivitySelector(activities, start, finish):
    n = len(start)

    # activities
    A = []
    A.append(activities[0])
    i = 1
    for m in range(2, n):
        if start[m] >= finish[i]:
            A.append(activities[m])
            i = m
    return A

def sortByFinishTime(array1, arrayStart, arrayEnd):
    for i in range(0, 3):
        for j in range(0, 3):
            if (i != j and arrayEnd[i] < arrayEnd[j]):
                tempStart = arrayStart[i]
                tempEnd = arrayEnd[i]
                tempA = array1[i]

                # Swap activity number
                array1[i] = array1[j]
                array1[j] = tempA

                # Swap arrayStart values
                arrayStart[i] = arrayStart[j]
                arrayStart[j] = tempStart

                # Swap arrayEnd values
                arrayEnd[i] = arrayEnd[j]
                arrayEnd[j] = tempEnd
            elif arrayEnd[j] < arrayEnd[i]:
                tempStart = arrayStart[i]
                tempEnd = arrayEnd[i]
                tempA = array1[i]

                # Swap activity number
                array1[i] = array1[j]
                array1[j] = tempA

                # Swap arrayStart values
                arrayStart[i] = arrayStart[j]
                arrayStart[j] = tempStart

                # Swap arrayEnd values
                arrayEnd[i] = arrayEnd[j]
                arrayEnd[j] = tempEnd

    return array1, arrayStart, arrayEnd


readFileIn(sys.argv[1])