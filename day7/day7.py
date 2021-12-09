# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:12:01 2021

@author: hongb
"""

def triangle(val):
    count = val
    total = 0
    while count != 0:
        total += count
        count -= 1

    return total
  

values = [i.strip().split(",") for i in open("input.txt", "r")]
values = values[0]
values = [int(i) for i in values]

values.sort()

median = values[len(values) // 2]

total = 0

for i in values:
    total += abs(median - i)
print(total)    
flag = False
ans = 0


position = 0

while position <= values[-1]:    
    total = 0
    for j in values:
        total += triangle(abs(position - j))

    if not flag:
        ans = total
        flag = True
    if total < ans:
        ans = total
    elif ans < total:
        print(ans)
        break
        
    position += 1
        
print(ans)    