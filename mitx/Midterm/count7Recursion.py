def count7(N):
    """
    :param N: any non-negative integer
    :return: the number of occurrences of the digit 7 in the integer N
    """

    # base case
    if N == 0:
        return 0
    # test right most digit and shift left after test
    if N % 10 == 7:
        return 1 + count7(N//10)
    elif N % 10 != 7:
        return 0 + count7(N//10)
