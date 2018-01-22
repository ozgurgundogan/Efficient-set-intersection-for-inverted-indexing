from Intersections import Intersections, SVSIntersection, ADBIntersection, SEQIntersection, MAXIntersection
from data_reader import read_wordlist, load_data
from query_parser import parse_queries
import time
from matplotlib import pyplot as plt
import numpy as np


def main(args=None):
    word_dict = read_wordlist()
    queries = parse_queries()

    queries.sort(key=len)

    printList = False

    querylengthCounter = 1

    queryDict = {}
    for query in queries:
        if (querylengthCounter < len(query)):
            #querylengthCounter = querylengthCounter + 1
            pass
        else:
            continue

        #lengthOfQuery.add(len(query))

        if(str(len(query)) in queryDict.keys()):
            pass
        else:
            queryDict[len(query)]={}
            queryDict[len(query)]['svs'] = []
            queryDict[len(query)]['adb'] = []
            queryDict[len(query)]['seq'] = []
            queryDict[len(query)]['max'] = []


        print query

        for tms in range(4):
            list_of_input = []

            for word in query:
                print word,
                # check whether word in our dict
                if word in word_dict.keys():
                    list_of_input.append(load_data(word_dict[word][0], word_dict[word][1]))

            if (len(list_of_input) <= 1):
                break


            #print list_of_input

            if (tms == 0):
                # print list_of_input
                start = time.time()
                svs_intersection = Intersections(SVSIntersection)
                interarr = svs_intersection.intersect(list_of_input)
            #    benchmark_result = interarr
                if (printList):
                    print interarr,
                end = time.time()
                print "svs_intersection " + str(end - start)
                # svs_time[len(query)] += (end - start)
                queryDict[len(query)]['svs'].append((end - start))

            if (tms == 1):
                start = time.time()
                adb_intersection = Intersections(ADBIntersection)
                interarr = adb_intersection.intersect(list_of_input)
                # assert interarr == benchmark_result
                if (printList):
                    print interarr,
                end = time.time()
                print "adb_intersection " + str(end - start)
                #adb_time[len(query)] += (end - start)
                queryDict[len(query)]['adb'].append((end - start))

            if (tms == 2):
                start = time.time()
                seq_intersection = Intersections(SEQIntersection)
                interarr = seq_intersection.intersect(list_of_input)
                if (printList):
                    print interarr,
                # assert interarr == benchmark_result
                end = time.time()
                print "seq_intersection " + str(end - start)
                #seq_time[len(query)] += (end - start)
                queryDict[len(query)]['seq'].append((end - start))

            if (tms == 3):
                start = time.time()
                max_intersect = Intersections(MAXIntersection)
                interarr = max_intersect.intersect(list_of_input)
                if (printList):
                    print interarr,
                # assert interarr == benchmark_result
                end = time.time()
                print "max_intersect " + str(end - start)
                #max_time[len(query)] += (end - start)
                queryDict[len(query)]['max'].append((end - start))


    avg_svs = []
    avg_abd = []
    avg_seq = []
    avg_max = []
    kys = []

    # sort dict wrt to key
    for key, value in sorted(queryDict.iteritems()):
        print key
        avg_svs.append(np.average(queryDict[key]['svs']))
        avg_abd.append(np.average(queryDict[key]['adb']))
        avg_seq.append(np.average(queryDict[key]['seq']))
        avg_max.append(np.average(queryDict[key]['max']))
        kys.append(key)
    #return

    #lengthOfQuery = range(len(avg_svs))
    plt.plot(kys, avg_svs, label="svs_time")
    plt.plot(kys, avg_abd, label="adb_time")
    plt.plot(kys, avg_seq, label="seq_time")
    plt.plot(kys, avg_max, label="max_time")
    plt.legend()
    plt.xlabel('Query Length')
    plt.ylabel('Time')
    # print max_time
    plt.savefig("/Users/iafs/Desktop/GitHub/Efficient-set-intersection-for-inverted-indexing/result.png")


if __name__ == "__main__":
    main()



