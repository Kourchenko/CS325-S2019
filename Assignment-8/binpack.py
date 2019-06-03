import sys, timeit, functools, random

def FIRST_FIT(items, limit):
    bins = []
    for item in items:
        placed = False
        if len(bins) == 0:
            bins.append(item)
        elif len(bins) > 0:
            for i in range(0, len(bins)):
                if bins[i] + item <= limit and not placed:
                    bins[i] += item
                    placed = True
            if not placed:
                bins.append(item)
    return len(bins)


def FIRST_FIT_DESC(items, limit):
    sorted_items = sorted(items, reverse=True)
    return FIRST_FIT(sorted_items, limit)


def BEST_FIT(items, limit):
    bins = []
    for item in items:
        if len(bins) == 0:
            bins.append(item)
        elif len(bins) > 0:
            leftovers = limit
            place_position = 0
            for i in range(0, len(bins)):
                # item will fit the limit and 0 =< item < leftovers
                if bins[i] + item <= limit and 0 <= limit - bins[i] - item and limit - bins[i] - item < leftovers:
                    leftovers = limit - bins[i] - item
                    place_position = i

            # no better fit was found, create a new bin
            if leftovers == limit:
                bins.append(item)
            else:
                # place bin at best fit position
                bins[place_position] += item
    return len(bins)

def time_first_fit(items, limit):
    FIRST_FIT(items, limit)

def time_first_fit_desc(items, limit):
    FIRST_FIT_DESC(items, limit)

def time_best_fit(items, limit):
    BEST_FIT(items, limit)


def read_file(_file):
    file = open(_file, "r")
    line = file.readline()

    test_cases = int(line.split()[0])

    for t in range(1, test_cases+1):
        line = file.readline()
        limit = int(line.split()[0])

        # number of items, can skip
        line = file.readline()

        # items
        line = file.readline()
        # split line by space " "
        temp = line.split()

        items = []

        # convert items to integers and add to list
        for i in temp:
            items.append(int(i))

        t_first_fit = timeit.Timer(functools.partial(time_first_fit, items, limit))
        t_first_fit_desc = timeit.Timer(functools.partial(time_first_fit_desc, items, limit))
        t_best_fit = timeit.Timer(functools.partial(time_best_fit, items, limit))

        print("Test Case %d "
              "First Fit: %d, <%f> seconds. "
              "First Fit Decreasing %d, <%f> seconds, "
              "Best Fit: %d, <%f> seconds."
              % (t,
                 FIRST_FIT(items, limit), t_first_fit.timeit(1),
                 FIRST_FIT_DESC(items, limit), t_first_fit_desc.timeit(1),
                 BEST_FIT(items, limit), t_best_fit.timeit(1)))


def run_random_test():
    LIST_SIZE = 1000
    for t in range(1, 21):

        items = []
        limit = 0
        for i in range(0, LIST_SIZE):
            v = random.randint(0, 100)
            items.append(v)
            if v > limit:
                limit = v

        t_first_fit = timeit.Timer(functools.partial(time_first_fit, items, limit))
        t_first_fit_desc = timeit.Timer(functools.partial(time_first_fit_desc, items, limit))
        t_best_fit = timeit.Timer(functools.partial(time_best_fit, items, limit))

        print("# OF ITEMS = %d: "
              "Test Case %d "
              "First Fit: %d, <%f> seconds. "
              "First Fit Decreasing %d, <%f> seconds, "
              "Best Fit: %d, <%f> seconds."
              % (LIST_SIZE,
                 t,
                 FIRST_FIT(items, limit), t_first_fit.timeit(1),
                 FIRST_FIT_DESC(items, limit), t_first_fit_desc.timeit(1),
                 BEST_FIT(items, limit), t_best_fit.timeit(1)))

        LIST_SIZE = LIST_SIZE + 1000


run_random_test()
