from main.Intersections import *


list3 = sorted([0, 2, 8 , 15])

list2 = sorted([11 , 15 , 17 , 36 , 47])

list1 = sorted([1, 2, 3, 4, 5 , 15])

list4 = sorted([1, 2, 5, 6, 7, 3 ,15])
# list4 = sorted([1, 2, 5, 6, 3, 8])

intersector = Intersections(MAXIntersection)



print intersector.intersect([list1, list2, list3, list4])
