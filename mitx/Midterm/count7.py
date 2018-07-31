def count7(N):
    """
    :param N: any non-negative integer
    :return: the number of occurrences of the digit 7 in the integer N
    """

    #initializes the count variable and creates a string of the integer N
    ct = 0
    nString = str(N)

    #iterates through string of an integer counting occurrences of '7'
    for i in nString:
        if i == '7':
            ct += 1
        else:
            continue

    return ct

print(count7(717))
print(count7(1237123))
print(count7(8989))
print(count7(13247132777231300))

print('mod:', 7%11)