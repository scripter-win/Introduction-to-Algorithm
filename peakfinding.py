<<<<<<< HEAD
#test case
c=[]
for i in range(33600):
    c.append([i])
count = 0


# one dimension edition of binary serach
def PeakFinding(a,lo,hi):
    global count
    count+=1
    #print count
    if lo==hi:
        return a[lo]
    if a[(hi+lo)/2] < a[(hi+lo)/2-1]:
        hi = (hi+lo)/2-1
        return PeakFinding(a,lo,hi)
    elif a[(hi+lo)/2] < a[(hi+lo)/2+1]:
        lo = (hi+lo)/2+1
        return PeakFinding(a,lo,hi)
    else:
        return (hi+lo)/2
print PeakFinding(c,0,len(c)-1)
print count

#two dimension edition of greedy strategy
def PeakFinding_TwoDimension_greed(a,row,column):
    i = 0
    j = 0
    row-=1
    column-=1
    for count in range((row+1)*(column+1)):
        max = a[i][j]
        state = 0
        if(i < row):
            if(a[i+1][j] > max):
                max = a[i+1][j]
                state = 1
        if(j < column):
            if(a[i][j+1] > max):
                max = a[i][j+1]
                state = 2
        if(a[i-1][j] > max):
            max = a[i-1][j]
            state = -1
        if(a[i][j-1] > max):
            max = a[i][j-1]
            state = -2
        if state == 0:
            return [i,j] 
        i += state % 2
        j += state / 2
        
    return 0

#two dimension edition of binary serach
def PeakFinding_TwoDimension_binary(a,row,column):
    column-=1
    lo = 0
    hi = column
    mi = (lo + hi)/2  
    while 1:
        mi = (lo + hi)/2
        if lo==hi:
            return [mi,a[mi].index(max(a[mi]))]
        if  max(a[mi-1]) > max(a[mi]):
            hi = mi - 1
        elif max(a[mi+1]) > max(a[mi]):
            lo = mi + 1
        else:
            return [mi,a[mi].index(max(a[mi]))]
    return mi

#test case
k=[23,24,13],[3,3,5],[11,1,6]
print PeakFinding_TwoDimension_binary(k,3,3)
=======
#test case

count = 0

# one dimension edition
def PeakFinding(a,lo,hi):
    global count
    count+=1
    #print count
    if lo==hi:
        return a[lo]
    if a[(hi+lo)/2] < a[(hi+lo)/2-1]:
        hi = (hi+lo)/2-1
        return PeakFinding(a,lo,hi)
    elif a[(hi+lo)/2] < a[(hi+lo)/2+1]:
        lo = (hi+lo)/2+1
        return PeakFinding(a,lo,hi)
    else:
        return (hi+lo)/2

#two dimension edition of greed strategy
def PeakFinding_TwoDimension_greed(a,row,column):
    i = 0
    j = 0
    row-=1
    column-=1
    for count in range((row+1)*(column+1)):
        max = a[i][j]
        state = 0
        if(i < row):
            if(a[i+1][j] > max):
                max = a[i+1][j]
                state = 1
        if(j < column):
            if(a[i][j+1] > max):
                max = a[i][j+1]
                state = 2
        if(a[i-1][j] > max):
            max = a[i-1][j]
            state = -1
        if(a[i][j-1] > max):
            max = a[i][j-1]
            state = -2
        if state == 0:
            return [i,j] 
        i += state % 2
        j += state / 2        
    return 0

#two dimension edition of greed strategy
def PeakFinding_TwoDimension_binary(a,row,column):
    column-=1
    lo = 0
    hi = column
    mi = (lo + hi)/2  
    while 1:
        mi = (lo + hi)/2
        if lo==hi:
            return [mi,a[mi].index(max(a[mi]))]
        if  max(a[mi-1]) > max(a[mi]):
            hi = mi - 1
        elif max(a[mi+1]) > max(a[mi]):
            lo = mi + 1
        else:
            return [mi,a[mi].index(max(a[mi]))]
    return mi
>>>>>>> origin/master
