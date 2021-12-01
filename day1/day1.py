# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:57:42 2021

@author: hongb
"""


f = open("input.txt", "r")
count = 0

Flag = False
values = []
for line in f:
    values.append(int(line))
    a = int(line)
    if not Flag:
        Flag = True
        prev = a
    else:
        if a > prev:
            count += 1
        prev = a
        

print(count)
back_ptr = 0
front_ptr = 3
count2 = 0
prev = sum(values[:2])

while front_ptr < len(values):
    temp = prev - values[back_ptr] + values[front_ptr]
    if temp > prev:
        count2 += 1
    prev = temp
    front_ptr += 1
    back_ptr += 1
print(count2)