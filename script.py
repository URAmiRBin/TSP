from numpy import *
from Point import Point
from NN import nearest_neighbour
from E import exhaustive
from functions import calculate_all
import fileinput
import sys

Input = fileinput.input(sys.argv[1])
numOfPoints = int(Input[0])
points = []
for line in Input:
    lineNumbers = [int(n) for n in line.split()]
    points.append(Point(lineNumbers[0], lineNumbers[1]))


calculate_all(numOfPoints, points)
if sys.argv[2] == 'n':
    nearest_neighbour(numOfPoints, points)
else:
    exhaustive(numOfPoints, points)
