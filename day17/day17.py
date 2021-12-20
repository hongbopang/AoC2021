# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:23:35 2021

@author: hongb
"""
def calc_max_height(v_y):
    return v_y * (v_y + 1) / 2
 
def get_steps_bounds(x_itr, xmin, xmax):
    lower_bound = 0
    upper_bound = 0
    l_flag = True
    
    x = 0
    xv = x_itr
    
    counter = 0

    while 1:
        x += xv
        counter += 1
        

        
        if x >= xmin and l_flag:
            l_flag = False
            lower_bound = counter
        if x > xmax or xv == 0:
            upper_bound = counter -1
            return (lower_bound,upper_bound)
        
        
        if xv != 0:
            if xv > 0:
                xv -=1
            else:
                xv += 1
def process(x_itr,y,steps_bounds):
    lower, upper = steps_bounds
    y_pos = 0
    y_v = y
    
    counter = 0

    while counter < lower:
        y_pos += y_v
        y_v -= 1
        counter += 1
        
    while counter <= upper:
        y_pos += y_v
        y_v -= 1
        counter += 1
        if y_pos >= ymin and y_pos <= ymax:
            
            return True, True        
    print(y,y_pos,y_v)
    if y_pos > ymax and y_v >0:
        return False, False
        
        
    return False, True

    
def get_best_y_for_x(x_itr, steps_bounds):
    y = 0
    ans = 0
    
    cont_flag = True
    while cont_flag:

        tmp, cont_flag = process(x_itr, y, steps_bounds)
        if tmp:
            print(x_itr,y)
            ans = max(ans,calc_max_height(y))
        y += 1
        
    return ans
    
    

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
    
lower_x = x_try
upper_x = xmax + 1
ans = 0

for x in range(lower_x,upper_x):
    bounds = get_steps_bounds(x, xmin, xmax)
    val = get_best_y_for_x(x, bounds)
    ans = max(val, ans)
print(ans)

