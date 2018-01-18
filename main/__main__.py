from Intersections import Intersections, SVSIntersection, ADBIntersection, SEQIntersection, MAXIntersection
from data_reader import read_wordlist, load_data
from query_parser import parse_queries
import time
from matplotlib import pyplot as plt




def main(args=None):
    word_dict = read_wordlist()
    queries = parse_queries()

    lengthOfQuery = []
    svs_time = []
    adb_time = []
    seq_time = []
    max_time = []

    queries.sort(key=len)

    querylengthCounter = 0
    for query in queries:
        if(querylengthCounter < len(query)):
            querylengthCounter = querylengthCounter + 1
        else:
            continue
        list_of_input = []
        lengthOfQuery.append(len(query))
        for word in query:
            # check whether word in our dict
            if word in word_dict.keys():
                list_of_input.append(load_data(word_dict[word][0], word_dict[word][1]))

        start = time.time()
        svs_intersection = Intersections(SVSIntersection)
        svs_intersection.intersect(list_of_input)
        end = time.time()

        print "svs_intersection " + str(end - start)
        svs_time.append(end - start)

        start = time.time()
        adb_intersection = Intersections(ADBIntersection)
        adb_intersection.intersect(list_of_input)
        end = time.time()

        print "ADB_intersection " + str(end - start)
        adb_time.append(end - start)

        start = time.time()
        seq_intersection = Intersections(SEQIntersection)
        seq_intersection.intersect(list_of_input)
        end = time.time()

        print "seq_intersection " + str(end - start)
        seq_time.append(end - start)

        start = time.time()
        max_intersect = Intersections(MAXIntersection)
        max_intersect.intersect(list_of_input)
        end = time.time()

        print "max_intersect " + str(end - start)
        max_time.append(end - start)


    plt.plot(lengthOfQuery,svs_time, label="svs_time")
    plt.plot(lengthOfQuery, adb_time, label="adb_time")
    plt.plot(lengthOfQuery, seq_time, label="seq_time")
    plt.plot(lengthOfQuery, max_time, label="max_time")
    plt.legend()
    # print max_time
    plt.savefig("result.png")

if __name__ == "__main__":
    main()