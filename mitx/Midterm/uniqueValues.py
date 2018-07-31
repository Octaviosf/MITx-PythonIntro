def uniqueValues(aDict):
    """
    :param aDict: a dictionary
    :return: a sorted list of keys which map to the unique integer values of aDict, if
        aDict has no unique values then an empty list is returned
    """

    #find unique values
    values = list(aDict.values())
    valClone = values[:]
    keys = list(aDict.keys())
    keysUnique = []
    indexListVals = []
    ct = 1
    for i in values:
        if i in values[:ct] and i in values[ct:]:
            if valClone == []:
                return []
            while i in valClone:
                valClone.remove(i)
        ct += 1

    #extract keys of unique values
    for i in valClone:
        indexListVals.append(values.index(i))
    for k in indexListVals:
        keysUnique.append(keys[k])

    #sort unique keys
    keysUnique.sort()

    return keysUnique

dict1 = {'a':2,'o':2, 'c': 1, 'f': 9, 'd': 0, 'b': 3, 'w': 5}
print(uniqueValues(dict1))

dict2 = {'a':2,'o':2, 'c': 2, 'f': 2, 'd': 2, 'b': 2, 'w': 2}
print(uniqueValues(dict2))

