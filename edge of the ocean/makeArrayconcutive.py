def makeArrayConsecutive2(statues):
    a=sorted(statues)
    n=[]
    for i in range(a[0],a[-1]+1):
        n.append(i)
    return len(list(set(n)-set(a)))
