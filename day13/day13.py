# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:27:30 2021

@author: hongb
"""
import pandas as pd

lines = [i.strip() for i in open("input.txt", "r")]


dotted = dict()

fold_ins = []

dots = True

rmin = 0
rmax = 0

cmin = 0
cmax = 0

for point in lines:
    if not point:
        dots = False
        continue
    if dots:
        point = point.split(",")
        dotted[(int(point[1]),int(point[0]))]  = 1
      
        if int(point[1]) > rmax:
            rmax = int(point[1])
        if int(point[0]) > cmax:
            cmax = int(point[0])
        
    else:
        tmp = point.split("=")
        
        
        fold_ins.append((tmp[0][-1],int(tmp[1])))

rmax+=1
cmax+=1

    
tmp_dict = dict()
first = True
for dimension, location in fold_ins:
    if dimension == 'x':        
        for r,c in dotted:
            if c > location:
                c_transformed = 2 * location - c
                tmp_dict[(r,c_transformed)] = 1
            else:
                tmp_dict[(r,c)] = 1                
    elif dimension == 'y':
        for r,c in dotted:
            if r > location:
                r_transformed = 2*location - r

                tmp_dict[r_transformed,c] = 1
            else:
                tmp_dict[(r,c)] = 1
    dotted = dict()           
    for entry in tmp_dict:
        dotted[entry] = tmp_dict[entry]
    if first:
        print(len(dotted))
        first = False
    
rmax = 0
cmax = 0


for r,c in dotted:
    if r > rmax:
        rmax = r
    if c > cmax:
        cmax = c
rmax +=1
cmax+=1       
picture = [[0 for _ in range(cmax)]for __ in range(rmax)]

for r,c in dotted:
    picture[r][c] = 'X'
 
picture = pd.DataFrame(picture)
try:
    picture.to_csv("ans.csv")
except:
    print("already there!")