def parent(i):
    return i/2
    
def left(i):
    return 2*i

def right(i):
    return 2*i

def MaxHeapify(A,i):
    l = left(i)
    r = right(i)
    largest = i 
    if l <= A.heapsize and A[l] > A[i]:
        largest = l
    if r <= A.heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]        
        print A
        MaxHeapify(A,largest)

def BuildMaxHeap(A):
    for i in range(A.heapsize/2, 0):
        MaxHeapify(A,i)

def heapsort(A):
    for i in range(A.length, 1):
        A[A.heapsize], A[i] = A[i], A[A.heapsize]
        A.heapsize -= 1
        MaxHeapify(A,1)







