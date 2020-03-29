def allLongestStrings(inputArray):
    n =[]
    for i in inputArray:
        n.append(len(i))
    x =max(n)
    m =[]
    for index,i in enumerate(inputArray):
        if len(i)==x:
            m.append(inputArray[index])
    return m

