def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def calculate_all(num_of_points, points):
    for i in range(0, num_of_points):
        points[i].calculate_distances(num_of_points, points)
    return
