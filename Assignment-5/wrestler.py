import sys
from queue import Queue

my_graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def bfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            print(stack)
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def my_bfs(graph, start):
    visited = []
    que = Queue()
    visited.append(start)
    que.put(start)
    print("Root: {}\n".format(start))
    while not que.empty():
        vertex = que.get_nowait()
        print("Parent: {}".format(vertex))
        print("Unvisited Children: ", end='')
        for n in graph[vertex]:     # visit neighbors
            if n not in visited:
                print(n, end=' ')       # display source
                que.put(n)          # enqueue neighbor
                visited.append(n)   # visited neighbor
        print()
        print()


my_bfs(my_graph, 'A')


def readFile():
    babyfaces = []
    heels = []

    file = open(sys.argv[1], "r")
    line = file.readline()

    nWrestlers = int(line.split()[0])
    wrestlers = []
    for i in range(0, nWrestlers):
        line = file.readline()
        wrestler = str(line.split()[0])
        wrestlers.append(wrestler)

    line = file.readline()
    nRivalries = int(line.split()[0])
    for i in range(0, nRivalries):
        line = file.readline()
        wrestler1 = str(line.split()[0])
        wrestler2 = str(line.split()[1])

        if wrestler1 in heels and wrestler2 in heels:
            print("No")
            print("{} cannot fight {} because they are both Babyfacess...".format(wrestler1, wrestler2))
            exit()
        elif wrestler1 in babyfaces and wrestler2 in babyfaces:
            print("No")
            print("{} cannot fight {} because they are both Babyfacess...".format(wrestler1, wrestler2))
            exit()
        else:
            if wrestler1 in babyfaces and wrestler2 in heels:
                continue
            elif wrestler1 in heels and wrestler2 in babyfaces:
                continue
            elif wrestler1 in babyfaces and wrestler2 not in heels:
                heels.append(wrestler2)
            elif wrestler1 in heels and wrestler2 not in babyfaces:
                babyfaces.append(wrestler2)
            elif wrestler1 not in babyfaces and wrestler2 not in babyfaces:
                babyfaces.append(wrestler1)
                if wrestler2 not in heels:
                    heels.append(wrestler2)
            elif wrestler1 not in heels and wrestler2 not in heels:
                heels.append(wrestler1)
                if wrestler2 not in babyfaces:
                    babyfaces.append(wrestler2)
    print("Yes\n")
    print("Babyfaces: ")
    for bf in babyfaces:
        print(bf, end=' ')
    print()
    print("Heels: ")
    for h in heels:
        print(h, end=' ')
    print()


