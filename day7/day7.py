# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:12:01 2021

@author: hongb
"""

def triangle(val):
    return val * (val + 1) // 2

def get_fuel_at_position(pos, values):
    counter = 0
    for i in values:
        dist = abs(i-pos)
        counter += triangle(dist)
    return counter
    
def get_fuel_trio(pos, values):
    a = get_fuel_at_position(pos-1, values)
    b = get_fuel_at_position(pos, values)
    c = get_fuel_at_position(pos+1, values)    
    return a,b,c


def binary_search(start, end, values):
    median = (end - start) // 2 + start    
    one,two,three = get_fuel_trio(median,values)

    if one > two and three > two:
        return two
    if one < two:
        return binary_search(start,median, values)
    if three < two:
        if median == start:
            return three
        return binary_search(median,end, values)
    

values = [i.strip().split(",") for i in open("input.txt", "r")]
values = values[0]
values = [int(i) for i in values]
values.sort()
median = len(values) // 2 

print(sum(values[median:])-sum(values[:median]))

print(binary_search(values[0], values[-1], values))     
  