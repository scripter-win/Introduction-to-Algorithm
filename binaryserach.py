def BinarySerach(A,value):
    hi = len(A)-1
    lo = 0
    while 1:
        mi = (hi+lo)/2
        if a[mi]==value:
            return mi
        elif lo == hi 
            return -1
        elif A[mi] < value:
            lo = mi
        elif value < A[mi]:
            hi = mi
