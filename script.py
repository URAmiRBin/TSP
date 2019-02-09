from numpy import *
import fileinput
import itertools
import sys
import Point

Input = fileinput.input(sys.argv[1])
numOfPoints = int(Input[0])
points = []
for line in Input:
    lineNumbers = [int(n) for n in line.split()]
    points.append(Point(lineNumbers[0], lineNumbers[1]))
