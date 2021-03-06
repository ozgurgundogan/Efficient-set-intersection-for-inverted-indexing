import re
import random

def parse_queries(concat=False):
    queries = []
    with open("/Users/iafs/Desktop/GitHub/Efficient-set-intersection-for-inverted-indexing/data/q-topics-org-SET1.txt") as q_file:
        for line in q_file:
            m_obj = re.match(r"^<title>(.*)\n$", line)
            if m_obj is not None:
                queries.append(map(lambda x: x.lower(), m_obj.group(1).strip().replace(',','').split(" ")))
    with open("/Users/iafs/Desktop/GitHub/Efficient-set-intersection-for-inverted-indexing/data/q-topics-org-SET2.txt") as q_file:
        for line in q_file:
            m_obj = re.match(r"^<title>(.*)\n$", line)
            if m_obj is not None:
                queries.append(map(lambda x: x.lower(), m_obj.group(1).strip().replace(',','').split(" ")))
    with open("/Users/iafs/Desktop/GitHub/Efficient-set-intersection-for-inverted-indexing/data/q-topics-org-SET3.txt") as q_file:
        for line in q_file:
            m_obj = re.match(r"^<title>(.*)\n$", line)
            if m_obj is not None:
                queries.append(map(lambda x: x.lower(), m_obj.group(1).strip().replace(',','').split(" ")))


    ## randomly concat queries
    if(concat):
        for k in range(50):
            x = random.sample(range(len(queries)),1)[0]
            y = random.sample(range(len(queries)),1)[0]

            for el in queries[x]:
                queries[y].append(el)


    return queries

