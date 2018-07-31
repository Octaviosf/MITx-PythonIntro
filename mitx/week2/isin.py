def isin(s1,s2):
    """
    :param s1: string one
    :param s2: string two
    :return: True if either string occurs within the other and False otherwise.
    """
    if s1 in s2 or s2 in s1:
        return True
    else:
        return False

result = isin('sal','universal')
print(result)

result = isin('tornado','torn')
print(result)

result = isin('North','Face')
print(result)
