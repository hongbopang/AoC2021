# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:57:42 2021

@author: hongb
"""
def count_stride(stride, values):
    prev = sum(values[:stride])
    count = 0
    
    f_p = stride    
    
    while f_p < len(values) + 1:
        tmp = sum(values[f_p-stride:f_p])
        if tmp > prev:
            count += 1
        prev = tmp
        f_p += 1
    return count
    
def direct_compare(stride, values):
    f_p = stride
    b_p = 0
    count = 0
    
    while f_p < len(values):
        if values[f_p] > values[b_p]:
            count += 1
        f_p += 1
        b_p += 1
    return count
    

values = [int(i) for i in open("input.txt", "r")]
        
print(direct_compare(1,values))
print(direct_compare(3,values))
#1692
#1724