class Path:
    def __init__(self):
        self.distance = 0
        self.route = []
        self.route.append(0)
        return

    def show(self):
        print("The answer is " + str(self.route) + " with distance of " + str(self.distance))
