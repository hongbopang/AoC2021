# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:10:54 2021

@author: hongb
"""
class octopus:
    def __init__(self,value,location, octopi):
        self.value = value
        self.location = location
        r,c = location
        self.neighbours = []
        self.flashed = False
        self.octopi = octopi
        rs = [r-1, r, r+1]
        cs = [c-1, c, c+1]
        
        for tr in rs:
            if tr == -1 or tr == 10:
                continue
            for tc in cs:
                if tc == -1 or tc == 10:
                    continue
                
                if tc != c or tr != r:
                    self.neighbours.append((tr,tc))
                    
    def increment(self):  
        if not self.flashed:
            self.value += 1
            if self.value > 9:
                self.flash()
            
    def flash(self):        
        self.flashed = True
        for r,c in self.neighbours:
            self.octopi[r][c].increment()
                
    def cleanup(self):
        if self.flashed:
            self.flashed = False
            self.value = 0
            return 1
        return 0
        
      
values = [i.strip() for i in open("input.txt", "r")]

octopi = []
r = 0
for line in values:
    tmp = []
    for idx in range(len(line)):
        char = line[idx]
        tmp.append(octopus(int(char), (r,idx),octopi))
    octopi.append(tmp)
    r+=1

counter = 0
total = 0
while 1: 
    for r in range(10):
        for c in range(10):
            octopi[r][c].increment()
            
    flashes = 0
    for r in range(10):
        for c in range(10):
           flashes += octopi[r][c].cleanup()
    total += flashes
    counter += 1
    if counter == 100:
        print(total)
    if flashes == 100:
        print(counter)
        break
    