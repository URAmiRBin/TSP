import matplotlib.pyplot as plt


def connect_points(p1, p2):
    x1, x2 = p1.xCord, p2.xCord
    y1, y2 = p1.yCord, p2.yCord
    plt.plot([x1, x2],[y1, y2])
    plt.pause(0.4)


def answer_graphic(num, points, path):
    xs = []
    ys = []
    for i in range(0, num):
        xs.append(points[i].xCord)
        ys.append(points[i].yCord)

    plt.scatter(xs, ys)

    for i in range(0, num):
        if i != num:
            connect_points(points[path.route[i]], points[path.route[i+1]])
        else:
            connect_points(points[path.route[i]], points[path.route[0]])
    plt.show()
