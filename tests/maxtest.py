from main.Intersections import *

list1 = sorted([1, 2, 3, 4, 5])

list2 = sorted([1, 3, 4, 2])

list3 = sorted([0, 2, 3])

list4 = sorted([1, 2, 5, 6, 7, 3])

intersector = Intersections(MAXIntersection)

print intersector.intersect([list1, list2, list3, list4])
