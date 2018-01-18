from main.Intersections import *
import random

# since intersectors manipulates the arrays , we are going to keep array beside.
_c1 = sorted(list(set(random.sample(range(10), 3))))
_c2 = sorted(list(set(random.sample(range(10), 5))))
_c3 = sorted(list(set(random.sample(range(10), 6))))
_c4 = sorted(list(set(random.sample(range(10), 4))))

print _c1, _c2, _c3, _c4

c1 = list(_c1)
c2 = list(_c2)
c3 = list(_c3)
c4 = list(_c4)
intersector = Intersections(BinaryIntersection)
pre_1 = intersector.intersect([c1, c2])

c1 = list(_c1)
c2 = list(_c2)
c3 = list(_c3)
c4 = list(_c4)
intersector = Intersections(SVSIntersection)
pre_2 = intersector.intersect([c1, c2, c3, c4])

c1 = list(_c1)
c2 = list(_c2)
c3 = list(_c3)
c4 = list(_c4)
intersector = Intersections(ADBIntersection)
pre_3 = intersector.intersect([c1, c2, c3, c4])

c1 = list(_c1)
c2 = list(_c2)
c3 = list(_c3)
c4 = list(_c4)
intersector = Intersections(SEQIntersection)
pre_4 = intersector.intersect([c1, c2, c3, c4])

print pre_1, pre_2, pre_3, pre_4
