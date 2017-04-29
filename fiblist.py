fibs(lengths): 
    'return the list of Fibonacci sequence'
    fiblist = [0, 1]
    for i in range(lengths-2):
        fiblist.append(fiblist[-2]+fiblist[-1])
    return fiblist
print fibs(11)
