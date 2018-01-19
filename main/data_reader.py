from struct import unpack


def read_wordlist():
    word_dict = {}
    start = 0
    with open("/home/ozgurgundogan/Desktop/Efficient-set-intersection-for-inverted-indexing/data/wordlist.txt", 'r') as word_list:
        for line in word_list:
            line = line.split(" ")[:2]
            word = line[0]
            freq = int(line[1])
            word_dict[word] = (start, start + freq*8)

            start += freq*8

    return word_dict


def load_data(start, end):
    ret = []
    postings = open("/home/ozgurgundogan/Desktop/Efficient-set-intersection-for-inverted-indexing/data/entry.bin", 'rb')
    pointer = start
    while pointer <= end:
        postings.seek(pointer, 0)
        lll = unpack('<i', postings.read(4))
        ret.append(lll[0])
        pointer += 8

    return ret
