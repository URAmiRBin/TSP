from Path import *


def nearest_neighbour(num_of_points, points):
    answer = Path()
    source = 0
    print("Nearest Neighbour Running...")
    for i in range(0, num_of_points - 1):
        source, distance = points[source].go_to_near(num_of_points, points)
        answer.route.append(source)
        answer.distance += distance
    answer.distance += points[source].distances[0]
    answer.route.append(0)
    answer.show()
    return
