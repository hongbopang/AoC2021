# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:46:56 2021

@author: hongb
"""

def enhance(holder, r_min, r_max, c_min, c_max, polarity,enhancer):
    r_min_new, r_max_new = r_min-1, r_max +1
    c_min_new, c_max_new = c_min-1, c_max +1
    
    new_holder = dict()
    
    for r in range(r_min_new,r_max_new+1):
        for c in range(c_min_new,c_max_new+1):            
            val = 0
            for r_prev in range(r-1,r+2):
                for c_prev in range(c-1, c+2):
                    val *= 2
                    if (r_prev,c_prev) in holder :
                        if holder[(r_prev,c_prev)] == "#":     
                            val += 1
                    elif polarity != 1:
                        val += 1
          
            new_holder[(r,c)] =  enhancer[val]
    return new_holder, r_min_new, r_max_new, c_min_new, c_max_new, -polarity
                            
     
    

lines = [i.strip() for i in open("input.txt", "r")]

enhancer = lines[0]

inputs = lines[2:]

holder_dict = dict()

row = 0

row_min = 0
col_min = 0


for line in inputs:
    col = 0
    
    for char in line:
        holder_dict[(row,col)] = char
        col_max = col
        col += 1
    row_max = row
    row += 1       
polarity = 1

for _ in range(50):
    ans = 0
    holder_dict, row_min, row_max, col_min, col_max, polarity = enhance(holder_dict, row_min, row_max, col_min, col_max, polarity,enhancer)
    if _ == 1:
        for key in holder_dict:
            if holder_dict[key] == '#':
                ans += 1
        print(ans)
    
        
for key in holder_dict:
    if holder_dict[key] == '#':
        ans += 1
print(ans)
               
ans = 0

