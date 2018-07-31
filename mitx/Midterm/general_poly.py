def general_poly(L):
    """
    :param L: a list of numbers (n0, n1, n2, ... nk)
    :return: a function, which when applied to a value x, returns the value
        n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def conversion(x):
        """
        :param x: an integer
        :return: polynomial n0 * x^k + n1 * x^(k-1) + ... nk * x^0
        """
        #initialize variables
        poly = 0
        ct = 0

        #iterate through L and sum each polynomial
        for j in L:
            poly += j*x**kthList[ct]
            ct += 1

        return poly

    #initialize lists
    kthList = []

    #create list of exponents in decreasing order
    for i in range(len(L)):
        kthList.append(i)
    kthList.reverse()

    return conversion



   
L1 = [1, 2, 3, 4]
print(general_poly(L1)(10))

