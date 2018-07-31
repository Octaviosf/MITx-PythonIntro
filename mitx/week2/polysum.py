def polysum(n,s):
    """
    :param n: number of sides in polygon
    :param s: length of each side
    :return: sum of polygon area and square of perimeter; rounded to 4 decimals
    """
    #calculates area and perimeter of polygon, 'math' module must be imported
    area = 0.25*n*s**2/tan(pi/n)
    perimeter = n*s

    #returns sum of area and square of perimeter to 4 decimals
    return round(area + perimeter**2,4)

from math import *
