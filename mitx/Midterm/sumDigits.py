def sumDigits(N):
    """
    :param N: non-negative integer
    :return: sum of the digits of N
    """
    # base case
    if N//10 == 0:
        return N
    # sum right-most digit to recursion of left-shifted N
    if N % 10 > 0:
        return N % 10 + sumDigits(N//10)
    if N % 10 == 0:
        return sumDigits(N//10)

print(sumDigits(0))
print(sumDigits(111))
print(sumDigits(1004))
