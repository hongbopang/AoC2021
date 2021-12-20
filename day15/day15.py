# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:09:25 2021

@author: hongb
"""
import time

lines = [i.strip() for i in open("input.txt", "r")]

cave = []

for l in lines:
    tmp = []
    for char in l:
        tmp.append(int(char))
        
    cave.append(tmp)
    
   

r_t,c_t = len(cave), len(cave[0])

lengths = dict()

lengths[0] = [(0,0)]

done = dict()

step = 0
go = True

start= time.time()
while go:

    if step not in lengths:
        step += 1
        continue
    currs = lengths[step]
    
    for loc in currs:
        
        if loc in done:
            continue
        done[loc] = 1
        
        r_prime, c_prime = loc
        if r_prime == r_t-1 and c_prime == c_t-1:
            print(step)
            go = False
            break
        candidates = []
        if r_prime != 0:
            candidates.append((r_prime-1, c_prime))           
            
        if r_prime != r_t-1:
            candidates.append((r_prime+1, c_prime))    
    
        if c_prime != 0:
            candidates.append((r_prime, c_prime-1))    

        if c_prime != c_t - 1:
            candidates.append((r_prime, c_prime+1))
            
        for r_new, c_new in candidates:
            dist = step + cave[r_new][c_new]
            if dist not in lengths:
                lengths[dist] = []
            lengths[dist].append((r_new,c_new))
    step += 1
    
print(time.time()-start)
lengths_2 = dict()    
lengths_2[0] = [(0,0)] 

done = dict()

step = 0
go = True
start = time.time()
while go:
    if step not in lengths_2:
        step += 1
        continue
    currs = lengths_2[step]

    for loc in currs:
        
        if loc in done:
            continue
        done[loc] = 1
        
        r_prime, c_prime = loc
        if r_prime == r_t*5-1 and c_prime == c_t*5-1:
            print(step)
            go = False
            break
        candidates = []
        if r_prime != 0:
            candidates.append((r_prime-1, c_prime))           
            
        if r_prime != r_t*5-1:
            candidates.append((r_prime+1, c_prime))    
    
        if c_prime != 0:
            candidates.append((r_prime, c_prime-1))    

        if c_prime != c_t*5 - 1:
            candidates.append((r_prime, c_prime+1))
            
        for r_new, c_new in candidates:
            r_disp = r_new // r_t
            c_disp = c_new // c_t
            
            r_mod = r_new % r_t
            c_mod = c_new % r_t
            
            
            value = cave[r_mod][c_mod] + r_disp + c_disp
            if value > 9:
                value -= 9
            
            dist = step + value          
                                    
            
            if dist not in lengths_2:
                lengths_2[dist] = []
            lengths_2[dist].append((r_new,c_new))
    step += 1    
   

print(time.time()-start)        
    
    
            