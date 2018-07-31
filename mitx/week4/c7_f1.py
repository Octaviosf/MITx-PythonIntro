def sumDigits(s):
    """
    :param s: string
    :return: sum of decimal digits in s
    """
    numsum = 0

    # loops through string to sum it's decimal digits
    for i in s:
        try:
            numsum += int(i)
        except ValueError:
            print(i, 'is not a decimal digit.')
            continue

    return print('The sum of the decimal digits in', s, 'is', str(numsum) + '.')


s1 = 'ab3n8n9'

s2 = '0001'

s3 = 'abcde'

s4 = '590'

slist = [s1, s2, s3, s4]

for i in slist:
    print('\n'+i+':')
    sumDigits(i)

