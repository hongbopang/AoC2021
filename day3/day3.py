# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:04:50 2021

@author: hongb
"""
def bin_list_to_dec(binary):
    value = 0
    
    for char in binary:
        value *= 2
        if char == 1:
            value += 1
    return value

values = [i.strip() for i in open("input.txt", "r")]
length = len(values[0])
total = 2 ** length  - 1

counters = [0 for _ in range(length)]

for word in values:
    for i in range(length):
        if word[i] == "1":
            counters[i] += 1
        else:
            counters[i] -= 1
        

ans = [0 for _ in range(length)]

for i in range(length):
    if counters[i] > 0:
        ans[i] = 1
        
gamma = bin_list_to_dec(ans)
#print((total - gamma) * gamma)
#4191876

bitmask = [1 for _ in range(len(values))]

for i in range(length):
    zeros = 0
    ones = 0
    for j in range(len(values)):
        if bitmask[j] == 1:
            bit = values[j][i]
            if bit == "1":
                ones += 1
            else:
                zeros += 1    
    if zeros > ones:
        val = "0"
    else:
        val = "1"
    for j in range(len(values)):
        if bitmask[j] == 1:
            if values[j][i] != val:
                bitmask[j] = 0
    if sum(bitmask) == 1:
       a = [int(i) for i in values[bitmask.index(1)]]
bitmask = [1 for _ in range(len(values))]
for i in range(length):
    zeros = 0
    ones = 0
    for j in range(len(values)):
        if bitmask[j] == 1:
            bit = values[j][i]
            if bit == "1":
                ones += 1
            else:
                zeros += 1    
    if zeros <= ones:
        val = "0"
    else:
        val = "1"
    for j in range(len(values)):
        if bitmask[j] == 1:
            if values[j][i] != val:
                bitmask[j] = 0
    if sum(bitmask) == 1:
        b = [int(i) for i in values[bitmask.index(1)]]
        
oxy = bin_list_to_dec(a) 
co2 = bin_list_to_dec(b)
print(a)
#print(oxy*co2)
#3414905