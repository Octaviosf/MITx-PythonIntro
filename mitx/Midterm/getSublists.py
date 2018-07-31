def getSublists(L, n):
    """
    :param L: a list of integers where n <= len(L)
    :param n: an integer where 0 < n <= len(L)
    :return: a list of integers with sublists of length n, iterated right-wise where each
        integer of L is the first element of each sublist
    """

    # base case
    if n == len(L):
        return [L]
    # recursive appending
    else:
        return [L[:n]] + getSublists(L[1:], n)

