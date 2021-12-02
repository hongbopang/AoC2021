# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:52:21 2021

@author: hongb
"""

values = [i.strip().split() for i in open("input.txt", "r")]

d1 = 0
x1 = 0
d2 = 0
x2 = 0
aim = 0

for arg, arg2 in values:
    b = int(arg2)
    if arg == 'down':
        d1 += b
        aim += b
    elif arg == 'up':
        d1 -= b
        aim -= b
    else:
        x1 += b
        x2 += b
        d2 += b * aim
print(d1 * x1)
#1690020

print(d2 * x2)
#1408487760