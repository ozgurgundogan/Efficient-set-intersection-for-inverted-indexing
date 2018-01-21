from main.Intersections import *


list3 = sorted([0, 2,  8 , 9 ,15 ])

list4 = sorted([4 , 7 , 8, 5, 6, 15,36 ])

list2 = sorted([2,3 ,4 ,8, 9, 11, 15 , 17 ,36])

list1 = sorted([1, 2, 3, 4, 5 ,8, 15, 17, 34])


# list4 = sorted([1, 2, 5, 6, 3, 8])

intersector = Intersections(MAXIntersection)



print intersector.intersect([list1, list2, list3, list4])
