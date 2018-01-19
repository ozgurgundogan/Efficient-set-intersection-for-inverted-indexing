from Searchs import *

BinaryIntersection = 0
SVSIntersection = 1
ADBIntersection = 2
SEQIntersection = 3
MAXIntersection = 4


class Intersections():
    def __init__(self, type):
        self.type = type

    def intersect(self, list_of_input_lists):
        if (self.type == BinaryIntersection):
            return self.binary_intersect(list_of_input_lists)
        elif (self.type == SVSIntersection):
            return self.svs_intersect(list_of_input_lists)
        elif (self.type == ADBIntersection):
            return self.adp_intersect(list_of_input_lists)
        elif (self.type == SEQIntersection):
            return self.seq_intersect(list_of_input_lists)
        elif (self.type == MAXIntersection):
            return self.max_intersect(list_of_input_lists)

    def binary_intersect(self, list_of_input_lists, sorrt=True ,verbose=False):

        assert len(list_of_input_lists) == 2

        if(sorrt):
            # sort list wrt its length
            listsAreSortedWRTLength = sorted(list_of_input_lists, key=len)
        else:
            listsAreSortedWRTLength = list_of_input_lists

        intersectedArray = []

        # split short and long list
        shortList, longList = listsAreSortedWRTLength[0], \
                              listsAreSortedWRTLength[1]


        for x in shortList:
            # calculate golomb parameter
            golombParameter = int(len(longList) / len(shortList))

            # make a golomb search in long list, it returns overall offset
            y = golomb_search(longList, x, golombParameter)

            if (verbose):
                print " return eden overall offset : ", y

            # if elements are equal then append
            if (x == longList[y]):
                intersectedArray.append(x)
            else:
                if (verbose):
                    print " target was ", x, " found was ", longList[y]

        return intersectedArray

    def svs_intersect(self, list_of_input_lists):

        # sort list wrt its length
        listsAreSortedWRTLength = sorted(list_of_input_lists, key=len)

        numberOfLists = len(listsAreSortedWRTLength)

        # get shortest list
        shortestList = listsAreSortedWRTLength[0]

        intersectedArray = shortestList

        for i in range(1, numberOfLists):
            # DONE # TODO burada tekrar binary intersect'e giriyor tekrar tekrar liste sort ediliyor.
            intersectedArray = self.binary_intersect([intersectedArray, listsAreSortedWRTLength[i]], sorrt=False)

        return intersectedArray

    def adp_intersect(self, list_of_input_lists, verbose=False):

        def getListsAsSortedWRTLength(listsOfLists):
            return sorted(listsOfLists, key=len)

        def getEliminator(lst):

            return lst.pop(0)

        intersectedArray = []

        loil = list_of_input_lists

        while (1):
            # TODO burada her seferinde listeleri sort ediyor.
            listsAreSortedWRTLength = getListsAsSortedWRTLength(loil)

            # if first array is empty return
            if (len(listsAreSortedWRTLength[0]) == 0):
                return intersectedArray

            eliminator = getEliminator(listsAreSortedWRTLength[0])

            numberOfLists = len(listsAreSortedWRTLength)

            if (verbose):
                print eliminator

            unmatch = False
            for i in range(1, numberOfLists):

                '''
                it goes find an exact match or bigger match.
                if it finds exact match return True and restoflist
                if it finds bigger match return False and restoflist
                '''
                bool, newList = linearSearch(listsAreSortedWRTLength[i],eliminator)

                if (bool):
                    # replace list and keep continue
                    listsAreSortedWRTLength[i] = newList
                else:
                    # unmatch case or empty list case
                    if (len(newList) == 0):
                        # list is empty
                        return intersectedArray
                    else:
                        listsAreSortedWRTLength[i] = newList
                        unmatch = True
                        break
            if (not unmatch):
                intersectedArray.append(eliminator)
            loil = listsAreSortedWRTLength

    def seq_intersect(self, list_of_input_lists):

        def getListsAsSortedWRTLength(listsOfLists):
            return sorted(listsOfLists, key=len)

        def getEliminator(lst):
            return lst.pop(0)

        intersectedArray = []
        loil = list_of_input_lists

        # initially take the shortest array as eliminator
        listsAreSortedWRTLength = getListsAsSortedWRTLength(loil)

        if (len(listsAreSortedWRTLength[0]) == 0):
            return intersectedArray

        eliminator = getEliminator(listsAreSortedWRTLength[0])
        numberOfLists = len(listsAreSortedWRTLength)

        kingListIndex = 0
        while (1):

            #print eliminator
            unmatch = False
            for i in range(0, numberOfLists):
                ## eliminatori veren arrayi atla
                if (kingListIndex == i):
                    continue

                bool, newList = linearSearch(listsAreSortedWRTLength[i], eliminator)

                if (bool):
                    # keep continue
                    listsAreSortedWRTLength[i] = newList
                else:
                    #  empty list case
                    if (len(newList) == 0):
                        # list is empty
                        return intersectedArray

                    # unmatch case
                    else:
                        # unmatch and list are still full.
                        # take that list as kinglist
                        listsAreSortedWRTLength[i] = newList
                        eliminator = getEliminator(listsAreSortedWRTLength[i])
                        kingListIndex = i
                        unmatch = True
                        break
            # if there is no unmatch then continue with the same list
            if (not unmatch):
                intersectedArray.append(eliminator)
                listsAreSortedWRTLength = getListsAsSortedWRTLength(loil)
                if (len(listsAreSortedWRTLength[0]) == 0):
                    return intersectedArray
                eliminator = getEliminator(listsAreSortedWRTLength[0])
                kingListIndex = 0
            loil = listsAreSortedWRTLength



    def max_intersect(self, list_of_input_lists):

        def getEliminator(lst):

            if (len(lst) > 0):
                return lst.pop(0)
            else:
                return None

        lengthsorted = sorted(list_of_input_lists, key=len)
        intersectedArray = []

        eliminatorArrayLength = len(lengthsorted[0])
        x = getEliminator(lengthsorted[0])
        # start searching from the first list
        startat = 1

        while (x):

            for i in range(startat, len(lengthsorted)):
                print startat, x, eliminatorArrayLength

                # if any list is empty go back.
                if (len(lengthsorted[i]) == 0):
                    return intersectedArray

                y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i]) / eliminatorArrayLength))

                # if the value found by golomb bigger than x , then keep smallest array as eliminator generator.

                if (lengthsorted[i][y] > x):
                    x = getEliminator(lengthsorted[0])
                    # if new eliminator is also less than that value
                    if (lengthsorted[i][y] > x):
                        startat = 0
                        x = lengthsorted[i][y]
                    else:
                        startat = 1

                    break
                elif (i == len(lengthsorted) - 1):
                    intersectedArray.append(x)
                    x = getEliminator(lengthsorted[0])
                    startat = 1
        return intersectedArray
