from main.Intersections import *

list1 = sorted([1, 0, 3, 899, 32323])

list2 = sorted([1, 0, 899, 32323, 7, 11, 3, 5, 65])

list3 = sorted([1, 0, 3, 11, 3, 5, 65])

list4 = sorted(range(0, 5))

intersector = Intersections(SVSIntersection)

print intersector.intersect([list1, list2, list3, list4])
