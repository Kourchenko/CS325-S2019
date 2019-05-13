import sys

def readFile():
    babyfaces = []
    heels = []

    file = open(sys.argv[1], "r")
    line = file.readline()

    nWrestlers = int(line.split()[0])
    wresters = []
    for i in range(0, nWrestlers):
        line = file.readline()
        wrestler = str(line.split()[0])
        wrester.append(wrestler)

    line = file.readline()
    nRivalries = int(line.split()[0])
    for i in range(0, nRivalries):
        line = file.readline()
        wrestler1 = str(line.split()[0])
        wrestler2 = str(line.split()[1])

        if wrestler1 not in babyfaces or wrestler1 not in heels:
            if wresteler2 not in babyfaces or wrestler2 not in heels:
                babyfaces.append(wrester1)
                heels.append(wrester2)
            elif wrester2 in babyfaces:
                heels.append(wrester1)
            elif wrester2 in heels:
                babyfaces.append(wrester1)
        elif wrester1 in babyfaces:
            if wrester2 in babyfaces:
                print("No, cannot make rivalries, both wrestlers are in the same group...")
                exit()
        elif wrester1 in heels:
            if wrester2 in heels:
                print("No, cannot make rivalries, both wrestlers are in the same group...")
                exit()
    print("Yes\n")
    print("Babyfaces: ")
    for bf in babyfaces:
        print(bf + " ")
    print()
    print("Heels: ")
    for h in heels:
        print(h + " ")
    print()


readFile()