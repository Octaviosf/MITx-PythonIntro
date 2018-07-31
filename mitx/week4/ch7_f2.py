def findAnEven(L):
    """
    :param L: list of integers
    :return: first even number in L
    """

    # returns first even number in L
    for i in L:
        if i%2 == 0:
            return i
        else:
            continue

    # raises ValueError
    raise ValueError('findAnEven called with no even numbers in list.')

testLists = [[1,4,5,6], [1, 5, 7, 9], [2, 0, 4, 6], [], [0]]

for i in testLists:
    print(str(i)+':')
    try:
        print(findAnEven(i),'\n')
    except ValueError as msg:
        print(msg,'\n')
