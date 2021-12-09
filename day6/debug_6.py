# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:07:52 2021

@author: hongb
"""


with open('input.txt') as f:
    first_line = f.readline()

ins = []
splits = first_line.split(',')
for split in splits:
    ins.append(split.strip())
print(ins)
for i in range(18):
    print(ins)
    for count, value in enumerate(ins):
        newv = int(value)
        if newv == 0:
            ins[count] = 6
            ins.append(8)
        else:
            ins[count] = str(int(value) - 1)
            
print(len(ins))