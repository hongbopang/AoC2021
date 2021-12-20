# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:08:14 2021

@author: hongb
"""
import numpy as np

def transform(other,major_ID,minor_ID):
    base = np.array(([1,0,0],[0,1,0],[0,0,1]))
    second_base = np.array(([-1,0,0],[0,1,0],[0,0,-1]))
    major_rotater = np.array(([1,0,0],[0,0,-1],[0,1,0]))
    minor_rotator = np.array(([0,1,0],[0,0,1],[1,0,0]))
    
    
    
    
    if major_ID < 4:
        for _ in range(major_ID):
            base = np.matmul(base,major_rotater)
           
    else:
        base = second_base
        for _ in range(major_ID-4):
            base = np.matmul(base,major_rotater)
    for _ in range(minor_ID):
        base = np.matmul(base,minor_rotator)
    
    return np.matmul(other,base)
    
    


class scanner:
    def __init__(self, idx):
        self.idx = idx
        self.data = []
        if idx == 0:
            self.absolute = (0,0,0)
        else:
            self.absolute = None
        
    def add_data(self,data):
        self.data.append(data)
        
    def cleanup(self):
        self.data = np.array(self.data)
        
        
    def check_for_cohesion(self,other):
        for major_ID in range(8):
            for minor_ID in range(3):
                comparer = transform(other.data,major_ID,minor_ID)
                tmp_dict = dict()
                for row in self.data:
                    for other_row in comparer:
                        line = row - other_row
                        idx = (line[0],line[1],line[2])
                        if idx not in tmp_dict:
                            tmp_dict[idx] = 0
                        tmp_dict[idx] += 1
                    
                    
                
                for key in tmp_dict:
                    if tmp_dict[key] >= 12:                        
                        scannerpos = (self.absolute[0] + key[0],self.absolute[1] + key[1],self.absolute[2] + key[2])
                        return True, scannerpos, major_ID, minor_ID

        
        return False, (0,0,0), -1, -1
    
    
    def normalize(self,maj,minor,position):
        self.data = transform(self.data,maj,minor)
        self.absolute = position

        
        

lines = [i.strip() for i in open("input.txt", "r")]

counter = 0

curr_scan = None

scanners = []

for line in lines:

    if not line: 
        if curr_scan:
            curr_scan.cleanup()
            scanners.append(curr_scan)
        continue
    if line[:3] == '---':
        tmp = scanner(counter)
        counter += 1
        curr_scan=tmp
    else:
        args = list(map(int,line.split(",")))
        curr_scan.add_data(args)
        
curr_scan.cleanup()
scanners.append(curr_scan)   


not_found = [i for i in range(1,len(scanners))]

to_find = [0]

while len(to_find) != 0:
    base = to_find.pop()
    new_not_found = []
    for i in not_found:
        hit, position, maj,minor = scanners[base].check_for_cohesion(scanners[i])
        if hit:

            scanners[i].normalize(maj,minor,position)
            to_find.append(i)
        else:
            new_not_found.append(i)
    
    not_found = [i for i in new_not_found]
full_scan = dict()

for scanner in scanners:
    for row in scanner.data:
        idx = (row[0]+scanner.absolute[0],row[1]+scanner.absolute[1],row[2]+scanner.absolute[2])
        full_scan[idx] = 1
        

print(len(full_scan))

distances = []

for i in range(len(scanners)):
    for j in range(i+1,len(scanners)):
        distances.append(abs(scanners[i].absolute[0] - scanners[j].absolute[0]) + abs(scanners[i].absolute[1] - scanners[j].absolute[1]) + abs(scanners[i].absolute[2] - scanners[j].absolute[2]))
        
print(max(distances))

