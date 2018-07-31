def findAnEven(L):
    """
    :param L: list of integers
    :return: first even number of L
    Raises ValueError if L does not contain an even number
    """

    # attempts to find first even number
    try:
        for i in L:
            if i % 2 == 0:
                num = i
                break
        return num

    # if incorrect type TypeError is raised
    except TypeError:
        raise TypeError('Incorrect type in list.')

    # if no even number found then ValueError is raised
    except:
        raise ValueError('L does not contain an even number.')


nums = [1, 5, 7, 9, 14, 12, 15, 2]
nums1 = []
nums2 = [1, 5, 7, 9]
nums3 = ['2', 1, 4, 5]
# attempts to call findAnEven()
try:
    print(findAnEven(nums))
    print(findAnEven(nums1))
    print(findAnEven(nums2))
    print(findAnEven(nums3))
# prints error message bound to ValueError if exception is raised
except (ValueError, TypeError) as msg:
    print(msg)
