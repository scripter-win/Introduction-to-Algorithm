def QuicckSort(A, lo, hi):
    register = A[lo]
    j = hi
    i = lo
    while 1 :
        while j > i:
            if a[j] < register:
                a[hi], a[lo] = a[lo], a[hi]
            j-=1
        while i < j:
            if a[i] > register:
                 a[lo], a[hi] = a[hi], a[lo]
            i+=1
        if i==j:
            break
    QuicckSort(A, lo, i-1)
    QuicckSort(A, j+1, hi)
