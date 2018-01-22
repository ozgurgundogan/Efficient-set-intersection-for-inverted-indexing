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


        for ind in range(len(shortList)):
            # calculate golomb parameter

            x = shortList[ind]
            golombParameter = int(len(longList) / (len(shortList)-ind))

            # if(golombParameter > 40):
            #     golombParameter = 10
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
            # if returned array is empty no more intersection needed.
            if(len(intersectedArray)==0):
                return intersectedArray

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
                #bool, newList = linearSearch(listsAreSortedWRTLength[i],eliminator)
                bool, newList = binary_search2(listsAreSortedWRTLength[i], 0, len(listsAreSortedWRTLength[i]) - 1,
                                               eliminator)

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

                #bool, newList = linearSearch(listsAreSortedWRTLength[i], eliminator)
                bool, newList = binary_search2(listsAreSortedWRTLength[i], 0, len(listsAreSortedWRTLength[i]) - 1,
                                               eliminator)

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



    def max_intersect(self, list_of_input_lists, verbose=False):

        def getListsAsSortedWRTLength(listsOfLists):
            return sorted(listsOfLists, key=len)

        def getEliminator(lst, popit=True):

            if (len(lst) > 0):
                if(popit):
                    return lst.pop(0)
                else:
                    return lst[0]
            else:
                return None


        lengthsorted = getListsAsSortedWRTLength(list_of_input_lists)
        intersectedArray = []

        # init values
        x = getEliminator(lengthsorted[0])
        eliminatorListIndex = 0
        # start searching from the first list initially
        startat = 1
        eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])

        while (x != None):

            if(verbose):
                print "eliminator" , x , "startat list", startat,

            for i in range(startat, len(lengthsorted)):
                # print startat, x, eliminatorArrayLength

                # if any list is empty go back.
                if (len(lengthsorted[i]) == 0):
                    return intersectedArray

                # golomb search gives equal value or bigger value. if it gives a value less than search item then that list ends.
                # y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i]) / eliminatorArrayLength))

                if(len(lengthsorted[0])==0):
                    y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i])))
                else:

                    y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i]) / len(lengthsorted[0])))

                if (verbose):
                    print "found y" , lengthsorted[i][y] , "in list" , lengthsorted[i]

                valfound = lengthsorted[i][y]

                # remove previous value of the array,
                # arrayin yeni halinde bizim eleman artik yok
                lengthsorted[i] = lengthsorted[i][y:]

                # print len(lengthsorted[0]),len(lengthsorted[1])
                if(i==0):
                    if (valfound > x):
                        x = getEliminator(lengthsorted[0], popit=True)
                        startat = 1
                    elif (valfound < x):
                        return intersectedArray


                elif(i==1):
                    if (valfound > x):
                        x = getEliminator(lengthsorted[0], popit=False)
                        if (valfound > x):
                            dummy = getEliminator(lengthsorted[0], popit=True)
                            startat = 0
                            x = valfound
                        else:
                            x = getEliminator(lengthsorted[0], popit=True)
                            startat = 1

                        break
                    elif (valfound < x):
                        return intersectedArray
                    #eger liste 2 lik ise buraya girmemiz gerekiyor
                    elif (valfound == x):
                        if(len(lengthsorted)==2):
                            if (verbose):
                                print "found : ", x, " eliminator index ", eliminatorListIndex
                            intersectedArray.append(x)
                            # TODO there is a problem here, will we keep get eliminator from the list which previous eliminator is taken or will we get eliminator from first list ?

                            x = getEliminator(lengthsorted[0], popit=True)
                            startat = 1

                            for i in range(startat, len(lengthsorted)):
                                dmmy = getEliminator(lengthsorted[i],popit=True)

                            if(verbose):
                                for i in range(len(lengthsorted)):
                                    print "arr " , i , lengthsorted[i]

                else:
                    if(valfound!=x):
                        # not found rest list
                        # get a new eliminator from 0 and start with 1
                        x = getEliminator(lengthsorted[0], popit=True)
                        startat = 1
                        break
                    else:

                        if ((i == len(lengthsorted) - 1)):

                            if (verbose):
                                print "found : ", x, " eliminator index ", eliminatorListIndex
                            intersectedArray.append(x)
                            # TODO there is a problem here, will we keep get eliminator from the list which previous eliminator is taken or will we get eliminator from first list ?

                            x = getEliminator(lengthsorted[0], popit=True)
                            startat = 1

                            for i in range(startat, len(lengthsorted)):
                                dmmy = getEliminator(lengthsorted[i],popit=True)

                            if(verbose):
                                for i in range(len(lengthsorted)):
                                    print "arr " , i , lengthsorted[i]
        # eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])

        return intersectedArray
