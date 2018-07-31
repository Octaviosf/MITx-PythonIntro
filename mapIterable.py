def mapIterable(L,f):
    L1 = []
    for i in map(f, L):
        L1.append(i)

    return L1

L = [1,-1,5,1.5,-4]

mappedList = mapIterable(L,abs)
print(mappedList)
