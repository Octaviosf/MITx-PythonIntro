def sumDigits(s):
    """
    :param s: string
    :return: sum of decimal digits in s
    """

    # var init
    digitsum = 0

    # checks whether each char is digit and performs sum
    try:
        for i in s:
            if i.isdigit():
                digitsum += int(i)
    # prints error message if incorrect type
    except TypeError:
        print('Incorrect input type. Please input a string.')

    return digitsum

testStrs = ['abc510','510abc','00abc', 5,0,'00017','loligag']
for i in testStrs:
    print(sumDigits(i))
