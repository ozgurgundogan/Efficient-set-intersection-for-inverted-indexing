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




    def max_intersect(self, list_of_input_lists, verbose=True):

        def getEliminator(lst):

            if (len(lst) > 0):
                return lst.pop(0)
            else:
                return None

        lengthsorted = sorted(list_of_input_lists, key=len)
        intersectedArray = []

        x = getEliminator(lengthsorted[0])
        eliminatorListIndex = 0
        # start searching from the first list
        startat = 1

        while (x != None):

            if(verbose):
                print "eliminator" , x , "from" , eliminatorListIndex , "startat list", startat,
            eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])


            for i in range(startat, len(lengthsorted)):
                # print startat, x, eliminatorArrayLength

                # if any list is empty go back.
                if (len(lengthsorted[i]) == 0):
                    return intersectedArray

                # golomb search gives equal value or bigger value. if it gives a value less than search item then that list ends.
                y = golomb_search(lengthsorted[i], x, 1)
                if (verbose):
                    print "found y" , lengthsorted[i][y] , "in list" , lengthsorted[i] , "ind" , i

                valfound = lengthsorted[i][y]
                lengthsorted[i] = lengthsorted[i][y:]


                # print x
                # if the value found by golomb bigger than x , then keep smallest array as eliminator generator.
                if (valfound > x):
                    x = getEliminator(lengthsorted[0])
                    # if new eliminator is also less than that value
                    if (valfound > x):
                        startat = 0
                        x = valfound
                        # update eliminator list index
                        eliminatorListIndex = i
                        # break
                    else:
                        # DONT update eliminator index
                        startat = 1

                    ## if not found in that list , then break it up
                    break

                # if
                elif(valfound < x):
                    return intersectedArray
                    # x = getEliminator(lengthsorted[0])
                    # break

                elif ((i == len(lengthsorted) - 1)):
                    if (verbose):
                        print "found : " , x
                    intersectedArray.append(x)
                    x = getEliminator(lengthsorted[0])
                    startat = 1
        return intersectedArray


    #
    # def max_intersect(self, list_of_input_lists, verbose=True):
    #
    #     def getListsAsSortedWRTLength(listsOfLists):
    #         return sorted(listsOfLists, key=len)
    #
    #     def getEliminator(lst, popit=True):
    #
    #         if (len(lst) > 0):
    #             if(popit):
    #                 return lst.pop(0)
    #             else:
    #                 return lst[0]
    #         else:
    #             return None
    #
    #     lengthsorted = getListsAsSortedWRTLength(list_of_input_lists)
    #     intersectedArray = []
    #
    #     # init values
    #     x = getEliminator(lengthsorted[0])
    #     eliminatorListIndex = 0
    #     # start searching from the first list initially
    #     startat = 1
    #     eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])
    #
    #     while (x != None):
    #
    #         if(verbose):
    #             print "eliminator" , x , "startat list", startat,
    #
    #         for i in range(startat, len(lengthsorted)):
    #             # print startat, x, eliminatorArrayLength
    #
    #             # if any list is empty go back.
    #             if (len(lengthsorted[i]) == 0):
    #                 return intersectedArray
    #
    #             # golomb search gives equal value or bigger value. if it gives a value less than search item then that list ends.
    #             y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i]) / eliminatorArrayLength))
    #             if (verbose):
    #                 print "found y" , lengthsorted[i][y] , "in list" , lengthsorted[i]
    #
    #             valfound = lengthsorted[i][y]
    #
    #             # remove previous value of the array,
    #             # arrayin yeni halinde bizim eleman artik yok
    #             lengthsorted[i] = lengthsorted[i][y+1:]
    #
    #
    #             # print x
    #             # if the value found by golomb bigger than x , then keep smallest array as eliminator generator.
    #             if (valfound > x):
    #                 x = getEliminator(lengthsorted[0],popit=False)
    #                 # if new eliminator is also less than that value
    #                 if (valfound > x):
    #                     # if x still less , then popit to a dummy since no need to it
    #                     dummy = getEliminator(lengthsorted[0],popit=True)
    #                     # start search from 0th array
    #                     startat = 0
    #
    #                     # put valfound back into the array
    #                     lengthsorted[i] = [valfound] + lengthsorted[i]
    #
    #                     # set eliminator as valfound
    #                     x = valfound
    #
    #                     # update eliminator list index
    #                     eliminatorListIndex = i
    #                     # break
    #                 else:
    #                     # DONT update eliminator index
    #                     x = getEliminator(lengthsorted[0], popit=True)
    #                     startat = 1
    #
    #                 ## if not found in that list , then break it up
    #                 break
    #
    #             # if
    #             elif(valfound < x):
    #                 return intersectedArray
    #                 # x = getEliminator(lengthsorted[0])
    #                 # break
    #
    #             elif ((i == len(lengthsorted) - 1)):
    #                 if (verbose):
    #                     print "found : " , x , " eliminator index " ,eliminatorListIndex
    #                 intersectedArray.append(x)
    #                 # TODO there is a problem here, will we keep get eliminator from the list which previous eliminator is taken or will we get eliminator from first list ?
    #                 x = getEliminator(lengthsorted[eliminatorListIndex])
    #
    #                 # x = getEliminator(lengthsorted[eliminatorListIndex])
    #                 if(eliminatorListIndex ==0):
    #                     startat = 1
    #                 else:
    #                     startat = 0
    #
    #         # update eliminator array length
    #         eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])
    #
    #     return intersectedArray
    #

    # def max_intersect(self, list_of_input_lists, verbose=True):
    #
    #     def getListsAsSortedWRTLength(listsOfLists):
    #         return sorted(listsOfLists, key=len)
    #
    #     def getEliminator(lst, popit=True):
    #
    #         if (len(lst) > 0):
    #             if(popit):
    #                 return lst.pop(0)
    #             else:
    #                 return lst[0]
    #         else:
    #             return None
    #
    #     lengthsorted = getListsAsSortedWRTLength(list_of_input_lists)
    #     intersectedArray = []
    #
    #     # init values
    #     x = getEliminator(lengthsorted[0])
    #     eliminatorListIndex = 0
    #     # start searching from the first list initially
    #     startat = 1
    #     eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])
    #
    #     while (x != None):
    #
    #         if(verbose):
    #             print "eliminator" , x , "startat list", startat,
    #
    #         for i in range(startat, len(lengthsorted)):
    #             # print startat, x, eliminatorArrayLength
    #
    #             # if any list is empty go back.
    #             if (len(lengthsorted[i]) == 0):
    #                 return intersectedArray
    #
    #             # golomb search gives equal value or bigger value. if it gives a value less than search item then that list ends.
    #             # y = golomb_search(lengthsorted[i], x, int(len(lengthsorted[i]) / eliminatorArrayLength))
    #             y = golomb_search(lengthsorted[i], x, 1)
    #
    #             if (verbose):
    #                 print "found y" , lengthsorted[i][y] , "in list" , lengthsorted[i]
    #
    #             valfound = lengthsorted[i][y]
    #
    #             # remove previous value of the array,
    #             # arrayin yeni halinde bizim eleman artik yok
    #             lengthsorted[i] = lengthsorted[i][y:]
    #
    #
    #             if(i==0):
    #                 if (valfound > x):
    #                     x = getEliminator(lengthsorted[0], popit=True)
    #                     startat = 1
    #                 elif (valfound < x):
    #                     return intersectedArray
    #
    #
    #             elif(i==1):
    #                 if (valfound > x):
    #                     x = getEliminator(lengthsorted[0], popit=False)
    #                     if (valfound > x):
    #                         dummy = getEliminator(lengthsorted[0], popit=True)
    #                         startat = 0
    #                         x = valfound
    #                     else:
    #                         x = getEliminator(lengthsorted[0], popit=True)
    #                         startat = 0
    #
    #                     break
    #                 elif (valfound < x):
    #                     return intersectedArray
    #
    #             else:
    #                 if(valfound!=x):
    #                     # not found rest list
    #                     # get a new eliminator from 0 and start with 1
    #                     x = getEliminator(lengthsorted[0], popit=True)
    #                     startat = 1
    #                 else:
    #
    #                     if ((i == len(lengthsorted) - 1)):
    #                         if (verbose):
    #                             print "found : ", x, " eliminator index ", eliminatorListIndex
    #                         intersectedArray.append(x)
    #                         # TODO there is a problem here, will we keep get eliminator from the list which previous eliminator is taken or will we get eliminator from first list ?
    #
    #                         x = getEliminator(lengthsorted[eliminatorListIndex], popit=True)
    #                         startat = 1
    #
    #
    #
    #     # eliminatorArrayLength = len(lengthsorted[eliminatorListIndex])
    #
    #     return intersectedArray
