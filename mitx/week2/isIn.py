def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    # order aStr alphabetically
    midindex = int(len(aStr)/2)
    aStr = sorted(aStr)
    # test middle most character from aStr and compare to char
    if char < aStr[midindex] and midindex != 0:
        return isIn(char, aStr[0:midindex])
    if char > aStr[midindex] and midindex != 0:
        return isIn(char, aStr[midindex:])
    if char == aStr[midindex]:
        return True
    if midindex == 0:
        return False
    # if char is less than middle most char then search left half of aStr, else search right half and repeat

print(isIn('s','fibonnaci'))