def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '"""
    # Your code here
    print('Before comp:', 'a = ' + str(a), 'b = ' + str(b))
    if b != 0:
        print('within if b != 0:')
        return gcdRecur(b, a % b)
    elif b == 0:
        print('within if b == 0:', 'a =',a)
        return a



print(gcdRecur(192, 160))
