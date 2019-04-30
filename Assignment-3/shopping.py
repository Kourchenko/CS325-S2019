import sys

def readFileDoShopping(fileName):
    file = open(fileName, "r")

    line = file.readline()

    currentLine = line.split()

    T = int(currentLine[0]) # 2 <- Convert first and only item in the line into an INT

    for t in range(0, T):
        line = file.readline() # read the next line

        currentLine = line.split()

        N = int(currentLine[0]) # 3 <- Convert first and only item in the line into an INT
        itemPriceArray = []

        itemWeightsArray = []

        for n in range(0, N):

            line = file.readline()

            currentLine = line.split()

            # There's only two numbers per line, convert them to int and add them to their corresponding arrays

            itemPriceArray.append(int(currentLine[0]))

            itemWeightsArray.append(int(currentLine[1]))

        # Now we want to know how many family members there are...
        line = file.readline()

        currentLine = line.split()

        familyMembers = []

        F = int(currentLine[0])

        for f in range(0, F):
            line = file.readline()

            currentLine = line.split()

            familyMembers.append(int(currentLine[0]))

        # Print out how much each family member can take
        totalPrice = 0
        for i in range(0, len(familyMembers)):
            w, l = shoppingSpree(familyMembers[i], itemWeightsArray, itemPriceArray, len(itemWeightsArray))
            totalPrice += w

        ##########################################
        # Store results in file named "results.txt"
        outputFile = open("results.txt", "a")
        ##########################################
        outputFile.write("Test Case {}".format(t+1))
        outputFile.write('\n')
        outputFile.write("Total Price {}".format(totalPrice))
        outputFile.write('\n')

        for fm in range(0, len(familyMembers)):
            w, l = shoppingSpree(familyMembers[fm], itemWeightsArray, itemPriceArray, len(itemWeightsArray))
            itemsToString = ""
            if (len(l) == 0):
                for item in l:
                    itemsToString += str(item) + " "
                outputFile.write("\t {}: {}".format(fm+1, None))
                outputFile.write('\n')
                totalPrice += w
            else:
                for item in l:
                    itemsToString += str(item) + " "
                outputFile.write("\t {}: {}".format(fm+1, itemsToString))
                outputFile.write('\n')
                totalPrice += w
    outputFile.close()

# Do your shopping algorithm here

def shoppingSpree(maxWeight, itemWeights, itemPrices, n):
    sol = [[0 for x in range(maxWeight + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for mw in range(maxWeight + 1):
            # Don't store values with no weight
            if i == 0 or mw == 0:
                sol[i][mw] = 0
            elif itemWeights[i - 1] <= mw:
                sol[i][mw] = max(itemPrices[i - 1] + sol[i - 1][mw - itemWeights[i - 1]], sol[i - 1][mw])
            else:
                sol[i][mw] = sol[i - 1][mw]

    # Store the optimal solution, the last solution in our array
    optimalSol = sol[n][maxWeight]

    valuesUsed = []
    w = maxWeight
    for i in range(n, 0, -1):
        if optimalSol <= 0:
            break
        if optimalSol == sol[i - 1][w]:
            continue
        else:

            # Add the item used into position 0
            valuesUsed.insert(0, i-1+1)

            # Since this weight is included
            # its value is deducted
            optimalSol = optimalSol - itemPrices[i - 1]
            w = w - itemWeights[i - 1]

    return sol[n][maxWeight], valuesUsed


itemWeights = [2, 3, 4, 5]
itemPrices = [10, 2, 5, 6]

r = shoppingSpree(8, itemWeights, itemPrices, 4)
print(r)
