class Point:
    def __init__(self, x, y):
        self.xCord = x
        self.yCord = y
        self.visited = False
        self.distances = []
        return

    def show(self):
        print("X: " + str(self.xCord))
        print("Y: " + str(self.yCord))
        print("Visited: " + str(self.visited))
        print("Distances: " + str(self.distances))
        return

    def calculate_distances(self, num_of_points, points):
        for i in range(0, num_of_points):
            self.distances.append((((self.yCord - points[i].yCord) ** 2)
                                   + ((self.xCord - points[i].xCord) ** 2)) ** 0.5)
        return

    def go_to_near(self, num_of_points, points):
        self.visited = True
        min_value = 99999
        min_index = 0
        for i in range(0, num_of_points):
            if self.distances[i] > 0:
                if self.distances[i] < min_value:
                    if not points[i].visited:
                        min_value = self.distances[i]
                        min_index = i
        return min_index, min_value
