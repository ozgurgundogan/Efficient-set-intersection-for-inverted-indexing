
def linearSearch(lst,target):
    while(len(lst)>0):
        if(lst[0]>target):
            return False,lst
        elif(lst[0] == target):
            lst.pop(0)
            return True, lst
        else:
            lst.pop(0)

    return False,[]


def binary_search(array, lengthOfArray, target, verbose = False):
    if (verbose):
        print " in binary search array : ", array , " length of array ", lengthOfArray, " target " , target
    if(lengthOfArray ==1):
        if(array[0] == target):
            return 0
        else:
            return lengthOfArray

    lower = 0
    upper = lengthOfArray
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                return x+1
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x


def golomb_search(L,x,b,currentPosition=0,verbose=False):
    if (verbose):
        print "golomb search ==> arr : " , L ," target : " , x
    curr = currentPosition
    pos = curr + b
    n = len(L)-1

    # if x is less then first element than return directly.
    if(x<L[curr]):
        return 0

    while(pos < n and L[pos]<x):
        curr = pos
        pos = curr + b

    if(pos > n):
        pos = n

    if (verbose):
        print " element " , x , " between " , L[curr:pos+1]

    offset = binary_search(L[curr:pos+1],pos-curr + 1 ,x)
    if (verbose):
        print " calculated offset" , offset

    if(curr+offset > n):
        return n
    else:
        return curr+offset
