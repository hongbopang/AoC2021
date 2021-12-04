# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:52:21 2021

@author: hongb
"""

values = [i.strip().split() for i in open("input.txt", "r")]

d1 = 0
d2 = 0
x = 0

for arg, arg2 in values:
    b = int(arg2)
    if arg == 'down':
        d1 += b
    elif arg == 'up':
        d1 -= b
    else:
        x += b
        d2 += b * d1
print(d1 * x)
#1690020
       
print(d2 * x)
#1408487760