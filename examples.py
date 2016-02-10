# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def fahrenheit(t):
    return (float(9)/5)*t + 32
temp = range(30, 35)

print map(fahrenheit, temp)

#   USING lambda
print map(lambda t: (float(9)/5)*t + 32, temp)

# can be applied to more than one list. The lists have to have the same length
#                                                                  -----------
a = b = range(10)
print map(lambda x, y: x+y, a, b)

