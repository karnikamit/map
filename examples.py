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

# applying fn separately to each element in lists
a1, b1, c1, d1 = range(10), range(20, 30), range(30, 40), range(40, 50)
temp = map(lambda *args: [i**2 for i in args], a1, b1, c1, d1)
list_name = {}
for i in range(len(temp[0])):
    list_name["list_"+str(i)] = []

for i in temp:
    m = 0
    for j in i:
        list_name["list_" +str(m)].append(j)
        m += 1

for m in list_name:
    print list_name[m]
