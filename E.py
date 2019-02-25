import itertools
from functions import factorial
from Path import Path
from Graphics import *
import timeit


def exhaustive(num_of_points, points):
    temp = []
    paths = []
    for i in range(0, num_of_points - 1):
        temp.append(int(i + 1))

    permutation_array = list(itertools.permutations(temp))
    print("Exhaustive Running...")
    start_time = timeit.default_timer()
    for i in range(0, factorial(num_of_points - 1)):
        paths.append(Path())
        for j in range(0, num_of_points - 1):
            if j == 0:
                paths[i].distance = points[j].distances[permutation_array[i][j]]
            else:
                paths[i].distance += points[permutation_array[i][j-1]].distances[permutation_array[i][j]]
        paths[i].distance += points[permutation_array[i][num_of_points - 2]].distances[0]
        for j in range(0, num_of_points - 1):
            paths[i].route.append(permutation_array[i][j])
        paths[i].route.append(0)
    print("time is ", timeit.default_timer() - start_time)
    paths.sort(key=lambda x: x.distance, reverse=False)
    paths[0].show()
    answer_graphic(num_of_points, points, paths[0])
    return
