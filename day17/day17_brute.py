# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:06:00 2021

@author: hongb
"""
import time
def check(x,y):
    x_pos = 0
    y_pos = 0
    
    x_v = x
    y_v = y
    flag = False
    y_max = 0
    
    
    while x_pos <= xmax:

        x_pos += x_v
        y_pos += y_v
        
        if x_v == 0 and x_pos < xmin:
            break
        if y_pos < ymin:
            break
        y_v -=1
        
        if x_v != 0:
            if x_v > 0:
                x_v -=1
            else:
                x_v +=1
        
        if x_pos >= xmin and x_pos <= xmax and y_pos >= ymin and y_pos <= ymax:

            flag = True
    
        y_max = max(y_pos,y_max)
        
    if flag:
        return True, y_max
    else:
        return False, -1
    

lines = [i.strip() for i in open("input.txt", "r")]

input_data = lines[0]

x,y = input_data.split(", ")

x = x[13:]

xmin,xmax = x.split("..")
xmin = xmin[2:]

ymin,ymax = y.split("..")
ymin = ymin[2:]

xmin = int(xmin)
xmax = int(xmax)
ymin = int(ymin)
ymax = int(ymax)

x_try = 0
value = 0.5

while value <= xmin:
    x_try += 1
    value = x_try * (x_try - 1) // 2
    
lower_x = x_try-1
upper_x = xmax
ans = 0
counter = 0
start = time.time()
for x in range(lower_x, upper_x+1):
    for y in range(-300,500):

        can, tmp = check(x,y)
        if can:
            counter += 1
        ans = max(tmp,ans)
        
print(ans,counter)
print(time.time()-start)